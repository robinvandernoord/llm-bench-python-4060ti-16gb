# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "datasets>=2.20.0"
# ]
# ///

# usage: uv run human.py [python js rust ...]

from datasets import load_dataset, Dataset
from pathlib import Path
import typing as t
import random
import re
import shutil
import sys

SAFE_NAME_RE = re.compile(r"[^A-Za-z0-9_.-]")


def safe_name(task_id: str) -> str:
    return SAFE_NAME_RE.sub("_", task_id)


# ----------------- Python -----------------
def generate_python(base_dir: Path, examples: t.Iterable[dict]) -> None:
    lang_dir = base_dir / "python"
    lang_dir.mkdir(parents=True, exist_ok=True)

    for item in examples:
        task_id = item["task_id"]
        task_dir = lang_dir / safe_name(task_id)
        task_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / "__init__.py").touch()

        solution_path = task_dir / "solution.py"
        with solution_path.open("w") as f:
            f.write(f"# {task_id}\n# Prompt:\n")
            for line in item["prompt"].splitlines():
                f.write(f"# {line}\n")
            f.write("\n")
            if declaration := item.get("declaration"):
                f.write(declaration + "\n    pass\n")
            else:
                f.write("# No declaration provided\n")

        test_path = task_dir / f"test_{safe_name(task_id)}.py"
        with test_path.open("w") as f:
            f.write("from .solution import *\n\n")
            f.write(item["test"])

    print(f"Python tasks created in {lang_dir}")
    print(f"Run: cd {lang_dir} && pytest")


# ----------------- Rust -----------------
def generate_rust(base_dir: Path, examples: list[dict]) -> None:
    rust_dir = base_dir / "rust"
    src_dir = rust_dir / "src"
    rust_dir.mkdir(parents=True, exist_ok=True)
    src_dir.mkdir(parents=True, exist_ok=True)

    cargo_toml = rust_dir / "Cargo.toml"
    if not cargo_toml.exists():
        cargo_toml.write_text(
            '[package]\nname = "human_eval"\nversion = "0.1.0"\nedition = "2021"\n'
        )

    mod_lines = []

    for item in examples:
        task_id = safe_name(item["task_id"])
        lib_path = src_dir / f"{task_id}.rs"
        mod_lines.append(f"mod {task_id};")

        with lib_path.open("w") as f:
            # prompt as comments
            f.write(f"// {task_id}\n")
            f.write("// Prompt:\n")
            for line in item["prompt"].splitlines():
                f.write(f"// {line}\n")
            f.write("\n")

            # stub with exactly one pair of braces
            if declaration := item.get("declaration"):
                f.write("%s\n    // TODO: implement\n}\n" % declaration)
            else:
                f.write("// No declaration provided\n")

            f.write("// Tests are below\n" + "\n" * 100)
            f.write(item["test"])

    # minimal lib.rs
    lib_rs = src_dir / "lib.rs"
    with lib_rs.open("w") as f:
        for line in mod_lines:
            f.write(f"{line}\n")

    print(f"Rust tasks created in {rust_dir}")
    print(f"Run: cd {rust_dir} && cargo test")


# ----------------- JavaScript -----------------
def generate_js(base_dir: Path, examples: list[dict]) -> None:
    js_dir = base_dir / "js"
    js_dir.mkdir(parents=True, exist_ok=True)

    for item in examples:
        task_id = safe_name(item["task_id"])
        file_path = js_dir / f"{task_id}.test.js"

        with file_path.open("w") as f:
            # prompt as comments
            f.write(f"// {task_id}\n")
            f.write("// Prompt:\n")
            f.write(item["prompt"])

            # stub with exactly one pair of braces
            if declaration := item.get("declaration"):
                f.write("%s\n    // TODO: implement\n}\n" % declaration)
            else:
                f.write("// No declaration provided\n")

            f.write("// Tests are below\n" + "\n" * 100)
            f.write(item["test"])

    print(f"JS tasks created in {js_dir}")
    print(f"Run: cd {js_dir} && bun test")


# ----------------- Main -----------------
LANG_GENERATORS = {
    "python": generate_python,
    "rust": generate_rust,
    "js": generate_js,
}


def main(langs: list[str]) -> None:
    base_dir = Path("/tmp/benchllama_human_eval_pack")
    if base_dir.exists():
        shutil.rmtree(base_dir)
    base_dir.mkdir(parents=True, exist_ok=True)

    for lang in langs:
        ds = load_dataset("bigcode/humanevalpack", lang)["test"]
        # pick 10 examples here
        indices = random.sample(range(len(ds)), 10)
        generator = LANG_GENERATORS[lang]
        generator(base_dir, (ds[i] for i in indices))


if __name__ == "__main__":
    langs = sys.argv[1:] if len(sys.argv) > 1 else ["python", "js", "rust"]
    main(langs)

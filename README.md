# LLM Bench Python 4060Ti 16GB

This repository stores **benchmark results** for Python code generation on local LLMs using a **4060 Ti with 16GB VRAM**.  
Benchmarks were generated with [benchllama](https://github.com/srikanth235/benchllama).

## Overview

- **Task**: Python code generation
- **Models tested**: Various Ollama-compatible LLMs
- **Hardware**: NVIDIA 4060 Ti (16GB)
- **Metric of interest**: **Correctness** – fraction of test samples for which the model’s first solution passes all tests

## Results

| Model            | Correctness | Eval Duration (s) |
| ---------------- | ----------- | ----------------- |
| gemma3:12b       | 1.000       | 6.245             |
| qwen3:14b        | 1.000       | 172.499           |
| mistral:7b       | 0.667       | 7.019             |
| mistral-nemo:12b | 0.667       | 8.882             |
| deepseek-r1:14b  | 0.667       | 169.324           |
| gemma3n\:e4b     | 0.333       | 8.938             |
| gpt-oss:20b      | 0.333       | 74.766            |


## Usage

Run benchmarks with:

```bash
benchllama evaluate --models <model> --languages python --samples 3 --eval
```

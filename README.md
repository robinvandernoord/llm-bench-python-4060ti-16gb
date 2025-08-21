# LLM Bench Python 4060Ti 16GB

This repository stores **benchmark results** for Python code generation on local LLMs using a **4060 Ti with 16GB VRAM
**.  
Benchmarks were generated with [benchllama](https://github.com/srikanth235/benchllama).

## Overview

- **Task**: Python code generation
- **Models tested**: Various Ollama-compatible LLMs
- **Hardware**: NVIDIA 4060 Ti (16GB)
- **Metric of interest**: **Correctness** – fraction of test samples for which the model’s first solution passes all
  tests

## Results

| Model            | Correctness | Eval Duration (s) | Memory Usage           |
|------------------|-------------|-------------------|------------------------|
| gemma3:12b       | 1.000       | 6.245             | 11 GB; 100% GPU        |
| qwen3-coder:30b  | 1.000       | 19.581            | 20 GB; 26%/74% CPU/GPU |
| qwen3:14b        | 1.000       | 172.499           | 10 GB; 100% GPU        |
| mistral:7b       | 0.667       | 7.019             | 5.8 GB; 100% GPU       |
| mistral-nemo:12b | 0.667       | 8.882             | 8.3 GB; 100% GPU       |
| deepseek-r1:14b  | 0.667       | 169.324           | 10 GB; 100% GPU        |
| gemma3n:e4b      | 0.333       | 8.938             | 5.8 GB; 100% GPU       |
| gpt-oss:20b      | 0.333       | 74.766            | 18 GB; 17%/83% CPU/GPU |

## Usage

Run benchmarks with:

```bash
benchllama evaluate --models <model> --languages python --samples 3 --eval
```

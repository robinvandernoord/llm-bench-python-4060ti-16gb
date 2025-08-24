# LLM Bench Python 4060Ti 16GB

This repository stores **benchmark results** for (Python) code generation on local LLMs using a **4060 Ti with 16GB VRAM
**.  
Benchmarks were generated with [benchllama](https://github.com/srikanth235/benchllama).

## Overview

- **Task**: (Python) code generation
- **Models tested**: Various Ollama-compatible LLMs
- **Hardware**: NVIDIA 4060 Ti (16GB)
- **Metric of interest**: **Correctness** – fraction of test samples for which the model’s first solution passes all
  tests

## Triage Combined Results (10 samples per language)

 Model            | Memory Usage           | Python Correctness | Python Duration (s) | JS Correctness | JS Duration (s) | Rust Correctness | Rust Duration (s) | Avg Correctness |
|------------------|------------------------|--------------------|---------------------|----------------|-----------------|------------------|-------------------|-----------------|
| gemma3:12b       | 11 GB; 100% GPU        | 0.6                | 8.510               | 0.9            | 5.078           | 0.8              | 22.277            | 0.77            |
| qwen3-coder:30b  | 20 GB; 25%/75% CPU/GPU | 0.9                | 24.865              | 0.7            | 17.800          | 0.2              | 27.840            | 0.60            |
| qwen3:14b        | 10 GB; 100% GPU        | 0.7                | 116.899             | 0.7            | 112.468         | 0.4              | 187.583           | 0.60            |
| deepseek-r1:14b  | 10 GB; 100% GPU        | 0.7                | 132.081             | 0.6            | 173.481         | 0.4              | 205.081           | 0.57            |
| gemma3n:e4b      | 5.8 GB; 100% GPU       | 0.7                | 4.958               | 0.6            | 5.444           | 0.0              | 17.887            | 0.43            |
| mistral-nemo:12b | 8.3 GB; 100% GPU       | 0.3                | 6.990               | 0.8            | 6.494           | 0.0              | 7.641             | 0.37            |
| qwen2.5-coder:7b | 5.6 GB; 100% GPU       | 0.0                | 9.000               | 0.0            | 11.177          | 0.8              | 10.769            | 0.27            |
| mistral:7b       | 5.8 GB; 100% GPU       | 0.3                | 5.932               | 0.2            | 5.933           | 0.2              | 6.900             | 0.23            |
| codellama:7b [1] | 6.9 GB; 100% GPU       | 0.0                | 3.371               | 0.0            | 5.301           | 0.0              | 5.616             | 0.0             |
| gpt-oss:20b [2]  | 18 GB; 17%/83% CPU/GPU | ?                  | ?                   | ?              | ?               | ?                | ?                 | ?               |

These results are used as an initial triage to determine which to further explore,
because the full run takes a long time with almost 500 tests across multiple languages.
The threshold is set to an avg. correctness of 0.7 across the three languages.

[1] `codellama` always generated extra non-code text, causing the tests to fail  
[2]` gpt-oss` takes forever before giving any answers.

## Results for all samples Python + JS + Rust

 Model      | Python Correctness | Python Duration (s) | JS Correctness | JS Duration (s) | Rust Correctness | Rust Duration (s) | Avg Correctness |
|------------|--------------------|---------------------|----------------|-----------------|------------------|-------------------|-----------------|
| gemma3:12b | ?                  | ?                   | ?              | ?               | ?                | ?                 | ?               |

## Usage

Run benchmarks with:

```bash
benchllama evaluate --models <model> --languages python --samples 10 --eval
benchllama evaluate --models <model> --languages python --languages js --languages rust --eval
```

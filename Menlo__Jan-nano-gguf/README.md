---
quantized_by: Menlo
pipeline_tag: text-generation
base_model: Menlo/Jan-nano
base_model_relation: quantized
license: apache-2.0
---
# Jan Nano

Authors: [Alan Dao](https://scholar.google.com/citations?user=eGWws2UAAAAJ&hl=en), [Bach Vu Dinh](https://scholar.google.com/citations?user=7Lr6hdoAAAAJ&hl=vi), [Thinh Le](https://scholar.google.com/citations?user=8tcN7xMAAAAJ&hl=en)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/657a81129ea9d52e5cbd67f7/YQci8jiHjAAFpXWYOadrU.png)

## Overview

Jan Nano is a fine-tuned language model built on top of the Qwen3 architecture. Developed as part of the Jan ecosystem, it balances compact size and extended context length, making it ideal for efficient, high-quality text generation in local or embedded environments.

## Features

- **Tool Use**: Excellent function calling and tool integration
- **Research**: Enhanced research and information processing capabilities
- **Small Model**: VRAM efficient for local deployment

## Use it with Jan (UI)

1. Install **Jan** using [Quickstart](https://jan.ai/docs/quickstart)

Original weight: https://huggingface.co/Menlo/Jan-nano

## Recommended Sampling Parameters

- Temperature: 0.7
- Top-p: 0.8
- Top-k: 20
- Min-p: 0

## Documentation
[Setup, Usage & FAQ](https://menloresearch.github.io/deep-research/)
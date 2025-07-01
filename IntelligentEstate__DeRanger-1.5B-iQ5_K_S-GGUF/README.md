---
license: cc-by-nc-4.0
language:
- en
pipeline_tag: text-generation
tags:
- nvidia
- AceMath
- math
- CoT
- pytorch
- llama-cpp
base_model: nvidia/AceMath-1.5B-Instruct
---

# IntelligentEstate/DeRanger-1.5B-iQ5_K_S-GGUF

A little Helper for all your Impish needs, Excellent at math and coding for it's size. If you enable bad hehavior it will behave badly.

![Deranger.png](https://cdn-uploads.huggingface.co/production/uploads/6593502ca2607099284523db/8VYqIdLs7eKUuBT5rbQQV.png)

This model Is meant to give Android devices a functional AI with 70B style capabilities. It is not censored and has simple instruction base template. It was quantized using a custom importance matrix to GGUF format from [`nvidia/AceMath-1.5B-Instruct`](https://huggingface.co/nvidia/AceMath-1.5B-Instruct)

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.
---
tags:
- quantized
- 2-bit
- 3-bit
- 4-bit
- 5-bit
- 6-bit
- 8-bit
- GGUF
- transformers
- safetensors
- mistral
- text-generation
- arxiv:2304.12244
- arxiv:2306.08568
- arxiv:2308.09583
- license:apache-2.0
- autotrain_compatible
- endpoints_compatible
- text-generation-inference
- region:us
- text-generation
model_name: WizardLM-2-8x22B-GGUF
base_model: microsoft/WizardLM-2-8x22B
inference: false
model_creator: microsoft
pipeline_tag: text-generation
quantized_by: MaziyarPanahi
---
# [MaziyarPanahi/WizardLM-2-8x22B-GGUF](https://huggingface.co/MaziyarPanahi/WizardLM-2-8x22B-GGUF)
- Model creator: [microsoft](https://huggingface.co/microsoft)
- Original model: [microsoft/WizardLM-2-8x22B](https://huggingface.co/microsoft/WizardLM-2-8x22B)

## Description
[MaziyarPanahi/WizardLM-2-8x22B-GGUF](https://huggingface.co/MaziyarPanahi/WizardLM-2-8x22B-GGUF) contains GGUF format model files for [microsoft/WizardLM-2-8x22B](https://huggingface.co/microsoft/WizardLM-2-8x22B).

## How to download
You can download only the quants you need instead of cloning the entire repository as follows:


```
huggingface-cli download MaziyarPanahi/WizardLM-2-8x22B-GGUF --local-dir . --include '*Q2_K*gguf'
```

On Windows:

```sh
huggingface-cli download MaziyarPanahi/WizardLM-2-8x22B-GGUF --local-dir . --include *Q4_K_S*gguf
```

## Load sharded model

`llama_load_model_from_file` will detect the number of files and will load additional tensors from the rest of files.

```sh
llama.cpp/main -m WizardLM-2-8x22B.Q2_K-00001-of-00005.gguf -p "Building a website can be done in 10 simple steps:\nStep 1:" -n 1024 -e
```

## Prompt template

```
{system_prompt}
USER: {prompt}
ASSISTANT: </s>
```

or

```
A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful, 
detailed, and polite answers to the user's questions. USER: Hi ASSISTANT: Hello.</s>
USER: {prompt} ASSISTANT: </s>......
```

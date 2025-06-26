---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-8B/blob/main/LICENSE
pipeline_tag: text-generation
base_model: Alphatao/Affine-9459823
tags:
- TensorBlock
- GGUF
---

<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/jC7kdl8.jpeg" alt="TensorBlock" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>

[![Website](https://img.shields.io/badge/Website-tensorblock.co-blue?logo=google-chrome&logoColor=white)](https://tensorblock.co)
[![Twitter](https://img.shields.io/twitter/follow/tensorblock_aoi?style=social)](https://twitter.com/tensorblock_aoi)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white)](https://discord.gg/Ej5NmeHFf2)
[![GitHub](https://img.shields.io/badge/GitHub-TensorBlock-black?logo=github&logoColor=white)](https://github.com/TensorBlock)
[![Telegram](https://img.shields.io/badge/Telegram-Group-blue?logo=telegram)](https://t.me/TensorBlock)


## Alphatao/Affine-9459823 - GGUF

This repo contains GGUF format model files for [Alphatao/Affine-9459823](https://huggingface.co/Alphatao/Affine-9459823).

The files were quantized using machines provided by [TensorBlock](https://tensorblock.co/), and they are compatible with llama.cpp as of [commit b5753](https://github.com/ggml-org/llama.cpp/commit/73e53dc834c0a2336cd104473af6897197b96277).

## Our projects
<table border="1" cellspacing="0" cellpadding="10">
<tr>
  <th style="font-size: 25px;">Awesome MCP Servers</th>
  <th style="font-size: 25px;">TensorBlock Studio</th>
</tr>
  <tr>
    <th><img src="https://imgur.com/2Xov7B7.jpeg" alt="Project A" width="450"/></th>
    <th><img src="https://imgur.com/pJcmF5u.jpeg" alt="Project B" width="450"/></th>
  </tr>
  <tr>
    <th>A comprehensive collection of Model Context Protocol (MCP) servers.</th>
    <th>A lightweight, open, and extensible multi-LLM interaction studio.</th>
  </tr>
<tr>
  <th>
    <a href="https://github.com/TensorBlock/awesome-mcp-servers" target="_blank" style="
      display: inline-block;
      padding: 8px 16px;
      background-color: #FF7F50;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-weight: bold;
      font-family: sans-serif;
    ">👀 See what we built 👀</a>
  </th>
  <th>
    <a href="https://github.com/TensorBlock/TensorBlock-Studio" target="_blank" style="
      display: inline-block;
      padding: 8px 16px;
      background-color: #FF7F50;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-weight: bold;
      font-family: sans-serif;
    ">👀 See what we built 👀</a>
  </th>
</tr>
</table>

## Prompt template

```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
```

## Model file specification

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [Affine-9459823-Q2_K.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q2_K.gguf) | Q2_K | 3.282 GB | smallest, significant quality loss - not recommended for most purposes |
| [Affine-9459823-Q3_K_S.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q3_K_S.gguf) | Q3_K_S | 3.770 GB | very small, high quality loss |
| [Affine-9459823-Q3_K_M.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q3_K_M.gguf) | Q3_K_M | 4.124 GB | very small, high quality loss |
| [Affine-9459823-Q3_K_L.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q3_K_L.gguf) | Q3_K_L | 4.431 GB | small, substantial quality loss |
| [Affine-9459823-Q4_0.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q4_0.gguf) | Q4_0 | 4.775 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [Affine-9459823-Q4_K_S.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q4_K_S.gguf) | Q4_K_S | 4.802 GB | small, greater quality loss |
| [Affine-9459823-Q4_K_M.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q4_K_M.gguf) | Q4_K_M | 5.028 GB | medium, balanced quality - recommended |
| [Affine-9459823-Q5_0.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q5_0.gguf) | Q5_0 | 5.721 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [Affine-9459823-Q5_K_S.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q5_K_S.gguf) | Q5_K_S | 5.721 GB | large, low quality loss - recommended |
| [Affine-9459823-Q5_K_M.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q5_K_M.gguf) | Q5_K_M | 5.851 GB | large, very low quality loss - recommended |
| [Affine-9459823-Q6_K.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q6_K.gguf) | Q6_K | 6.726 GB | very large, extremely low quality loss |
| [Affine-9459823-Q8_0.gguf](https://huggingface.co/tensorblock/Alphatao_Affine-9459823-GGUF/blob/main/Affine-9459823-Q8_0.gguf) | Q8_0 | 8.710 GB | very large, extremely low quality loss - not recommended |


## Downloading instruction

### Command line

Firstly, install Huggingface Client

```shell
pip install -U "huggingface_hub[cli]"
```

Then, downoad the individual model file the a local directory

```shell
huggingface-cli download tensorblock/Alphatao_Affine-9459823-GGUF --include "Affine-9459823-Q2_K.gguf" --local-dir MY_LOCAL_DIR
```

If you wanna download multiple model files with a pattern (e.g., `*Q4_K*gguf`), you can try:

```shell
huggingface-cli download tensorblock/Alphatao_Affine-9459823-GGUF --local-dir MY_LOCAL_DIR --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

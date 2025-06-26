---
library_name: transformers
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
license: cc-by-nc-4.0
quantized_by: bartowski
pipeline_tag: text-generation
base_model: CohereForAI/aya-23-8B
---

## Llamacpp imatrix Quantizations of aya-23-8B

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b2965">b2965</a> for quantization.

Original model: https://huggingface.co/CohereForAI/aya-23-8B

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/b6ac44691e994344625687afe3263b3a)

## Prompt format

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>{system_prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [aya-23-8B-Q8_0.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q8_0.gguf) | Q8_0 | 8.54GB | Extremely high quality, generally unneeded but max available quant. |
| [aya-23-8B-Q6_K.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q6_K.gguf) | Q6_K | 6.59GB | Very high quality, near perfect, *recommended*. |
| [aya-23-8B-Q5_K_M.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q5_K_M.gguf) | Q5_K_M | 5.80GB | High quality, *recommended*. |
| [aya-23-8B-Q5_K_S.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q5_K_S.gguf) | Q5_K_S | 5.66GB | High quality, *recommended*. |
| [aya-23-8B-Q4_K_M.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q4_K_M.gguf) | Q4_K_M | 5.05GB | Good quality, uses about 4.83 bits per weight, *recommended*. |
| [aya-23-8B-Q4_K_S.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q4_K_S.gguf) | Q4_K_S | 4.82GB | Slightly lower quality with more space savings, *recommended*. |
| [aya-23-8B-IQ4_NL.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ4_NL.gguf) | IQ4_NL | 4.81GB | Decent quality, slightly smaller than Q4_K_S with similar performance *recommended*. |
| [aya-23-8B-IQ4_XS.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ4_XS.gguf) | IQ4_XS | 4.60GB | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [aya-23-8B-Q3_K_L.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q3_K_L.gguf) | Q3_K_L | 4.52GB | Lower quality but usable, good for low RAM availability. |
| [aya-23-8B-Q3_K_M.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q3_K_M.gguf) | Q3_K_M | 4.22GB | Even lower quality. |
| [aya-23-8B-IQ3_M.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ3_M.gguf) | IQ3_M | 3.99GB | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [aya-23-8B-IQ3_S.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ3_S.gguf) | IQ3_S | 3.88GB | Lower quality, new method with decent performance, recommended over Q3_K_S quant, same size with better performance. |
| [aya-23-8B-Q3_K_S.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q3_K_S.gguf) | Q3_K_S | 3.87GB | Low quality, not recommended. |
| [aya-23-8B-IQ3_XS.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ3_XS.gguf) | IQ3_XS | 3.72GB | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [aya-23-8B-IQ3_XXS.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ3_XXS.gguf) | IQ3_XXS | 3.41GB | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [aya-23-8B-Q2_K.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-Q2_K.gguf) | Q2_K | 3.43GB | Very low quality but surprisingly usable. |
| [aya-23-8B-IQ2_M.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ2_M.gguf) | IQ2_M | 3.08GB | Very low quality, uses SOTA techniques to also be surprisingly usable. |
| [aya-23-8B-IQ2_S.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ2_S.gguf) | IQ2_S | 2.89GB | Very low quality, uses SOTA techniques to be usable. |
| [aya-23-8B-IQ2_XS.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ2_XS.gguf) | IQ2_XS | 2.79GB | Very low quality, uses SOTA techniques to be usable. |
| [aya-23-8B-IQ2_XXS.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ2_XXS.gguf) | IQ2_XXS | 2.58GB | Lower quality, uses SOTA techniques to be usable. |
| [aya-23-8B-IQ1_M.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ1_M.gguf) | IQ1_M | 2.35GB | Extremely low quality, *not* recommended. |
| [aya-23-8B-IQ1_S.gguf](https://huggingface.co/bartowski/aya-23-8B-GGUF/blob/main/aya-23-8B-IQ1_S.gguf) | IQ1_S | 2.20GB | Extremely low quality, *not* recommended. |

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/aya-23-8B-GGUF --include "aya-23-8B-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/aya-23-8B-GGUF --include "aya-23-8B-Q8_0.gguf/*" --local-dir aya-23-8B-Q8_0
```

You can either specify a new local-dir (aya-23-8B-Q8_0) or download them all in place (./)

## Which file should I choose?

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski

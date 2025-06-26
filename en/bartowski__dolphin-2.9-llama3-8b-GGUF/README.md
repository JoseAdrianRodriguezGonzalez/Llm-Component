---
base_model: cognitivecomputations/dolphin-2.9-llama3-8b
datasets:
- cognitivecomputations/Dolphin-2.9
- teknium/OpenHermes-2.5
- m-a-p/CodeFeedback-Filtered-Instruction
- cognitivecomputations/dolphin-coder
- cognitivecomputations/samantha-data
- HuggingFaceH4/ultrachat_200k
- microsoft/orca-math-word-problems-200k
- abacusai/SystemChat-1.1
- Locutusque/function-calling-chatml
- internlm/Agent-FLAN
license: other
pipeline_tag: text-generation
tags:
- generated_from_trainer
- axolotl
quantized_by: bartowski
model-index:
- name: out
  results: []
---

## Llamacpp imatrix Quantizations of dolphin-2.9-llama3-8b

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3991">b3991</a> for quantization.

Original model: https://huggingface.co/cognitivecomputations/dolphin-2.9-llama3-8b

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

```
<|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
```

## What's new:

Updating with new quants

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [dolphin-2.9-llama3-8b-f16.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-f16.gguf) | f16 | 16.07GB | false | Full F16 weights. |
| [dolphin-2.9-llama3-8b-Q8_0.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q8_0.gguf) | Q8_0 | 8.54GB | false | Extremely high quality, generally unneeded but max available quant. |
| [dolphin-2.9-llama3-8b-Q6_K_L.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q6_K_L.gguf) | Q6_K_L | 6.85GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [dolphin-2.9-llama3-8b-Q6_K.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q6_K.gguf) | Q6_K | 6.60GB | false | Very high quality, near perfect, *recommended*. |
| [dolphin-2.9-llama3-8b-Q5_K_L.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q5_K_L.gguf) | Q5_K_L | 6.06GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [dolphin-2.9-llama3-8b-Q5_K_M.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q5_K_M.gguf) | Q5_K_M | 5.73GB | false | High quality, *recommended*. |
| [dolphin-2.9-llama3-8b-Q5_K_S.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q5_K_S.gguf) | Q5_K_S | 5.60GB | false | High quality, *recommended*. |
| [dolphin-2.9-llama3-8b-Q4_K_L.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q4_K_L.gguf) | Q4_K_L | 5.31GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [dolphin-2.9-llama3-8b-Q4_K_M.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q4_K_M.gguf) | Q4_K_M | 4.92GB | false | Good quality, default size for must use cases, *recommended*. |
| [dolphin-2.9-llama3-8b-Q3_K_XL.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q3_K_XL.gguf) | Q3_K_XL | 4.78GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [dolphin-2.9-llama3-8b-Q4_K_S.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q4_K_S.gguf) | Q4_K_S | 4.69GB | false | Slightly lower quality with more space savings, *recommended*. |
| [dolphin-2.9-llama3-8b-Q4_0.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q4_0.gguf) | Q4_0 | 4.68GB | false | Legacy format, generally not worth using over similarly sized formats |
| [dolphin-2.9-llama3-8b-IQ4_NL.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ4_NL.gguf) | IQ4_NL | 4.68GB | false | Similar to IQ4_XS, but slightly larger. |
| [dolphin-2.9-llama3-8b-Q4_0_8_8.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q4_0_8_8.gguf) | Q4_0_8_8 | 4.66GB | false | Optimized for ARM inference. Requires 'sve' support (see link below). *Don't use on Mac or Windows*. |
| [dolphin-2.9-llama3-8b-Q4_0_4_8.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q4_0_4_8.gguf) | Q4_0_4_8 | 4.66GB | false | Optimized for ARM inference. Requires 'i8mm' support (see link below). *Don't use on Mac or Windows*. |
| [dolphin-2.9-llama3-8b-Q4_0_4_4.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q4_0_4_4.gguf) | Q4_0_4_4 | 4.66GB | false | Optimized for ARM inference. Should work well on all ARM chips, pick this if you're unsure. *Don't use on Mac or Windows*. |
| [dolphin-2.9-llama3-8b-IQ4_XS.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ4_XS.gguf) | IQ4_XS | 4.45GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [dolphin-2.9-llama3-8b-Q3_K_L.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q3_K_L.gguf) | Q3_K_L | 4.32GB | false | Lower quality but usable, good for low RAM availability. |
| [dolphin-2.9-llama3-8b-Q3_K_M.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q3_K_M.gguf) | Q3_K_M | 4.02GB | false | Low quality. |
| [dolphin-2.9-llama3-8b-IQ3_M.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ3_M.gguf) | IQ3_M | 3.78GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [dolphin-2.9-llama3-8b-Q2_K_L.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q2_K_L.gguf) | Q2_K_L | 3.69GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [dolphin-2.9-llama3-8b-Q3_K_S.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q3_K_S.gguf) | Q3_K_S | 3.66GB | false | Low quality, not recommended. |
| [dolphin-2.9-llama3-8b-IQ3_XS.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ3_XS.gguf) | IQ3_XS | 3.52GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [dolphin-2.9-llama3-8b-IQ3_XXS.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ3_XXS.gguf) | IQ3_XXS | 3.27GB | false | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [dolphin-2.9-llama3-8b-Q2_K.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-Q2_K.gguf) | Q2_K | 3.18GB | false | Very low quality but surprisingly usable. |
| [dolphin-2.9-llama3-8b-IQ2_M.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ2_M.gguf) | IQ2_M | 2.95GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [dolphin-2.9-llama3-8b-IQ2_S.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ2_S.gguf) | IQ2_S | 2.76GB | false | Low quality, uses SOTA techniques to be usable. |
| [dolphin-2.9-llama3-8b-IQ2_XS.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ2_XS.gguf) | IQ2_XS | 2.61GB | false | Low quality, uses SOTA techniques to be usable. |
| [dolphin-2.9-llama3-8b-IQ2_XXS.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ2_XXS.gguf) | IQ2_XXS | 2.40GB | false | Very low quality, uses SOTA techniques to be usable. |
| [dolphin-2.9-llama3-8b-IQ1_M.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ1_M.gguf) | IQ1_M | 2.16GB | false | Extremely low quality, *not* recommended. |
| [dolphin-2.9-llama3-8b-IQ1_S.gguf](https://huggingface.co/bartowski/dolphin-2.9-llama3-8b-GGUF/blob/main/dolphin-2.9-llama3-8b-IQ1_S.gguf) | IQ1_S | 2.02GB | false | Extremely low quality, *not* recommended. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

Some say that this improves the quality, others don't notice any difference. If you use these models PLEASE COMMENT with your findings. I would like feedback that these are actually used and useful so I don't keep uploading quants no one is using.

Thanks!

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/dolphin-2.9-llama3-8b-GGUF --include "dolphin-2.9-llama3-8b-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/dolphin-2.9-llama3-8b-GGUF --include "dolphin-2.9-llama3-8b-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (dolphin-2.9-llama3-8b-Q8_0) or download them all in place (./)

## Q4_0_X_X

These are *NOT* for Metal (Apple) offloading, only ARM chips.

If you're using an ARM chip, the Q4_0_X_X quants will have a substantial speedup. Check out Q4_0_4_4 speed comparisons [on the original pull request](https://github.com/ggerganov/llama.cpp/pull/5780#pullrequestreview-21657544660)

To check which one would work best for your ARM chip, you can check [AArch64 SoC features](https://gpages.juszkiewicz.com.pl/arm-socs-table/arm-socs.html) (thanks EloyOn!).

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

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset

Thank you ZeroWw for the inspiration to experiment with embed/output

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski

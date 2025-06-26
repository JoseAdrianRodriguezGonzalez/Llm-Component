---
base_model: mistralai/Mistral-Large-Instruct-2407
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
pipeline_tag: text-generation
quantized_by: bartowski
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
---

## Llamacpp imatrix Quantizations of Mistral-Large-Instruct-2407

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3634">b3634</a> for quantization.

Original model: https://huggingface.co/mistralai/Mistral-Large-Instruct-2407

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

```
<s>[INST] {prompt}[/INST] 
```

## What's new:

Add chat template, some new sizes

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [Mistral-Large-Instruct-2407-Q8_0.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q8_0) | Q8_0 | 130.28GB | true | Extremely high quality, generally unneeded but max available quant. |
| [Mistral-Large-Instruct-2407-Q6_K.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q6_K) | Q6_K | 100.59GB | true | Very high quality, near perfect, *recommended*. |
| [Mistral-Large-Instruct-2407-Q5_K_M.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q5_K_M) | Q5_K_M | 86.49GB | true | High quality, *recommended*. |
| [Mistral-Large-Instruct-2407-Q4_K_M.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q4_K_M) | Q4_K_M | 73.22GB | true | Good quality, default size for must use cases, *recommended*. |
| [Mistral-Large-Instruct-2407-Q4_K_S.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q4_K_S) | Q4_K_S | 69.57GB | true | Slightly lower quality with more space savings, *recommended*. |
| [Mistral-Large-Instruct-2407-Q4_0.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q4_0) | Q4_0 | 69.32GB | true | Legacy format, generally not worth using over similarly sized formats |
| [Mistral-Large-Instruct-2407-Q4_0_4_4.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q4_0_4_4) | Q4_0_4_4 | 69.08GB | true | Optimized for ARM and CPU inference, much faster than Q4_0 at similar quality. |
| [Mistral-Large-Instruct-2407-IQ4_XS.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-IQ4_XS) | IQ4_XS | 65.43GB | true | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Mistral-Large-Instruct-2407-Q3_K_XL.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q3_K_XL) | Q3_K_XL | 64.91GB | true | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [Mistral-Large-Instruct-2407-Q3_K_L.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q3_K_L) | Q3_K_L | 64.55GB | true | Lower quality but usable, good for low RAM availability. |
| [Mistral-Large-Instruct-2407-Q3_K_M.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q3_K_M) | Q3_K_M | 59.10GB | true | Low quality. |
| [Mistral-Large-Instruct-2407-IQ3_M.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-IQ3_M) | IQ3_M | 55.28GB | true | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Mistral-Large-Instruct-2407-Q3_K_S.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/tree/main/Mistral-Large-Instruct-2407-Q3_K_S) | Q3_K_S | 52.85GB | true | Low quality, not recommended. |
| [Mistral-Large-Instruct-2407-IQ3_XXS.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-IQ3_XXS.gguf) | IQ3_XXS | 47.01GB | false | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [Mistral-Large-Instruct-2407-Q2_K_L.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q2_K_L.gguf) | Q2_K_L | 45.59GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [Mistral-Large-Instruct-2407-Q2_K.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-Q2_K.gguf) | Q2_K | 45.20GB | false | Very low quality but surprisingly usable. |
| [Mistral-Large-Instruct-2407-IQ2_M.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-IQ2_M.gguf) | IQ2_M | 41.62GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [Mistral-Large-Instruct-2407-IQ2_XS.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-IQ2_XS.gguf) | IQ2_XS | 36.08GB | false | Low quality, uses SOTA techniques to be usable. |
| [Mistral-Large-Instruct-2407-IQ2_XXS.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-IQ2_XXS.gguf) | IQ2_XXS | 32.43GB | false | Very low quality, uses SOTA techniques to be usable. |
| [Mistral-Large-Instruct-2407-IQ1_M.gguf](https://huggingface.co/bartowski/Mistral-Large-Instruct-2407-GGUF/blob/main/Mistral-Large-Instruct-2407-IQ1_M.gguf) | IQ1_M | 28.39GB | false | Extremely low quality, *not* recommended. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

Some say that this improves the quality, others don't notice any difference. If you use these models PLEASE COMMENT with your findings. I would like feedback that these are actually used and useful so I don't keep uploading quants no one is using.

Thanks!

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset

Thank you ZeroWw for the inspiration to experiment with embed/output

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/Mistral-Large-Instruct-2407-GGUF --include "Mistral-Large-Instruct-2407-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/Mistral-Large-Instruct-2407-GGUF --include "Mistral-Large-Instruct-2407-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (Mistral-Large-Instruct-2407-Q8_0) or download them all in place (./)

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


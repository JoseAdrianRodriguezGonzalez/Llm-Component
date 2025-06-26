---
license: other
license_name: deepseek-license
license_link: LICENSE
quantized_by: bartowski
pipeline_tag: text-generation
---

## Llamacpp imatrix Quantizations of DeepSeek-Coder-V2-Lite-Instruct

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3166">b3166</a> for quantization.

Original model: https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

## Prompt format

```
<｜begin▁of▁sentence｜>{system_prompt}

User: {prompt}

Assistant: <｜end▁of▁sentence｜>Assistant:
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Description |
| -------- | ---------- | --------- | ----------- |
| [DeepSeek-Coder-V2-Lite-Instruct-Q8_0_L.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q8_0_L.gguf) | Q8_0_L | 17.09GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. Extremely high quality, generally unneeded but max available quant. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q8_0.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q8_0.gguf) | Q8_0 | 16.70GB | Extremely high quality, generally unneeded but max available quant. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q6_K_L.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q6_K_L.gguf) | Q6_K_L | 14.56GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. Very high quality, near perfect, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q6_K.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q6_K.gguf) | Q6_K | 14.06GB | Very high quality, near perfect, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q5_K_L.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q5_K_L.gguf) | Q5_K_L | 12.37GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. High quality, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q5_K_M.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q5_K_M.gguf) | Q5_K_M | 11.85GB | High quality, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q5_K_S.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q5_K_S.gguf) | Q5_K_S | 11.14GB | High quality, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q4_K_L.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q4_K_L.gguf) | Q4_K_L | 10.91GB | *Experimental*, uses f16 for embed and output weights. Please provide any feedback of differences. Good quality, uses about 4.83 bits per weight, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf) | Q4_K_M | 10.36GB | Good quality, uses about 4.83 bits per weight, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q4_K_S.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q4_K_S.gguf) | Q4_K_S | 9.53GB | Slightly lower quality with more space savings, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-IQ4_XS.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-IQ4_XS.gguf) | IQ4_XS | 8.57GB | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q3_K_L.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q3_K_L.gguf) | Q3_K_L | 8.45GB | Lower quality but usable, good for low RAM availability. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q3_K_M.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q3_K_M.gguf) | Q3_K_M | 8.12GB | Even lower quality. |
| [DeepSeek-Coder-V2-Lite-Instruct-IQ3_M.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-IQ3_M.gguf) | IQ3_M | 7.55GB | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q3_K_S.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q3_K_S.gguf) | Q3_K_S | 7.48GB | Low quality, not recommended. |
| [DeepSeek-Coder-V2-Lite-Instruct-IQ3_XS.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-IQ3_XS.gguf) | IQ3_XS | 7.12GB | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [DeepSeek-Coder-V2-Lite-Instruct-IQ3_XXS.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-IQ3_XXS.gguf) | IQ3_XXS | 6.96GB | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [DeepSeek-Coder-V2-Lite-Instruct-Q2_K.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-Q2_K.gguf) | Q2_K | 6.43GB | Very low quality but surprisingly usable. |
| [DeepSeek-Coder-V2-Lite-Instruct-IQ2_M.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-IQ2_M.gguf) | IQ2_M | 6.32GB | Very low quality, uses SOTA techniques to also be surprisingly usable. |
| [DeepSeek-Coder-V2-Lite-Instruct-IQ2_S.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-IQ2_S.gguf) | IQ2_S | 6.00GB | Very low quality, uses SOTA techniques to be usable. |
| [DeepSeek-Coder-V2-Lite-Instruct-IQ2_XS.gguf](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF/blob/main/DeepSeek-Coder-V2-Lite-Instruct-IQ2_XS.gguf) | IQ2_XS | 5.96GB | Very low quality, uses SOTA techniques to be usable. |

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF --include "DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF --include "DeepSeek-Coder-V2-Lite-Instruct-Q8_0.gguf/*" --local-dir DeepSeek-Coder-V2-Lite-Instruct-Q8_0
```

You can either specify a new local-dir (DeepSeek-Coder-V2-Lite-Instruct-Q8_0) or download them all in place (./)

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

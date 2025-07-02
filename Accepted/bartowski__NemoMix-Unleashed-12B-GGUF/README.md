---
base_model: MarinaraSpaghetti/NemoMix-Unleashed-12B
library_name: transformers
pipeline_tag: text-generation
tags:
- mergekit
- merge
quantized_by: bartowski
---

## Llamacpp imatrix Quantizations of NemoMix-Unleashed-12B

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3600">b3600</a> for quantization.

Original model: https://huggingface.co/MarinaraSpaghetti/NemoMix-Unleashed-12B

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

No prompt format found, check original model page

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [NemoMix-Unleashed-12B-f16.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-f16.gguf) | f16 | 24.50GB | false | Full F16 weights. |
| [NemoMix-Unleashed-12B-Q8_0.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q8_0.gguf) | Q8_0 | 13.02GB | false | Extremely high quality, generally unneeded but max available quant. |
| [NemoMix-Unleashed-12B-Q6_K_L.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q6_K_L.gguf) | Q6_K_L | 10.38GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [NemoMix-Unleashed-12B-Q6_K.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q6_K.gguf) | Q6_K | 10.06GB | false | Very high quality, near perfect, *recommended*. |
| [NemoMix-Unleashed-12B-Q5_K_L.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q5_K_L.gguf) | Q5_K_L | 9.14GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [NemoMix-Unleashed-12B-Q5_K_M.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q5_K_M.gguf) | Q5_K_M | 8.73GB | false | High quality, *recommended*. |
| [NemoMix-Unleashed-12B-Q5_K_S.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q5_K_S.gguf) | Q5_K_S | 8.52GB | false | High quality, *recommended*. |
| [NemoMix-Unleashed-12B-Q4_K_L.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q4_K_L.gguf) | Q4_K_L | 7.98GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [NemoMix-Unleashed-12B-Q4_K_M.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q4_K_M.gguf) | Q4_K_M | 7.48GB | false | Good quality, default size for must use cases, *recommended*. |
| [NemoMix-Unleashed-12B-Q3_K_XL.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q3_K_XL.gguf) | Q3_K_XL | 7.15GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [NemoMix-Unleashed-12B-Q4_K_S.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q4_K_S.gguf) | Q4_K_S | 7.12GB | false | Slightly lower quality with more space savings, *recommended*. |
| [NemoMix-Unleashed-12B-IQ4_XS.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-IQ4_XS.gguf) | IQ4_XS | 6.74GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [NemoMix-Unleashed-12B-Q3_K_L.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q3_K_L.gguf) | Q3_K_L | 6.56GB | false | Lower quality but usable, good for low RAM availability. |
| [NemoMix-Unleashed-12B-Q3_K_M.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q3_K_M.gguf) | Q3_K_M | 6.08GB | false | Low quality. |
| [NemoMix-Unleashed-12B-IQ3_M.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-IQ3_M.gguf) | IQ3_M | 5.72GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [NemoMix-Unleashed-12B-Q3_K_S.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q3_K_S.gguf) | Q3_K_S | 5.53GB | false | Low quality, not recommended. |
| [NemoMix-Unleashed-12B-Q2_K_L.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q2_K_L.gguf) | Q2_K_L | 5.45GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [NemoMix-Unleashed-12B-IQ3_XS.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-IQ3_XS.gguf) | IQ3_XS | 5.31GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [NemoMix-Unleashed-12B-Q2_K.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-Q2_K.gguf) | Q2_K | 4.79GB | false | Very low quality but surprisingly usable. |
| [NemoMix-Unleashed-12B-IQ2_M.gguf](https://huggingface.co/bartowski/NemoMix-Unleashed-12B-GGUF/blob/main/NemoMix-Unleashed-12B-IQ2_M.gguf) | IQ2_M | 4.44GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |

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
huggingface-cli download bartowski/NemoMix-Unleashed-12B-GGUF --include "NemoMix-Unleashed-12B-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/NemoMix-Unleashed-12B-GGUF --include "NemoMix-Unleashed-12B-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (NemoMix-Unleashed-12B-Q8_0) or download them all in place (./)

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


---
base_model: deepseek-ai/DeepSeek-V2-Lite
inference: false
library_name: gguf
pipeline_tag: text-generation
quantized_by: legraphista
tags:
- quantized
- GGUF
- imatrix
- quantization
- imat
- imatrix
- static
---

# DeepSeek-V2-Lite-IMat-GGUF
_Llama.cpp imatrix quantization of deepseek-ai/DeepSeek-V2-Lite_

Original Model: [deepseek-ai/DeepSeek-V2-Lite](https://huggingface.co/deepseek-ai/DeepSeek-V2-Lite)  
Original dtype: `BF16` (`bfloat16`)  
Quantized by: llama.cpp [https://github.com/ggerganov/llama.cpp/pull/7519](https://github.com/ggerganov/llama.cpp/releases/tag/https://github.com/ggerganov/llama.cpp/pull/7519)  
IMatrix dataset: [here](https://gist.githubusercontent.com/legraphista/d6d93f1a254bcfc58e0af3777eaec41e/raw/d380e7002cea4a51c33fffd47db851942754e7cc/imatrix.calibration.medium.raw)  

- [DeepSeek-V2-Lite-IMat-GGUF](#deepseek-v2-lite-imat-gguf)
    - [Files](#files)
        - [IMatrix](#imatrix)
        - [Common Quants](#common-quants)
        - [All Quants](#all-quants)
    - [Downloading using huggingface-cli](#downloading-using-huggingface-cli)
    - [Inference](#inference)
        - [Llama.cpp](#llama-cpp)
    - [FAQ](#faq)
        - [Why is the IMatrix not applied everywhere?](#why-is-the-imatrix-not-applied-everywhere)
        - [How do I merge a split GGUF?](#how-do-i-merge-a-split-gguf)

---

## Files

### IMatrix
Status: ✅ Available  
Link: [here](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/imatrix.dat) 

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [DeepSeek-V2-Lite.Q8_0.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q8_0.gguf) | Q8_0 | 16.70GB | ✅ Available | ⚪ No | 📦 No
| [DeepSeek-V2-Lite.Q6_K.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q6_K.gguf) | Q6_K | 14.07GB | ✅ Available | ⚪ No | 📦 No
| [DeepSeek-V2-Lite.Q4_K.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q4_K.gguf) | Q4_K | 10.36GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.Q3_K.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q3_K.gguf) | Q3_K | 8.13GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.Q2_K.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q2_K.gguf) | Q2_K | 6.43GB | ✅ Available | 🟢 Yes | 📦 No


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [DeepSeek-V2-Lite.FP16.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.FP16.gguf) | F16 | 31.42GB | ✅ Available | ⚪ No | 📦 No
| [DeepSeek-V2-Lite.BF16.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.BF16.gguf) | BF16 | 31.42GB | ✅ Available | ⚪ No | 📦 No
| [DeepSeek-V2-Lite.Q5_K.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q5_K.gguf) | Q5_K | 11.85GB | ✅ Available | ⚪ No | 📦 No
| [DeepSeek-V2-Lite.Q5_K_S.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q5_K_S.gguf) | Q5_K_S | 11.14GB | ✅ Available | ⚪ No | 📦 No
| [DeepSeek-V2-Lite.Q4_K_S.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q4_K_S.gguf) | Q4_K_S | 9.53GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.Q3_K_L.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q3_K_L.gguf) | Q3_K_L | 8.46GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.Q3_K_S.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q3_K_S.gguf) | Q3_K_S | 7.49GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.Q2_K_S.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.Q2_K_S.gguf) | Q2_K_S | 6.46GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ4_NL.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ4_NL.gguf) | IQ4_NL | 8.91GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ4_XS.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ4_XS.gguf) | IQ4_XS | 8.57GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ3_M.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ3_M.gguf) | IQ3_M | 7.55GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ3_S.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ3_S.gguf) | IQ3_S | 7.49GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ3_XS.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ3_XS.gguf) | IQ3_XS | 7.12GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ3_XXS.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ3_XXS.gguf) | IQ3_XXS | 6.96GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ2_M.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ2_M.gguf) | IQ2_M | 6.33GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ2_S.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ2_S.gguf) | IQ2_S | 6.01GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ2_XS.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ2_XS.gguf) | IQ2_XS | 5.97GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ2_XXS.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ2_XXS.gguf) | IQ2_XXS | 5.64GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ1_M.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ1_M.gguf) | IQ1_M | 5.24GB | ✅ Available | 🟢 Yes | 📦 No
| [DeepSeek-V2-Lite.IQ1_S.gguf](https://huggingface.co/legraphista/DeepSeek-V2-Lite-IMat-GGUF/blob/main/DeepSeek-V2-Lite.IQ1_S.gguf) | IQ1_S | 4.99GB | ✅ Available | 🟢 Yes | 📦 No


## Downloading using huggingface-cli
If you do not have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Download the specific file you want:
```
huggingface-cli download legraphista/DeepSeek-V2-Lite-IMat-GGUF --include "DeepSeek-V2-Lite.Q8_0.gguf" --local-dir ./
```
If the model file is big, it has been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/DeepSeek-V2-Lite-IMat-GGUF --include "DeepSeek-V2-Lite.Q8_0/*" --local-dir DeepSeek-V2-Lite.Q8_0
# see FAQ for merging GGUF's
```

---

## Inference

### Llama.cpp
```
llama.cpp/main -m DeepSeek-V2-Lite.Q8_0.gguf --color -i -p "prompt here"
```

---

## FAQ

### Why is the IMatrix not applied everywhere?
According to [this investigation](https://www.reddit.com/r/LocalLLaMA/comments/1993iro/ggufs_quants_can_punch_above_their_weights_now/), it appears that lower quantizations are the only ones that benefit from the imatrix input (as per hellaswag results). 

### How do I merge a split GGUF?
1. Make sure you have `gguf-split` available
    - To get hold of `gguf-split`, navigate to https://github.com/ggerganov/llama.cpp/releases
    - Download the appropriate zip for your system from the latest release
    - Unzip the archive and you should be able to find `gguf-split`
2. Locate your GGUF chunks folder (ex: `DeepSeek-V2-Lite.Q8_0`)
3. Run `gguf-split --merge DeepSeek-V2-Lite.Q8_0/DeepSeek-V2-Lite.Q8_0-00001-of-XXXXX.gguf DeepSeek-V2-Lite.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!
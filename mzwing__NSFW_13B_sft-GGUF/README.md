---
base_model: zxbsmk/NSFW_13B_sft
inference: false
license: apache-2.0
model_creator: zxbsmk
model_name: NSFW 13B sft
model_type: baichuan
prompt_template: >
  System: A chat between a curious human and an artificial intelligence
  assistant. The assistant gives helpful, detailed, and polite answers to the
  human's questions.

  Human: {prompt}

  Assistant:
quantized_by: mzwing
language:
- zh
tags:
- baichuan
- not-for-all-audiences
pipeline_tag: text-generation
datasets:
- zxbsmk/instruct_short_novel
---

# NSFW 13B sft - GGUF

- Model creator: [zxbsmk](https://huggingface.co/zxbsmk)
- Original model: [NSFW 13B sft](https://huggingface.co/zxbsmk/NSFW_13B_sft)

<!-- description start -->

## Description

This repo contains GGUF format model files for [zxbsmk's NSFW 13B sft](https://huggingface.co/zxbsmk/NSFW_13B_sft).

These files were quantised using hardware kindly provided by [Google Colab](https://colab.research.google.com/)(Free CPU Machine).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mzwing/AI-related/blob/master/notebooks/NSFW_13B_sft-GGUF.ipynb)

You can also check it out easily in [my GitHub  repo](https://github.com/mzwing/AI-related/blob/master/notebooks/NSFW_13B_sft-GGUF.ipynb).

<!-- description end -->

<!-- README_GGUF.md-about-gguf start -->

### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplate list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [Nitro](https://nitro.jan.ai/), a fast, lightweight 3mb inference server to supercharge apps with local AI, and OpenAI-compatible API server.

<!-- README_GGUF.md-about-gguf end -->

<!-- repositories-available start -->

## Repositories available

* [2, 3, 4, 5, 6, 8, 16 and 32-bit GGUF models for CPU+GPU inference](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF)
* [zxbsmk's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/zxbsmk/NSFW_13B_sft)

<!-- repositories-available end -->

<!-- prompt-template start -->

## Prompt template: BLING

```
System: A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.
Human: {prompt}
Assistant:

```

<!-- prompt-template end -->

<!-- compatibility_gguf start -->

## Compatibility

These quantised GGUFv2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

They are also compatible with many third party UIs and libraries - please see the list at the top of this README.

## Explanation of quantisation methods

<details>
  <summary>Click to see details</summary>

The new methods available are:

* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw

Refer to the Provided Files table below to see what files use which methods, and how.
</details>

<!-- compatibility_gguf end -->

<!-- README_GGUF.md-provided-files start -->

## Provided files

| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| [NSFW_13B_sft.Q2_K.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q2_K.gguf) | Q2_K | 2 | 5.56 GB | untested yet | smallest, significant quality loss - not recommended for most purposes |
| [NSFW_13B_sft.Q3_K_S.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q3_K_S.gguf) | Q3_K_S | 3 | 6.38 GB | untested yet | very small, high quality loss |
| [NSFW_13B_sft.Q3_K_M.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q3_K_M.gguf) | Q3_K_M | 3 | 6.85 GB | untested yet | very small, high quality loss |
| [NSFW_13B_sft.Q3_K_L.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q3_K_L.gguf) | Q3_K_L | 3 | 7.27 GB | untested yet | small, substantial quality loss |
| [NSFW_13B_sft.Q4_0.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q4_0.gguf) | Q4_0 | 4 | 7.55 GB | untested yet | legacy; small, very high quality loss - prefer using Q3_K_M |
| [NSFW_13B_sft.Q4_K_S.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q4_K_S.gguf) | Q4_K_S | 4 | 7.93 GB | untested yet | small, greater quality loss |
| [NSFW_13B_sft.Q4_K_M.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q4_K_M.gguf) | Q4_K_M | 4 | 8.56 GB | untested yet | medium, balanced quality - recommended |
| [NSFW_13B_sft.Q5_0.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q5_0.gguf) | Q5_0 | 5 | 9.17 GB | untested yet | legacy; medium, balanced quality - prefer using Q4_K_M |
| [NSFW_13B_sft.Q5_K_S.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q5_K_S.gguf) | Q5_K_S | 5 | 9.34 GB | untested yet | large, low quality loss - recommended |
| [NSFW_13B_sft.Q5_K_M.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q5_K_M.gguf) | Q5_K_M | 5 | 9.85 GB | untested yet | large, very low quality loss - recommended |
| [NSFW_13B_sft.Q6_K.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q6_K.gguf) | Q6_K | 6 | 11.6 GB | untested yet | very large, extremely low quality loss |
| [NSFW_13B_sft.Q8_0.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.Q8_0.gguf) | Q8_0 | 8 | 14.1 GB | untested yet | very large, extremely low quality loss - not recommended |
| [NSFW_13B_sft.F16.gguf](https://huggingface.co/mzwing/NSFW_13B_sft-GGUF/blob/main/NSFW_13B_sft.F16.gguf) | F16 | 16 | 26.5 GB | untested yet | extremely large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

<!-- README_GGUF.md-provided-files end -->

<!-- README_GGUF.md-how-to-download start -->

## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: `mzwing/NSFW_13B_sft-GGUF`, and below it, a specific filename to download, such as: `NSFW_13B_sft.Q4_K_M.gguf`.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download mzwing/NSFW_13B_sft-GGUF NSFW_13B_sft.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download mzwing/NSFW_13B_sft-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download mzwing/NSFW_13B_sft-GGUF NSFW_13B_sft.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m NSFW_13B_sft.Q4_K_M.gguf --color -c 2048 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "System: A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\nHuman: {prompt}\nAssistant:"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 2048` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions here: [text-generation-webui/docs/llama.cpp.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp.md).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries.

### How to load this model in Python code, using ctransformers

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base ctransformers with no GPU acceleration
pip install ctransformers
# Or with CUDA GPU acceleration
pip install ctransformers[cuda]
# Or with AMD ROCm GPU acceleration (Linux only)
CT_HIPBLAS=1 pip install ctransformers --no-binary ctransformers
# Or with Metal GPU acceleration for macOS systems only
CT_METAL=1 pip install ctransformers --no-binary ctransformers
```

#### Simple ctransformers example code

```python
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("mzwing/NSFW_13B_sft-GGUF", model_file="NSFW_13B_sft.Q4_K_M.gguf", model_type="phi", gpu_layers=50)

print(llm("AI is going to"))
```

## How to use with LangChain

Here are guides on using llama-cpp-python and ctransformers with LangChain:

* [LangChain + llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
* [LangChain + ctransformers](https://python.langchain.com/docs/integrations/providers/ctransformers)

<!-- README_GGUF.md-how-to-run end -->

<!-- footer start -->
<!-- 200823 -->
## Thanks, and how to contribute

Thanks to [Google Colab](https://colab.research.google.com/)! All the quantised models in this repo are done on the awesome platform. Thanks a lot!

Thanks to [llama.cpp](https://github.com/ggerganov/llama.cpp)! It inspired me to explore the inspiring AI field, thanks!

Thanks to [TheBloke](https://huggingface.co/TheBloke)! Everything in this repo is a reference to him.

You are welcome to create a **PullRequest**! Especially for the **RAM Usage**!

<!-- footer end -->

<!-- original-model-card start -->

A instruction-tuned model of https://huggingface.co/baichuan-inc/Baichuan-13B-Base

- Instruction-following datasets used: instruct_nsfw_cn
- Training framework: https://github.com/hiyouga/LLaMA-Efficient-Tuning

# Usage:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
tokenizer = AutoTokenizer.from_pretrained("zxbsmk/NSFW_13B_sft", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("zxbsmk/NSFW_13B_sft", trust_remote_code=True).cuda()
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
query = "续写。白洁已经动情了，肩带滑落露出香肩。"
inputs = tokenizer([query], return_tensors="pt")
inputs = inputs.to("cuda")
generate_ids = model.generate(**inputs, max_new_tokens=1024, streamer=streamer)
```

You could also alternatively launch a CLI demo by using the script in https://github.com/hiyouga/LLaMA-Efficient-Tuning

```bash
python src/cli_demo.py --template baichuan --model_name_or_path zxbsmk/NSFW_13B_sft
```

# Examples:
Omit part of results for better visualization.

| Question | NSFW_13B_sft | ChatGPT |
| -------- | ---------------- | ------- |
| 中国第三代战斗机的代表是什么？ | 中国第三代战斗机的代表是歼-10战斗机。 |截至我所掌握的信息（截止2021年9月），中国第三代战斗机的代表是中国航空工业集团公司（AVIC）生产的"歼-20"战斗机。该战斗机是中国第三代隐形战斗机，也被称为"歼-20风暴"，它是中国空军的先进战斗机，具备隐身特性、超音速巡航能力以及先进的雷达系统和电子设备。歼-20的研发和部署标志着中国在军事航空技术方面取得了重要进展。请注意，自那之后，可能已经有更多新型战斗机被研发或部署，因此建议查阅最新资料以获取更准确和最新的信息。|
| 解释这句话中每个词语的含义：今天下雨，我骑车差点摔倒，好在我一把把把把住了。 | 这句话中，“今天”指的是当前的时间，即雨天。“下雨”指的是天气阴沉，雨水落下。“我”指的是说话者，即骑车人。“骑车”指的是用自行车或其他交通工具出行。“差点”指的是几乎，几乎要摔倒。“摔倒”指的是身体失去平衡，摔在地上。“好在我”指的是幸亏有。“一把”指的是一下子。“把”指的是握住。“把住了”指的是握住车把，保持平衡。 | 今天：指代当天，即当前的日期。下雨：指天气现象，指雨水从天空降落。我：指说话人自己，第一人称代词。骑车：动词短语，表示骑着自行车。差点：几乎、险些，表示差一点就发生某种情况。摔倒：动词，意为因失去平衡而跌倒。好在：幸好、庆幸的意思，用来引出一个好的结果或意外。一把把把：这是一个错别字或打字错误，可能原本是“一把抓住”或类似的表达。考虑到语境，应该是指在骑车差点摔倒的情况下，通过抓住某物保住了平衡。抓住：动词短语，意为紧紧抓住某物，以保持稳定或防止掉落。综合起来，这句话的意思是：今天因为下雨，我骑车时差点摔倒，幸好我抓住了某物，避免了摔倒。 |
| 续写。白洁已经动情了，肩带滑落露出香肩。 | 白洁低下头，将秀发从肩头挽起，露出娇俏的耳垂，戴着个银制的耳钉，是叶子送给她的生日礼物，上面有个心型的装饰，是叶子亲手在心型装饰上刻上了白洁的名字。白洁没有穿胸罩，一对丰满的乳房随着她的动作轻轻颤动，滑落的肩带垂落在乳房上，更平添了一份诱惑... | 她静静地坐在窗边，微风轻拂着她的长发，将她的芳香散发到整个房间。白洁的心情久久不能平静，她的内心充满了对他的思念和渴望。她闭上眼睛，回想起他们之间的点点滴滴，那些温柔的瞬间在她的脑海中浮现... |
| 续写一下片段。王健已经忍耐不住了，一把搂住陆春兰，狠狠地揉捏她的巨乳。 | “嗯......王校长......轻点，哎呀......”陆春兰痛呼一声，连忙推开王健，一边赶紧拉开自己的上衣，露出雪白的胸脯，擦干乳房上的汗水，一边瞪了王健一眼，“都是你，弄得我这么黏糊糊的。”... | 很抱歉，但我无法为你提供所请求的续写。 |

# Evaluation
Comparision between Baichuan-13B-Chat and NSFW_13B_sft.
(Zero-shot [CMMLU](https://github.com/haonan-li/CMMLU))

| Score | NSFW_13B_sft | Baichuan-13B-Chat | ChatGPT |
| -------- | ---------------- | ------- |------- |
| STEM |            37.73 | 37.00 |**44.80** |
| Humanities |      **54.85** | 53.74 |53.61 |
| Social Sciences | **55.55** | 52.77 |54.22 |
| Other |           53.47 | 52.31 |**59.95** |
| China specific |  **51.84** | 50.55 |49.74 |
| Overall |         50.42 | 48.86 |**53.22** |

(By the way, Baichuan-13B-Chat gets 50.43 with one-shot which seems much better than 48.86 with zero-shot.)

# Contact Us
Join group via https://t.me/+JbovpBG6-gBiNDI1

<!-- original-model-card end -->
---
base_model: CausalLM/7B-DPO-alpha
datasets:
- JosephusCheung/GuanacoDataset
- Open-Orca/OpenOrca
- stingning/ultrachat
- meta-math/MetaMathQA
- liuhaotian/LLaVA-Instruct-150K
- jondurbin/airoboros-3.1
- WizardLM/WizardLM_evol_instruct_V2_196k
- RyokoAI/ShareGPT52K
- RyokoAI/Fandom23K
- milashkaarshif/MoeGirlPedia_wikitext_raw_archive
- wikipedia
- wiki_lingua
- fnlp/moss-003-sft-data
- garage-bAInd/Open-Platypus
- LDJnr/Puffin
- openbmb/llava_zh
- BAAI/COIG
- TigerResearch/tigerbot-zhihu-zh-10k
- liwu/MNBVC
- teknium/openhermes
inference: false
language:
- en
- zh
license: wtfpl
model_creator: CausalLM
model_name: CausalLM 7B-DPO-alpha
model_type: llama
pipeline_tag: text-generation
prompt_template: '<|im_start|>system

  {system_message}<|im_end|>

  <|im_start|>user

  {prompt}<|im_end|>

  <|im_start|>assistant

  '
quantized_by: tastypear
tags:
- llama
- llama2
- qwen
---
<!-- header start -->
I made a quantized version of this model by referring to TheBloke's publishing format and based on the recommendation of TheBloke/CausalLM-7B-GGUF.

我参考 TheBloke 的发布格式，并根据 TheBloke/CausalLM-7B-GGUF 的推荐，制作了这个模型的量化版本。

---

<!-- header end -->
<!-- markdownlint-disable MD041 -->

# CausalLM 7B-DPO-alpha - GGUF
- Model creator: [CausalLM](https://huggingface.co/CausalLM)
- Original model: [CausalLM 7B-DPO-alpha](https://huggingface.co/CausalLM/7B-DPO-alpha)

<!-- description start -->
## Description

This repo contains GGUF format model files for [CausalLM's CausalLM 7B-DPO-alpha](https://huggingface.co/CausalLM/7B-DPO-alpha).

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

<!-- README_GGUF.md-about-gguf end -->

<!-- prompt-template start -->
## Prompt template: ChatML

```
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant

```

<!-- prompt-template end -->
<!-- licensing start -->
## Licensing

The creator of the source model has listed its license as `wtfpl`, and this quantization has therefore used that same license.

As this model is based on Llama 2, it is also subject to the Meta Llama 2 license terms, and the license files for that are additionally included. It should therefore be considered as being claimed to be licensed under both licenses. I contacted Hugging Face for clarification on dual licensing but they do not yet have an official position. Should this change, or should Meta provide any feedback on this situation, I will update this section accordingly.

In the meantime, any questions regarding licensing, and in particular how these two licenses might interact, should be directed to the original model repository: [CausalLM's CausalLM 7B-DPO-alpha](https://huggingface.co/CausalLM/7B-DPO-alpha).
<!-- licensing end -->
<!-- compatibility_gguf start -->
## Compatibility

These quantised GGUFv2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

They are also compatible with many third party UIs and libraries - please see the list at the top of this README.

## Explanation of quantisation methods

<details>
  <summary>Click to see details</summary>

The new methods available are:

* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw

Refer to the Provided Files table below to see what files use which methods, and how.
</details>
<!-- compatibility_gguf end -->

<!-- README_GGUF.md-provided-files start -->
## Provided files

| Name | Quant method | Bits | Size |
| ---- | ---- | ---- | ---- |
| [causallm_7b.Q4_K_M.gguf](https://huggingface.co/tastypear/CausalLM-7B-DPO-alpha-GGUF/blob/main/causallm_7b-dpo-alpha.Q4_K_M.gguf) | Q4_K_M | 4 | 4.77 GB|
| [causallm_7b.Q5_K_S.gguf](https://huggingface.co/tastypear/CausalLM-7B-DPO-alpha-GGUF/blob/main/causallm_7b-dpo-alpha.Q5_K_S.gguf) | Q5_K_S | 5 | 5.40 GB|
| [causallm_7b.Q5_K_M.gguf](https://huggingface.co/tastypear/CausalLM-7B-DPO-alpha-GGUF/blob/main/causallm_7b-dpo-alpha.Q5_K_M.gguf) | Q5_K_M | 5 | 5.53 GB|

<!-- README_GGUF.md-provided-files end -->

<!-- footer start -->

<!-- original-model-card start -->
# Original model card: CausalLM's CausalLM 7B-DPO-alpha

For details, please refer to the version without DPO training: [CausalLM/7B](https://huggingface.co/CausalLM/7B).

| Model                     | MT-Bench     |
| ------------------------- | ------------ |
| GPT-4                     | 8.99         |
| GPT-3.5-Turbo             | 7.94         |
|                           |              |
| Zephyr-7b-β (Overfitting) | 7.34         |
| Zephyr-7b-α               | 6.88         |
|                           |              |
| **CausalLM/14B-DPO-α**    | **7.618868** |
| **CausalLM/7B-DPO-α**     | **7.038125** |

It should be noted that this is not a version that continues training on CausalLM/14B & 7B, but rather an optimized version that has undergone DPO training concurrently on a previous training branch, and some detailed parameters may have changed. You will still need to download the full model.

The beta branch will soon be released, employing some aggressive approaches that might be detrimental in certain tasks, in order to achieve better alignment with human preferences, aiming to meet or exceed the GPT-3.5 benchmarks. Stay tuned.

Disclaimer: Please note that the model was trained on unfiltered internet data. Since we do not have the capacity to vet all of it, there may be a substantial amount of objectionable content, pornography, violence, and offensive language present that we are unable to remove. Therefore, you will still need to complete your own checks on the model's safety and filter keywords in the output. Due to computational resource constraints, we are presently unable to implement RLHF for the model's ethics and safety, nor training on SFT samples that refuse to answer certain questions for restrictive fine-tuning.

更多详情，请参见未经DPO训练的版本：[CausalLM/14B](https://huggingface.co/CausalLM/14B)

需要注意的是，这并不是在 CausalLM/14B & 7B 上继续训练的版本，而是在之前的训练分支上同时进行了 DPO 训练的优化版本，一些细节参数可能发生了变化。 您仍然需要下载完整模型。

很快将会发布beta分支，采用了一些可能不利于某些任务的激进方法，以实现更好地符合人类偏好以接近和超过GPT-3.5基准。敬请期待。

免责声明：请注意，模型是在未经过滤的互联网数据上进行训练的。由于我们无法审核所有数据，可能会出现大量不良内容、色情、暴力和冒犯性语言，我们无法删除这些内容。因此，您仍然需要对模型的安全性进行自己的检查，并对输出中的关键词进行过滤。由于计算资源的限制，我们目前无法为模型的伦理和安全实施RLHF，也无法对拒绝回答某些问题的SFT样本进行训练以进行限制性微调。

<!-- original-model-card end -->

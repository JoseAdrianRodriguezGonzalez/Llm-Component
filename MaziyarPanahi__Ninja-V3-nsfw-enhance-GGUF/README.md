---
base_model: swdq/Ninja-V3-nsfw-enhance
inference: false
model_creator: swdq
model_name: Ninja-V3-nsfw-enhance-GGUF
pipeline_tag: text-generation
quantized_by: MaziyarPanahi
tags:
- quantized
- 2-bit
- 3-bit
- 4-bit
- 5-bit
- 6-bit
- 8-bit
- GGUF
- text-generation
---
# [MaziyarPanahi/Ninja-V3-nsfw-enhance-GGUF](https://huggingface.co/MaziyarPanahi/Ninja-V3-nsfw-enhance-GGUF)
- Model creator: [swdq](https://huggingface.co/swdq)
- Original model: [swdq/Ninja-V3-nsfw-enhance](https://huggingface.co/swdq/Ninja-V3-nsfw-enhance)

## Description
[MaziyarPanahi/Ninja-V3-nsfw-enhance-GGUF](https://huggingface.co/MaziyarPanahi/Ninja-V3-nsfw-enhance-GGUF) contains GGUF format model files for [swdq/Ninja-V3-nsfw-enhance](https://huggingface.co/swdq/Ninja-V3-nsfw-enhance).

### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration. Linux available, in beta as of 27/11/2023.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note, as of time of writing (November 27th 2023), ctransformers has not been updated in a long time and does not support many recent models.

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.
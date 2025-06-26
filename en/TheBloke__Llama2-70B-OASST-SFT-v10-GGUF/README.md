---
language:
- en
license: llama2
library_name: transformers
tags:
- sft
datasets:
- rombodawg/LosslessMegaCodeTrainingV2_1m_Evol_Uncensored
- OpenAssistant/oasst1
- shahules786/orca-best
- argilla/databricks-dolly-15k-curated-multilingual
model_name: Llama2 70B SFT v10
base_model: OpenAssistant/llama2-70b-oasst-sft-v10
inference: false
model_creator: OpenAssistant
model_type: llama
pipeline_tag: text-generation
prompt_template: '<|im_start|>system

  {system_message}<|im_end|>

  <|im_start|>user

  {prompt}<|im_end|>

  <|im_start|>assistant

  '
quantized_by: TheBloke
---

<!-- header start -->
<!-- 200823 -->
<div style="width: auto; margin-left: auto; margin-right: auto">
<img src="https://i.imgur.com/EBdldam.jpg" alt="TheBlokeAI" style="width: 100%; min-width: 400px; display: block; margin: auto;">
</div>
<div style="display: flex; justify-content: space-between; width: 100%;">
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://discord.gg/theblokeai">Chat & support: TheBloke's Discord server</a></p>
    </div>
    <div style="display: flex; flex-direction: column; align-items: flex-end;">
        <p style="margin-top: 0.5em; margin-bottom: 0em;"><a href="https://www.patreon.com/TheBlokeAI">Want to contribute? TheBloke's Patreon page</a></p>
    </div>
</div>
<div style="text-align:center; margin-top: 0em; margin-bottom: 0em"><p style="margin-top: 0.25em; margin-bottom: 0em;">TheBloke's LLM work is generously supported by a grant from <a href="https://a16z.com">andreessen horowitz (a16z)</a></p></div>
<hr style="margin-top: 1.0em; margin-bottom: 1.0em;">
<!-- header end -->

# Llama2 70B SFT v10 - GGUF
- Model creator: [OpenAssistant](https://huggingface.co/OpenAssistant)
- Original model: [Llama2 70B SFT v10](https://huggingface.co/OpenAssistant/llama2-70b-oasst-sft-v10)

<!-- description start -->
## Description

This repo contains GGUF format model files for [OpenAssistant's Llama2 70B SFT v10](https://huggingface.co/OpenAssistant/llama2-70b-oasst-sft-v10).

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp. GGUF offers numerous advantages over GGML, such as better tokenisation, and support for special tokens. It is also supports metadata, and is designed to be extensible.

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
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF)
* [OpenAssistant's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/OpenAssistant/llama2-70b-oasst-sft-v10)
<!-- repositories-available end -->

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


<!-- compatibility_gguf start -->
## Compatibility

These quantised GGUFv2 files are compatible with llama.cpp from August 27th onwards, as of commit [d0cee0d36d5be95a0d9088b674dbb27354107221](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221)

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
| [llama2-70b-oasst-sft-v10.Q2_K.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q2_K.gguf) | Q2_K | 2 | 29.28 GB| 31.78 GB | smallest, significant quality loss - not recommended for most purposes |
| [llama2-70b-oasst-sft-v10.Q3_K_S.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q3_K_S.gguf) | Q3_K_S | 3 | 29.92 GB| 32.42 GB | very small, high quality loss |
| [llama2-70b-oasst-sft-v10.Q3_K_M.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q3_K_M.gguf) | Q3_K_M | 3 | 33.19 GB| 35.69 GB | very small, high quality loss |
| [llama2-70b-oasst-sft-v10.Q3_K_L.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q3_K_L.gguf) | Q3_K_L | 3 | 36.15 GB| 38.65 GB | small, substantial quality loss |
| [llama2-70b-oasst-sft-v10.Q4_0.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q4_0.gguf) | Q4_0 | 4 | 38.87 GB| 41.37 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [llama2-70b-oasst-sft-v10.Q4_K_S.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q4_K_S.gguf) | Q4_K_S | 4 | 39.08 GB| 41.58 GB | small, greater quality loss |
| [llama2-70b-oasst-sft-v10.Q4_K_M.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q4_K_M.gguf) | Q4_K_M | 4 | 41.42 GB| 43.92 GB | medium, balanced quality - recommended |
| [llama2-70b-oasst-sft-v10.Q5_0.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q5_0.gguf) | Q5_0 | 5 | 47.46 GB| 49.96 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [llama2-70b-oasst-sft-v10.Q5_K_S.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q5_K_S.gguf) | Q5_K_S | 5 | 47.46 GB| 49.96 GB | large, low quality loss - recommended |
| [llama2-70b-oasst-sft-v10.Q5_K_M.gguf](https://huggingface.co/TheBloke/Llama2-70B-OASST-SFT-v10-GGUF/blob/main/llama2-70b-oasst-sft-v10.Q5_K_M.gguf) | Q5_K_M | 5 | 48.76 GB| 51.26 GB | large, very low quality loss - recommended |
| llama2-70b-oasst-sft-v10.Q6_K.gguf | Q6_K | 6 | 56.59 GB| 59.09 GB | very large, extremely low quality loss |
| llama2-70b-oasst-sft-v10.Q8_0.gguf | Q8_0 | 8 | 73.29 GB| 75.79 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

### Q6_K and Q8_0 files are split and require joining

**Note:** HF does not support uploading files larger than 50GB. Therefore I have uploaded the Q6_K and Q8_0 files as split files.

<details>
  <summary>Click for instructions regarding Q6_K and Q8_0 files</summary>
   
### q6_K 
Please download:
* `llama2-70b-oasst-sft-v10.Q6_K.gguf-split-a`
* `llama2-70b-oasst-sft-v10.Q6_K.gguf-split-b`

### q8_0
Please download:
* `llama2-70b-oasst-sft-v10.Q8_0.gguf-split-a`
* `llama2-70b-oasst-sft-v10.Q8_0.gguf-split-b`

To join the files, do the following:

Linux and macOS:
```
cat llama2-70b-oasst-sft-v10.Q6_K.gguf-split-* > llama2-70b-oasst-sft-v10.Q6_K.gguf && rm llama2-70b-oasst-sft-v10.Q6_K.gguf-split-*
cat llama2-70b-oasst-sft-v10.Q8_0.gguf-split-* > llama2-70b-oasst-sft-v10.Q8_0.gguf && rm llama2-70b-oasst-sft-v10.Q8_0.gguf-split-*
```
Windows command line:
```
COPY /B llama2-70b-oasst-sft-v10.Q6_K.gguf-split-a + llama2-70b-oasst-sft-v10.Q6_K.gguf-split-b llama2-70b-oasst-sft-v10.Q6_K.gguf
del llama2-70b-oasst-sft-v10.Q6_K.gguf-split-a llama2-70b-oasst-sft-v10.Q6_K.gguf-split-b

COPY /B llama2-70b-oasst-sft-v10.Q8_0.gguf-split-a + llama2-70b-oasst-sft-v10.Q8_0.gguf-split-b llama2-70b-oasst-sft-v10.Q8_0.gguf
del llama2-70b-oasst-sft-v10.Q8_0.gguf-split-a llama2-70b-oasst-sft-v10.Q8_0.gguf-split-b
```

</details>
<!-- README_GGUF.md-provided-files end -->

<!-- README_GGUF.md-how-to-download start -->
## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:
- LM Studio
- LoLLMS Web UI
- Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: TheBloke/Llama2-70B-OASST-SFT-v10-GGUF and below it, a specific filename to download, such as: llama2-70b-oasst-sft-v10.q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub>=0.17.1
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/Llama2-70B-OASST-SFT-v10-GGUF llama2-70b-oasst-sft-v10.q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/Llama2-70B-OASST-SFT-v10-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HUGGINGFACE_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/Llama2-70B-OASST-SFT-v10-GGUF llama2-70b-oasst-sft-v10.q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows CLI users: Use `set HUGGINGFACE_HUB_ENABLE_HF_TRANSFER=1` before running the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d36d5be95a0d9088b674dbb27354107221](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 32 -m llama2-70b-oasst-sft-v10.q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<|im_start|>system\n{system_message}<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 4096` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions here: [text-generation-webui/docs/llama.cpp.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/llama.cpp.md).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries.

### How to load this model from Python using ctransformers

#### First install the package

```bash
# Base ctransformers with no GPU acceleration
pip install ctransformers>=0.2.24
# Or with CUDA GPU acceleration
pip install ctransformers[cuda]>=0.2.24
# Or with ROCm GPU acceleration
CT_HIPBLAS=1 pip install ctransformers>=0.2.24 --no-binary ctransformers
# Or with Metal GPU acceleration for macOS systems
CT_METAL=1 pip install ctransformers>=0.2.24 --no-binary ctransformers
```

#### Simple example code to load one of these GGUF models

```python
from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama2-70B-OASST-SFT-v10-GGUF", model_file="llama2-70b-oasst-sft-v10.q4_K_M.gguf", model_type="llama", gpu_layers=50)

print(llm("AI is going to"))
```

## How to use with LangChain

Here's guides on using llama-cpp-python or ctransformers with LangChain:

* [LangChain + llama-cpp-python](https://python.langchain.com/docs/integrations/llms/llamacpp)
* [LangChain + ctransformers](https://python.langchain.com/docs/integrations/providers/ctransformers)

<!-- README_GGUF.md-how-to-run end -->

<!-- footer start -->
<!-- 200823 -->
## Discord

For further support, and discussions on these models and AI in general, join us at:

[TheBloke AI's Discord server](https://discord.gg/theblokeai)

## Thanks, and how to contribute

Thanks to the [chirper.ai](https://chirper.ai) team!

Thanks to Clay from [gpus.llm-utils.org](llm-utils)!

I've had a lot of people ask if they can contribute. I enjoy providing models and helping people, and would love to be able to spend even more time doing it, as well as expanding into new projects like fine tuning/training.

If you're able and willing to contribute it will be most gratefully received and will help me to keep providing more models, and to start work on new AI projects.

Donaters will get priority support on any and all AI/LLM/model questions and requests, access to a private Discord room, plus other benefits.

* Patreon: https://patreon.com/TheBlokeAI
* Ko-Fi: https://ko-fi.com/TheBlokeAI

**Special thanks to**: Aemon Algiz.

**Patreon special mentions**: Alicia Loh, Stephen Murray, K, Ajan Kanaga, RoA, Magnesian, Deo Leter, Olakabola, Eugene Pentland, zynix, Deep Realms, Raymond Fosdick, Elijah Stavena, Iucharbius, Erik Bjäreholt, Luis Javier Navarrete Lozano, Nicholas, theTransient, John Detwiler, alfie_i, knownsqashed, Mano Prime, Willem Michiel, Enrico Ros, LangChain4j, OG, Michael Dempsey, Pierre Kircher, Pedro Madruga, James Bentley, Thomas Belote, Luke @flexchar, Leonard Tan, Johann-Peter Hartmann, Illia Dulskyi, Fen Risland, Chadd, S_X, Jeff Scroggin, Ken Nordquist, Sean Connelly, Artur Olbinski, Swaroop Kallakuri, Jack West, Ai Maven, David Ziegler, Russ Johnson, transmissions 11, John Villwock, Alps Aficionado, Clay Pascal, Viktor Bowallius, Subspace Studios, Rainer Wilmers, Trenton Dambrowitz, vamX, Michael Levine, 준교 김, Brandon Frisco, Kalila, Trailburnt, Randy H, Talal Aujan, Nathan Dryer, Vadim, 阿明, ReadyPlayerEmma, Tiffany J. Kim, George Stoitzev, Spencer Kim, Jerry Meng, Gabriel Tamborski, Cory Kujawski, Jeffrey Morgan, Spiking Neurons AB, Edmond Seymore, Alexandros Triantafyllidis, Lone Striker, Cap'n Zoog, Nikolai Manek, danny, ya boyyy, Derek Yates, usrbinkat, Mandus, TL, Nathan LeClaire, subjectnull, Imad Khwaja, webtim, Raven Klaugh, Asp the Wyvern, Gabriel Puliatti, Caitlyn Gatomon, Joseph William Delisle, Jonathan Leane, Luke Pendergrass, SuperWojo, Sebastain Graf, Will Dee, Fred von Graf, Andrey, Dan Guido, Daniel P. Andersen, Nitin Borwankar, Elle, Vitor Caleffi, biorpg, jjj, NimbleBox.ai, Pieter, Matthew Berman, terasurfer, Michael Davis, Alex, Stanislav Ovsiannikov


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: OpenAssistant's Llama2 70B SFT v10

# Open-Assistant Llama2 70B SFT v10

This model is an Open-Assistant fine-tuning of Meta's [Llama2 70B](https://huggingface.co/meta-llama/Llama-2-70b) LLM.
It was fine-tuned in two stages, first on a mix of synthetic instrunctions and coding tasks and then in a "polishing" stage
on the best human demonstrations collected at [open-assistant.io](https://open-assistant.io/) up to July 23, 2023 (see [Configuration Details](#configuration-details) below).

## Model Details

- **Finetuned from:** [meta-llama/Llama-2-70b](https://huggingface.co/meta-llama/Llama-2-70b) via [epfLLM/Megatron-LLM](https://github.com/epfLLM/Megatron-LLM)
- **Model type:** Causal decoder-only transformer language model
- **Language:** English (and limited capabilities in German, Spanish, French, Italian, Portuguese, Polish, Dutch, Romanian, Czech, Swedish)
- **Weights & Biases training logs:** [Stage 1](https://wandb.ai/open-assistant/public-sft/runs/run45_oasst_pre10_llama2_70b) (1 epoch pretrain-mix, 12k steps), [Stage 2](https://wandb.ai/open-assistant/public-sft/runs/run46_oasst_sft10_llama2_70b) (3 epochs oasst top-1, 519 steps)
- **Demo:** [Continuations for 250 random prompts (TGI, 4bit nf4 quantization)](https://open-assistant.github.io/oasst-model-eval/?f=https%3A%2F%2Fraw.githubusercontent.com%2FOpen-Assistant%2Foasst-model-eval%2Fmain%2Fsampling_reports%2Foasst-sft%2F2023-08-22_OpenAssistant_llama2-70b-oasst-sft-v10_sampling_noprefix2_nf4.json%0A)
- **Evaluation** [FastEval-OpenAssistant Overview](https://tju01.github.io/FastEval-OpenAssistant/) (using [FastEval](https://github.com/FastEval/FastEval) & [vLLM](https://github.com/vllm-project/vllm))
- **License:** [LLAMA 2 COMMUNITY LICENSE AGREEMENT](https://huggingface.co/meta-llama/Llama-2-70b/raw/main/LICENSE.txt)
- **Contact:** [Open-Assistant Discord](https://ykilcher.com/open-assistant-discord)


## Prompting / Prompt Template

Due to public demand (see [survey](https://twitter.com/erhartford/status/1682403597525430272)) we changed the prompt-template for this model from custom prompter/assistant tokens to OpenAI's [chatml](https://github.com/openai/openai-python/blob/main/chatml.md) standard prompt format.
We hope that this leads to greater compatibility with chat inference/frontend applications.

Prompt dialogue template:

```
"""
<|im_start|>system
{system_message}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
"""
```

The model input can contain multiple conversation turns between user and assistant, e.g.
```
<|im_start|>user
{prompt 1}<|im_end|>
<|im_start|>assistant
{reply 1}<|im_end|>
<|im_start|>user
{prompt 2}<|im_end|>
<|im_start|>assistant
(...)
```

The model was partly trained with orca system messages.
For inference we recommend to use the official [Llama2 system message](https://github.com/facebookresearch/llama/blob/ea9f33d6d3ea8ed7d560d270986407fd6c2e52b7/example_chat_completion.py#L57-L61):
```
<|im_start|>system
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<|im_end|>
```

### Credits & Special Thanks

- Thanks to [Meta AI](https://ai.meta.com/) for training and releasing the Llama2 model.
- Distributed training support was provided by EPFL's [Machine Learning and Optimization Laboratory](https://www.epfl.ch/labs/mlo/), and [Natural Language Processing Lab](https://nlp.epfl.ch/).
- The open-source [epfLLM/Megatron-LLM](https://github.com/epfLLM/Megatron-LLM) trainer was used for fine-tuning.
- [rombodawg](https://huggingface.co/rombodawg) curated the [LosslessMegaCodeTrainingV2_1m_Evol_Uncensored](https://huggingface.co/datasets/rombodawg/LosslessMegaCodeTrainingV2_1m_Evol_Uncensored) dataset.
- [ehartford](https://huggingface.co/ehartford) generated and published the [ehartford/dolphin](https://huggingface.co/datasets/ehartford/dolphin) and the [ehartford/oa_leet10k](https://huggingface.co/datasets/ehartford/oa_leet10k) datasets.
- [Argilla](https://huggingface.co/argilla) curated and published the [argilla/databricks-dolly-15k-curated-multilingual](https://huggingface.co/datasets/argilla/databricks-dolly-15k-curated-multilingual) dataset.
- [shahules786](https://github.com/shahules786) de-duped and filtered the Dolphin dataset with a cluster-center approach and generated the orca-best (ocra-chat) dataset.
- [andreaskoepf](https://github.com/andreaskoepf/) prepared & orchestrated the training.

We want to especially thank everyone who contributed in the crowed-sourced Open-Assistant dataset creation on https://open-assistant.io/ - without you this project would not have been possible.

## Ethical Considerations and Limitations

Testing conducted to date has been in English, and has not covered, nor could it cover all scenarios.
For these reasons, as with all LLMs, the potential outputs of llama2-70b-oasst-sft-v10 cannot be predicted
in advance, and the model may in some instances produce inaccurate, biased or other objectionable responses
to user prompts. Therefore, before deploying any applications of llama2-70b-oasst-sft-v10, developers should
perform safety testing and tuning tailored to their specific applications of the model.

Please see Meta's [Responsible Use Guide](https://ai.meta.com/llama/responsible-use-guide/).

## Note regarding inference with TGI

During evaluation we noticed that this 70B model produced extremely poor outputs when loaded it was loaded in 16 bit precision sharded in [TGI](https://github.com/huggingface/text-generation-inference).
In contrast the model could be evaluated without problem using [vLLM](https://github.com/vllm-project/vllm).
The model also worked decently well when loaded with TGI on a single GPPU nf4 quantized via [TimDettmers/bitsandbytes](https://github.com/TimDettmers/bitsandbytes).
Will will get it touch with the TGI authors to find out why sharded 16-bit inference doesn't work as expected.

## Configuration Details

The "pretokenizer" utility used to tokenize the datamix is part of the Open-Assistant github repository and can be found here: [model/pretokenizer](https://github.com/LAION-AI/Open-Assistant/tree/main/model/pretokenizer).


### Stage 1 Pretokenizer Configuration

Entries of the dataset with assistant replies shorter than 25 tokens were excluded from training.

```
oasst_pre10_min25:
  datasets:
    - megacode2:
        fraction: 0.5
        val_split: 0.01
        max_val_set: 1000
    - orca-chat:
        val_split: 0.01
        max_val_set: 1000
    - dolly15k_multilingual:
        val_split: 0.05
        max_val_set: 300
    - oa_leet10k:
        val_split: 0.05
        max_val_set: 250
  output_dir: "output/oasst_pre10_min25"
  filename_prefix: "oasst_pre10"
  min_assistant_tokens: 25
```

Stage 1 dataset statistics:
```
# Stats for output/oasst_pre10_min25_llama2

## Stats for 'Subset of InstructionDataset (megacode2)' (466364 samples (50.0%))
-----------------
  Accepted: 398223/466364 (85.4%)
  Accepted tokens: 167676873
  Skipped: 68141 (14.6%)
  Min tokens per sample: 36
  Max tokens per sample: 11810
  Avg tokens per sample: 421.063
-----------------

## Stats for 'Subset of OrcaChat (orca-chat)' (325616 samples (100.0%))
-----------------
  Accepted: 325616/325616 (100.0%)
  Accepted tokens: 178307574
  Skipped: 0 (0.0%)
  Min tokens per sample: 105
  Max tokens per sample: 10408
  Avg tokens per sample: 547.601
-----------------

## Stats for 'Subset of Dolly15kMultilingual' (57020 samples (100.0%))
-----------------
  Accepted: 47494/57020 (83.3%)
  Accepted tokens: 13883177
  Skipped: 9526 (16.7%)
  Min tokens per sample: 34
  Max tokens per sample: 9172
  Avg tokens per sample: 292.314
-----------------

## Stats for 'Subset of InstructionDataset (oa_leet10k)' (22236 samples (100.0%))
-----------------
  Accepted: 22236/22236 (100.0%)
  Accepted tokens: 15905296
  Skipped: 0 (0.0%)
  Min tokens per sample: 168
  Max tokens per sample: 10588
  Avg tokens per sample: 715.295
-----------------

## Stats for 'total' (871236 samples (100.0%))
-----------------
  Accepted: 793569/871236 (91.1%)
  Accepted tokens: 375772920
  Skipped: 77667 (8.9%)
  Min tokens per sample: 34
  Max tokens per sample: 11810
  Avg tokens per sample: 473.523
-----------------
```


### Stage 2 Pretokenizer Configuration

```
oasst_top1:
  datasets:
    - oasst_export:
        lang: "bg,ca,cs,da,de,en,es,fr,hr,hu,it,nl,pl,pt,ro,ru,sl,sr,sv,uk"
        input_file_path: 2023-07-23_oasst_ready.tar.gz
        top_k: 1
        val_split: 0.05
  output_dir: "output/oasst_top1_2023-07-23"
  filename_prefix: "oasst_top1"
```

Stage 2 dataset statistics:

```
# Stats for output/oasst_top1_2023-07-23_llama2

## Stats for 'ListDataset' (11441 samples (100.0%))
-----------------
  Accepted: 11441/11441 (100.0%)
  Accepted tokens: 5315368
  Skipped: 0 (0.0%)
  Min tokens per sample: 20
  Max tokens per sample: 5407
  Avg tokens per sample: 464.58945896337735
-----------------

## Stats for 'total' (11441 samples (100.0%))
-----------------
  Accepted: 11441/11441 (100.0%)
  Accepted tokens: 5315368
  Skipped: 0 (0.0%)
  Min tokens per sample: 20
  Max tokens per sample: 5407
  Avg tokens per sample: 464.58945896337735
-----------------
```


### Megatron Fine-Tuning Arguments for Stage 1 (Instruction Tuning):
```
--tensor_model_parallel_size 8
--pipeline_model_parallel_size 4
--load ./checkpoints/llama2-70b-tp8-pp4
--save ./checkpoints/llama2-70b-tp8-pp4-oasst_pre10
--tensorboard_dir ./checkpoints/llama2-70b-tp8-pp4-oasst_pre10/logging
--data_path ./data/oasst_pre10_min25_llama2/oasst_sft10-train
--model_name llama2
--tokenizer_type SentencePieceTokenizer
--bf16
--global_batch_size 64
--micro_batch_size 2
--vocab_file=./llama2/Llama-2-7b/tokenizer.model
--use_rms_norm
--glu_activation swiglu
--no_tie_embed_logits
--vocab_extra_ids_list "\"<|im_start|>,<|im_end|>\""
--layernorm_epsilon 1e-5
--use_flash_attn
--no_bias_gelu_fusion
--seq_length 4096
--max_position_embeddings 4096
--log_interval 1
--save_interval 500
--eval_interval 50
--eval_iters 10
--hidden_dropout 0.0
--position_embedding_type rotary
--no_bias_dropout_fusion
--use_checkpoint_args
--train_iters 12000
--attention_dropout 0.0
--adam_beta1 0.9
--adam_beta2 0.95
--adam_eps 1e-12
--lr_decay_style cosine
--lr_warmup_iters 100
--lr 1e-5
--min_lr 1e-6
--weight_decay 0.000001
--sequence_parallel
--recompute_granularity selective
--log_timers_to_tensorboard
--rope_scaling_factor 1.0
--wandb_logger
```

### Megatron Fine-Tuning Arguments for Stage 2 (OASST Polishing, LIMA Dropout):
```
--tensor_model_parallel_size 8
--pipeline_model_parallel_size 4
--load ./checkpoints/llama2-70b-tp8-pp4-oasst_pre10
--save ./checkpoints/llama2-70b-tp8-pp4-oasst_sft10
--tensorboard_dir ./checkpoints/llama2-70b-tp8-pp4-oasst_sft10/logging
--data_path ./data/oasst_top1_2023-07-23_llama2/oasst_top1-train
--model_name llama2
--tokenizer_type SentencePieceTokenizer
--bf16
--global_batch_size 64
--micro_batch_size 2
--vocab_file=./llama2/Llama-2-7b/tokenizer.model
--use_rms_norm
--glu_activation swiglu
--no_tie_embed_logits
--vocab_extra_ids_list "\"<|im_start|>,<|im_end|>\""
--layernorm_epsilon 1e-5
--use_flash_attn
--no_bias_gelu_fusion
--seq_length 4096
--max_position_embeddings 4096
--log_interval 1
--save_interval 346
--eval_interval 50
--eval_iters 10
--hidden_dropout 0.25
--lima_dropout
--position_embedding_type rotary
--no_bias_dropout_fusion
--use_checkpoint_args
--train_iters 519
--attention_dropout 0.0
--adam_beta1 0.9
--adam_beta2 0.95
--adam_eps 1e-12
--lr_decay_style cosine
--lr_warmup_iters 100
--lr 1e-5
--min_lr 1e-6
--weight_decay 0.000001
--sequence_parallel
--recompute_granularity selective
--log_timers_to_tensorboard
--rope_scaling_factor 1.0
--finetune
--wandb_logger
```

<!-- original-model-card end -->

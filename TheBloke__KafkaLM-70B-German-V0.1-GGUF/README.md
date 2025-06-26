---
base_model: seedboxai/KafkaLM-70B-German-V0.1
datasets:
- seedboxai/multitask_german_examples_32k
inference: false
language:
- de
library_name: transformers
license: llama2
model_creator: Seedbox
model_name: KafkaLM 70B German V0.1
model_type: llama
pipeline_tag: text-generation
prompt_template: '<|system|>

  {system_message}</s>

  <|user|>

  {prompt}</s>

  <|assistant|>

  '
quantized_by: TheBloke
tags:
- llama2
- deutsch
- german
- seedbox
---
<!-- markdownlint-disable MD041 -->

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

# KafkaLM 70B German V0.1 - GGUF
- Model creator: [Seedbox](https://huggingface.co/seedboxai)
- Original model: [KafkaLM 70B German V0.1](https://huggingface.co/seedboxai/KafkaLM-70B-German-V0.1)

<!-- description start -->
## Description

This repo contains GGUF format model files for [Seedbox's KafkaLM 70B German V0.1](https://huggingface.co/seedboxai/KafkaLM-70B-German-V0.1).

These files were quantised using hardware kindly provided by [Massed Compute](https://massedcompute.com/).

<!-- description end -->
<!-- README_GGUF.md-about-gguf start -->
### About GGUF

GGUF is a new format introduced by the llama.cpp team on August 21st 2023. It is a replacement for GGML, which is no longer supported by llama.cpp.

Here is an incomplete list of clients and libraries that are known to support GGUF:

* [llama.cpp](https://github.com/ggerganov/llama.cpp). The source project for GGUF. Offers a CLI and a server option.
* [text-generation-webui](https://github.com/oobabooga/text-generation-webui), the most widely used web UI, with many features and powerful extensions. Supports GPU acceleration.
* [KoboldCpp](https://github.com/LostRuins/koboldcpp), a fully featured web UI, with GPU accel across all platforms and GPU architectures. Especially good for story telling.
* [GPT4All](https://gpt4all.io/index.html), a free and open source local running GUI, supporting Windows, Linux and macOS with full GPU accel.
* [LM Studio](https://lmstudio.ai/), an easy-to-use and powerful local GUI for Windows and macOS (Silicon), with GPU acceleration. Linux available, in beta as of 27/11/2023.
* [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), a great web UI with many interesting and unique features, including a full model library for easy model selection.
* [Faraday.dev](https://faraday.dev/), an attractive and easy to use character-based chat GUI for Windows and macOS (both Silicon and Intel), with GPU acceleration.
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), a Python library with GPU accel, LangChain support, and OpenAI-compatible API server.
* [candle](https://github.com/huggingface/candle), a Rust ML framework with a focus on performance, including GPU support, and ease of use.
* [ctransformers](https://github.com/marella/ctransformers), a Python library with GPU accel, LangChain support, and OpenAI-compatible AI server. Note, as of time of writing (November 27th 2023), ctransformers has not been updated in a long time and does not support many recent models.

<!-- README_GGUF.md-about-gguf end -->
<!-- repositories-available start -->
## Repositories available

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF)
* [Seedbox's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/seedboxai/KafkaLM-70B-German-V0.1)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: Zephyr

```
<|system|>
{system_message}</s>
<|user|>
{prompt}</s>
<|assistant|>

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
| [kafkalm-70b-german-v0.1.Q2_K.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q2_K.gguf) | Q2_K | 2 | 25.46 GB| 27.96 GB | significant quality loss - not recommended for most purposes |
| [kafkalm-70b-german-v0.1.Q3_K_S.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q3_K_S.gguf) | Q3_K_S | 3 | 29.92 GB| 32.42 GB | very small, high quality loss |
| [kafkalm-70b-german-v0.1.Q3_K_M.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q3_K_M.gguf) | Q3_K_M | 3 | 33.27 GB| 35.77 GB | very small, high quality loss |
| [kafkalm-70b-german-v0.1.Q3_K_L.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q3_K_L.gguf) | Q3_K_L | 3 | 36.15 GB| 38.65 GB | small, substantial quality loss |
| [kafkalm-70b-german-v0.1.Q4_0.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q4_0.gguf) | Q4_0 | 4 | 38.87 GB| 41.37 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [kafkalm-70b-german-v0.1.Q4_K_S.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q4_K_S.gguf) | Q4_K_S | 4 | 39.25 GB| 41.75 GB | small, greater quality loss |
| [kafkalm-70b-german-v0.1.Q4_K_M.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q4_K_M.gguf) | Q4_K_M | 4 | 41.42 GB| 43.92 GB | medium, balanced quality - recommended |
| [kafkalm-70b-german-v0.1.Q5_0.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q5_0.gguf) | Q5_0 | 5 | 47.46 GB| 49.96 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [kafkalm-70b-german-v0.1.Q5_K_S.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q5_K_S.gguf) | Q5_K_S | 5 | 47.46 GB| 49.96 GB | large, low quality loss - recommended |
| [kafkalm-70b-german-v0.1.Q5_K_M.gguf](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF/blob/main/kafkalm-70b-german-v0.1.Q5_K_M.gguf) | Q5_K_M | 5 | 48.75 GB| 51.25 GB | large, very low quality loss - recommended |
| kafkalm-70b-german-v0.1.Q6_K.gguf | Q6_K | 6 | 56.59 GB| 59.09 GB | very large, extremely low quality loss |
| kafkalm-70b-german-v0.1.Q8_0.gguf | Q8_0 | 8 | 73.29 GB| 75.79 GB | very large, extremely low quality loss - not recommended |

**Note**: the above RAM figures assume no GPU offloading. If layers are offloaded to the GPU, this will reduce RAM usage and use VRAM instead.

### Q6_K and Q8_0 files are split and require joining

**Note:** HF does not support uploading files larger than 50GB. Therefore I have uploaded the Q6_K and Q8_0 files as split files.

<details>
  <summary>Click for instructions regarding Q6_K and Q8_0 files</summary>
   
### q6_K 
Please download:
* `kafkalm-70b-german-v0.1.Q6_K.gguf-split-a`
* `kafkalm-70b-german-v0.1.Q6_K.gguf-split-b`

### q8_0
Please download:
* `kafkalm-70b-german-v0.1.Q8_0.gguf-split-a`
* `kafkalm-70b-german-v0.1.Q8_0.gguf-split-b`

To join the files, do the following:

Linux and macOS:
```
cat kafkalm-70b-german-v0.1.Q6_K.gguf-split-* > kafkalm-70b-german-v0.1.Q6_K.gguf && rm kafkalm-70b-german-v0.1.Q6_K.gguf-split-*
cat kafkalm-70b-german-v0.1.Q8_0.gguf-split-* > kafkalm-70b-german-v0.1.Q8_0.gguf && rm kafkalm-70b-german-v0.1.Q8_0.gguf-split-*
```
Windows command line:
```
COPY /B kafkalm-70b-german-v0.1.Q6_K.gguf-split-a + kafkalm-70b-german-v0.1.Q6_K.gguf-split-b kafkalm-70b-german-v0.1.Q6_K.gguf
del kafkalm-70b-german-v0.1.Q6_K.gguf-split-a kafkalm-70b-german-v0.1.Q6_K.gguf-split-b

COPY /B kafkalm-70b-german-v0.1.Q8_0.gguf-split-a + kafkalm-70b-german-v0.1.Q8_0.gguf-split-b kafkalm-70b-german-v0.1.Q8_0.gguf
del kafkalm-70b-german-v0.1.Q8_0.gguf-split-a kafkalm-70b-german-v0.1.Q8_0.gguf-split-b
```

</details>
<!-- README_GGUF.md-provided-files end -->

<!-- README_GGUF.md-how-to-download start -->
## How to download GGUF files

**Note for manual downloaders:** You almost never want to clone the entire repo! Multiple different quantisation formats are provided, and most users only want to pick and download a single file.

The following clients/libraries will automatically download models for you, providing a list of available models to choose from:

* LM Studio
* LoLLMS Web UI
* Faraday.dev

### In `text-generation-webui`

Under Download Model, you can enter the model repo: TheBloke/KafkaLM-70B-German-V0.1-GGUF and below it, a specific filename to download, such as: kafkalm-70b-german-v0.1.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/KafkaLM-70B-German-V0.1-GGUF kafkalm-70b-german-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/KafkaLM-70B-German-V0.1-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/KafkaLM-70B-German-V0.1-GGUF kafkalm-70b-german-v0.1.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m kafkalm-70b-german-v0.1.Q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "<|system|>\n{system_message}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>"
```

Change `-ngl 32` to the number of layers to offload to GPU. Remove it if you don't have GPU acceleration.

Change `-c 4096` to the desired sequence length. For extended sequence models - eg 8K, 16K, 32K - the necessary RoPE scaling parameters are read from the GGUF file and set by llama.cpp automatically. Note that longer sequence lengths require much more resources, so you may need to reduce this value.

If you want to have a chat-style conversation, replace the `-p <PROMPT>` argument with `-i -ins`

For other parameters and how to use them, please refer to [the llama.cpp documentation](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

## How to run in `text-generation-webui`

Further instructions can be found in the text-generation-webui documentation, here: [text-generation-webui/docs/04 ‐ Model Tab.md](https://github.com/oobabooga/text-generation-webui/blob/main/docs/04%20%E2%80%90%20Model%20Tab.md#llamacpp).

## How to run from Python code

You can use GGUF models from Python using the [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) or [ctransformers](https://github.com/marella/ctransformers) libraries. Note that at the time of writing (Nov 27th 2023), ctransformers has not been updated for some time and is not compatible with some recent models. Therefore I recommend you use llama-cpp-python.

### How to load this model in Python code, using llama-cpp-python

For full documentation, please see: [llama-cpp-python docs](https://abetlen.github.io/llama-cpp-python/).

#### First install the package

Run one of the following commands, according to your system:

```shell
# Base ctransformers with no GPU acceleration
pip install llama-cpp-python
# With NVidia CUDA acceleration
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
# Or with OpenBLAS acceleration
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
# Or with CLBLast acceleration
CMAKE_ARGS="-DLLAMA_CLBLAST=on" pip install llama-cpp-python
# Or with AMD ROCm GPU acceleration (Linux only)
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
# Or with Metal GPU acceleration for macOS systems only
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

# In windows, to set the variables CMAKE_ARGS in PowerShell, follow this format; eg for NVidia CUDA:
$env:CMAKE_ARGS = "-DLLAMA_OPENBLAS=on"
pip install llama-cpp-python
```

#### Simple llama-cpp-python example code

```python
from llama_cpp import Llama

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = Llama(
  model_path="./kafkalm-70b-german-v0.1.Q4_K_M.gguf",  # Download the model file first
  n_ctx=4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  "<|system|>\n{system_message}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)

# Chat Completion API

llm = Llama(model_path="./kafkalm-70b-german-v0.1.Q4_K_M.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
llm.create_chat_completion(
    messages = [
        {"role": "system", "content": "You are a story writing assistant."},
        {
            "role": "user",
            "content": "Write a story about llamas."
        }
    ]
)
```

## How to use with LangChain

Here are guides on using llama-cpp-python and ctransformers with LangChain:

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

**Patreon special mentions**: Michael Levine, 阿明, Trailburnt, Nikolai Manek, John Detwiler, Randy H, Will Dee, Sebastain Graf, NimbleBox.ai, Eugene Pentland, Emad Mostaque, Ai Maven, Jim Angel, Jeff Scroggin, Michael Davis, Manuel Alberto Morcote, Stephen Murray, Robert, Justin Joy, Luke @flexchar, Brandon Frisco, Elijah Stavena, S_X, Dan Guido, Undi ., Komninos Chatzipapas, Shadi, theTransient, Lone Striker, Raven Klaugh, jjj, Cap'n Zoog, Michel-Marie MAUDET (LINAGORA), Matthew Berman, David, Fen Risland, Omer Bin Jawed, Luke Pendergrass, Kalila, OG, Erik Bjäreholt, Rooh Singh, Joseph William Delisle, Dan Lewis, TL, John Villwock, AzureBlack, Brad, Pedro Madruga, Caitlyn Gatomon, K, jinyuan sun, Mano Prime, Alex, Jeffrey Morgan, Alicia Loh, Illia Dulskyi, Chadd, transmissions 11, fincy, Rainer Wilmers, ReadyPlayerEmma, knownsqashed, Mandus, biorpg, Deo Leter, Brandon Phillips, SuperWojo, Sean Connelly, Iucharbius, Jack West, Harry Royden McLaughlin, Nicholas, terasurfer, Vitor Caleffi, Duane Dunston, Johann-Peter Hartmann, David Ziegler, Olakabola, Ken Nordquist, Trenton Dambrowitz, Tom X Nguyen, Vadim, Ajan Kanaga, Leonard Tan, Clay Pascal, Alexandros Triantafyllidis, JM33133, Xule, vamX, ya boyyy, subjectnull, Talal Aujan, Alps Aficionado, wassieverse, Ari Malik, James Bentley, Woland, Spencer Kim, Michael Dempsey, Fred von Graf, Elle, zynix, William Richards, Stanislav Ovsiannikov, Edmond Seymore, Jonathan Leane, Martin Kemka, usrbinkat, Enrico Ros


Thank you to all my generous patrons and donaters!

And thank you again to a16z for their generous grant.

<!-- footer end -->

<!-- original-model-card start -->
# Original model card: Seedbox's KafkaLM 70B German V0.1


![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/645ded34a45b4182d7f5c385/hJ7zsOGDgLWUmf7vbaoI_.jpeg)


# KafkaLM-70B-German-V0.1

**KafkaLM 70b** is a 70b model based on [Llama2 70B Base Model](https://huggingface.co/meta-llama/Llama-2-70b-hf) which was finetuned on an ensemble of popular high-quality open-source instruction sets (translated from English to German).

KafkaLM 70b is a [Seedbox](https://huggingface.co/seedboxai) project trained by [Dennis Dickmann](https://huggingface.co/doubledsbv).

**Why Kafka?**
The models are proficient, yet creative, have some tendencies to linguistically push boundaries 😊


## Model Details

The purpose of releasing the **KafkaLM series** is to contribute to the German AI community with a set of fine-tuned LLMs that are easy to use in everyday applications across a variety of tasks.

The main goal was to provide LLMs proficient in German, especially to be used in German-speaking business contexts where English alone is not sufficient.


### Dataset

I used a 4k filtered version of the following [seedboxai/multitask_german_examples_32k](https://huggingface.co/datasets/seedboxai/multitask_german_examples_32k)

### Prompt Format


This model follows the subsequent prompt format:

```
<|system|>
Du bist ein freundlicher und hilfsbereiter KI-Assistent. Du beantwortest Fragen faktenorientiert und präzise, ohne dabei relevante Fakten auszulassen.</s>
<|user|>
Welche Möglichkeiten der energetischen Sanierung habe ich neben Solar und Energiespeicher?</s>
<|assistant|>
```

### Inference

Getting started with the model is straight forward

```python
import transformers

model_id = "seedboxai/KafkaLM-70B-German-V0.1"

model = AutoModelForCausalLM.from_pretrained(model_id, load_in_4bit=True)

tokenizer = AutoTokenizer.from_pretrained(model_id)

tokenizer.padding_side = "right"
tokenizer.pad_token = tokenizer.unk_token
tokenizer.add_eos_token = False

def generate_prompt(input):
    prompt = ''
    sys_prompt = "Du bist ein freundlicher und hilfsbereiter KI-Assistent. Du beantwortest Fragen faktenorientiert und präzise, ohne dabei relevante Fakten auszulassen."

    prompt += f"<|system|>\n{sys_prompt.strip()}</s>\n"
    prompt += f"<|user|>\n{input.strip()}</s>\n"
    prompt += f"<|assistant|>\n"

    return prompt.strip()


generate_text = transformers.pipeline(
    model=model, tokenizer=tokenizer,
    return_full_text=True,
    task='text-generation',
    temperature=0.5,
    max_new_tokens=512,
    top_p=0.95,
    top_k=50,
    do_sample=True,
)

print(generate_text(generate_prompt("Wer ist eigentlich dieser Kafka?"))

```

## Disclaimer

The license on this model does not constitute legal advice. We are not responsible for the actions of third parties who use this model.
This model should only be used for research purposes. The original Llama2 license and all restrictions of datasets used to train this model apply.

<!-- original-model-card end -->

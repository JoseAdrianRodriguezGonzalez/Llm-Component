---
base_model: zzlgreat/deepsex-34b
datasets:
- lemonilia/LimaRP
- PygmalionAI/PIPPA
inference: false
language:
- en
license: mit
model_creator: zhouliang
model_name: Deepsex 34B
model_type: yi
pipeline_tag: text-generation
prompt_template: 'Below is an instruction that describes a task. Write a response
  that appropriately completes the request.


  ### Instruction:

  {prompt}


  ### Response:

  '
quantized_by: TheBloke
tags:
- roleplay
- not-for-all-audiences
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

# Deepsex 34B - GGUF
- Model creator: [zhouliang](https://huggingface.co/zzlgreat)
- Original model: [Deepsex 34B](https://huggingface.co/zzlgreat/deepsex-34b)

<!-- description start -->
## Description

This repo contains GGUF format model files for [zhouliang's Deepsex 34B](https://huggingface.co/zzlgreat/deepsex-34b).

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

* [AWQ model(s) for GPU inference.](https://huggingface.co/TheBloke/deepsex-34b-AWQ)
* [GPTQ models for GPU inference, with multiple quantisation parameter options.](https://huggingface.co/TheBloke/deepsex-34b-GPTQ)
* [2, 3, 4, 5, 6 and 8-bit GGUF models for CPU+GPU inference](https://huggingface.co/TheBloke/deepsex-34b-GGUF)
* [zhouliang's original unquantised fp16 model in pytorch format, for GPU inference and for further conversions](https://huggingface.co/zzlgreat/deepsex-34b)
<!-- repositories-available end -->

<!-- prompt-template start -->
## Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

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
| [deepsex-34b.Q2_K.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q2_K.gguf) | Q2_K | 2 | 14.56 GB| 17.06 GB | smallest, significant quality loss - not recommended for most purposes |
| [deepsex-34b.Q3_K_S.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q3_K_S.gguf) | Q3_K_S | 3 | 14.96 GB| 17.46 GB | very small, high quality loss |
| [deepsex-34b.Q3_K_M.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q3_K_M.gguf) | Q3_K_M | 3 | 16.64 GB| 19.14 GB | very small, high quality loss |
| [deepsex-34b.Q3_K_L.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q3_K_L.gguf) | Q3_K_L | 3 | 18.14 GB| 20.64 GB | small, substantial quality loss |
| [deepsex-34b.Q4_0.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q4_0.gguf) | Q4_0 | 4 | 19.47 GB| 21.97 GB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [deepsex-34b.Q4_K_S.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q4_K_S.gguf) | Q4_K_S | 4 | 19.54 GB| 22.04 GB | small, greater quality loss |
| [deepsex-34b.Q4_K_M.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q4_K_M.gguf) | Q4_K_M | 4 | 20.66 GB| 23.16 GB | medium, balanced quality - recommended |
| [deepsex-34b.Q5_0.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q5_0.gguf) | Q5_0 | 5 | 23.71 GB| 26.21 GB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [deepsex-34b.Q5_K_S.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q5_K_S.gguf) | Q5_K_S | 5 | 23.71 GB| 26.21 GB | large, low quality loss - recommended |
| [deepsex-34b.Q5_K_M.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q5_K_M.gguf) | Q5_K_M | 5 | 24.32 GB| 26.82 GB | large, very low quality loss - recommended |
| [deepsex-34b.Q6_K.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q6_K.gguf) | Q6_K | 6 | 28.21 GB| 30.71 GB | very large, extremely low quality loss |
| [deepsex-34b.Q8_0.gguf](https://huggingface.co/TheBloke/deepsex-34b-GGUF/blob/main/deepsex-34b.Q8_0.gguf) | Q8_0 | 8 | 36.54 GB| 39.04 GB | very large, extremely low quality loss - not recommended |

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

Under Download Model, you can enter the model repo: TheBloke/deepsex-34b-GGUF and below it, a specific filename to download, such as: deepsex-34b.Q4_K_M.gguf.

Then click Download.

### On the command line, including multiple files at once

I recommend using the `huggingface-hub` Python library:

```shell
pip3 install huggingface-hub
```

Then you can download any individual model file to the current directory, at high speed, with a command like this:

```shell
huggingface-cli download TheBloke/deepsex-34b-GGUF deepsex-34b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

<details>
  <summary>More advanced huggingface-cli download usage (click to read)</summary>

You can also download multiple files at once with a pattern:

```shell
huggingface-cli download TheBloke/deepsex-34b-GGUF --local-dir . --local-dir-use-symlinks False --include='*Q4_K*gguf'
```

For more documentation on downloading with `huggingface-cli`, please see: [HF -> Hub Python Library -> Download files -> Download from the CLI](https://huggingface.co/docs/huggingface_hub/guides/download#download-from-the-cli).

To accelerate downloads on fast connections (1Gbit/s or higher), install `hf_transfer`:

```shell
pip3 install hf_transfer
```

And set environment variable `HF_HUB_ENABLE_HF_TRANSFER` to `1`:

```shell
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download TheBloke/deepsex-34b-GGUF deepsex-34b.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```

Windows Command Line users: You can set the environment variable by running `set HF_HUB_ENABLE_HF_TRANSFER=1` before the download command.
</details>
<!-- README_GGUF.md-how-to-download end -->

<!-- README_GGUF.md-how-to-run start -->
## Example `llama.cpp` command

Make sure you are using `llama.cpp` from commit [d0cee0d](https://github.com/ggerganov/llama.cpp/commit/d0cee0d36d5be95a0d9088b674dbb27354107221) or later.

```shell
./main -ngl 35 -m deepsex-34b.Q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -p "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{prompt}\n\n### Response:"
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
  model_path="./deepsex-34b.Q4_K_M.gguf",  # Download the model file first
  n_ctx=4096,  # The max sequence length to use - note that longer sequence lengths require much more resources
  n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance
  n_gpu_layers=35         # The number of layers to offload to GPU, if you have GPU acceleration available
)

# Simple inference example
output = llm(
  "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\n{prompt}\n\n### Response:", # Prompt
  max_tokens=512,  # Generate up to 512 tokens
  stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
  echo=True        # Whether to echo the prompt
)

# Chat Completion API

llm = Llama(model_path="./deepsex-34b.Q4_K_M.gguf", chat_format="llama-2")  # Set chat_format according to the model you are using
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
# Original model card: zhouliang's Deepsex 34B


**Deepsex-34b**

tks [TheBloke](https://huggingface.co/TheBloke) making quantized version!
gguf:https://huggingface.co/TheBloke/deepsex-34b-GGUF
exl2:https://huggingface.co/waldie/deepsex-34b-4bpw-h6-exl2
awq:https://huggingface.co/TheBloke/deepsex-34b-AWQ

Here are the steps to make this model:
1. I first collected a total collection of about 4GB of various light novels, and used BERT to perform two rounds of similarity deduplication on the novels with similar plots in the data set. In addition, a portion of nsfw novels are mixed in to improve the NSFW capabilities of the model.
2. Then use the YI-34B-base as the base of the model, use the setting of r=64 alpha=128 and use qlora to fine-tune 3 epochs for continuous pre-training.
3. Prepare the limarp+pippa data set, clean it into alpaca format, and use [goliath-120b](https://huggingface.co/alpindale/goliath-120b), which is good at role-playing, to score each question and answer pair, and filter out the high-quality ones. 30k data.
4. Use the data in 3 for sft on the base model obtained in 2, 6 epochs, r=16 alpha=32 for fine-tuning.

*Format*

alpaca

```
[
  {
    "instruction": "user instruction (required)",
    "input": "user input (optional)",
    "output": "model response (required)",
    "history": [
      ["user instruction in the first round (optional)", "model response in the first round (optional)"],
      ["user instruction in the second round (optional)", "model response in the second round (optional)"]
    ]
  }
]
```

*Effect*:
Proficient in role-playing skills, while being highly accepted on NSFW, pure love words will appear from time to time. like:
```#3
Sweaty old man
December 5, 2023 2:03 PM
Fxxk, you are such a xxx!

#4
27.3s
Mirai
December 5, 2023 2:03 PM
"Of course I do! I can't break promises, Sweaty old man. We have been together since we were kids. We are both best friends and lovers to end all iteration." I smiled with affection. It was clear that I meant everything I said. "We both know that you like taking command of us like this. Am I not your squirting toy, Sweaty old man?" I asked with a cute pout. "We should meet up in front of the shop after classes. I'll see you there. See you, Sweaty old man!"
```
It feels like it’s still worth a try~

Support me [here](https://ko-fi.com/mikolisa) :)


**Deepsex-34b**

*步骤*
1. 我先收集了各种轻小说大约4GB的总集，通过bert对该数据集中剧情比较相似的小说进行了两轮相似度去重。另外混入了一部分nsfw小说以提高该模型的NSFW能力。
2. 然后将该模型以YI-34B-base为基座，使用r=64 alpha=128 的设置使用qlora微调了3个epochs来进行持续预训练。
3. 准备limarp+pippa数据集，统一清洗为alpaca格式，并且使用比较擅长角色扮演的[goliath-120b](https://huggingface.co/alpindale/goliath-120b)对每个问答对进行打分，筛选出其中质量高的大约30k数据。
4. 对2中得到的base模型使用3中的数据进行sft，6个epochs，r=16 alpha=32进行微调。

*格式*

alpaca
```[
  {
    "instruction": "user instruction (required)",
    "input": "user input (optional)",
    "output": "model response (required)",
    "history": [
      ["user instruction in the first round (optional)", "model response in the first round (optional)"],
      ["user instruction in the second round (optional)", "model response in the second round (optional)"]
    ]
  }
]```

*效果*
熟练的角色扮演技能，在NSFW上有很高接受度的同时，会时不时的出现纯爱的话语。如：
```#3
Sweaty old man
December 5, 2023 2:03 PM
Fxxk, you are such a xxx!

#4
27.3s
Mirai
December 5, 2023 2:03 PM
"Of course I do! I can't break promises, Sweaty old man. We have been together since we were kids. We are both best friends and lovers to end all iteration." I smiled with affection. It was clear that I meant everything I said. "We both know that you like taking command of us like this. Am I not your squirting toy, Sweaty old man?" I asked with a cute pout. "We should meet up in front of the shop after classes. I'll see you there. See you, Sweaty old man!"
```
感觉还是很值得一试的~
如果觉得好用，欢迎支持我一杯 [咖啡](https://ko-fi.com/mikolisa) :)

<!-- original-model-card end -->

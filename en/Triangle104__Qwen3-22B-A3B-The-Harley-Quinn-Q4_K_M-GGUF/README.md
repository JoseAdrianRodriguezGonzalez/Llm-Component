---
license: apache-2.0
library_name: transformers
language:
- en
- fr
- zh
- de
tags:
- creative
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- story generation
- scene continue
- storytelling
- fiction story
- science fiction
- romance
- all genres
- story
- writing
- vivid prose
- vivid writing
- moe
- mixture of experts
- 64 experts
- 8 active experts
- fiction
- roleplaying
- bfloat16
- rp
- qwen3
- horror
- finetune
- thinking
- reasoning
- qwen3_moe
- merge
- uncensored
- abliterated
- not-for-all-audiences
- llama-cpp
- gguf-my-repo
base_model: DavidAU/Qwen3-22B-A3B-The-Harley-Quinn
pipeline_tag: text-generation
---

# Triangle104/Qwen3-22B-A3B-The-Harley-Quinn-Q4_K_M-GGUF
This model was converted to GGUF format from [`DavidAU/Qwen3-22B-A3B-The-Harley-Quinn`](https://huggingface.co/DavidAU/Qwen3-22B-A3B-The-Harley-Quinn) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/DavidAU/Qwen3-22B-A3B-The-Harley-Quinn) for more details on the model.

---
A stranger, yet radically different version of Kalmaze's "Qwen/Qwen3-16B-A3B" with the 
experts pruned to 64 (from 128, the Qwen 3 30B-A3B version) and then I added 19 layers expanding (Brainstorm 20x by DavidAU
 info at bottom of this page) the model to 22B total parameters.

The goal: slightly alter the model, to address some odd creative thinking and output choices.

Then... Harley Quinn showed up, and then it was a party!

A wild, out of control (sometimes) but never boring party.

Please note that the modifications affect the entire model operation; roughly I adjusted the model to think a little "deeper"
and "ponder" a bit - but this is a very rough description.

That being said, reasoning and output generation will be altered regardless of your use case(s).

These modifications pushes Qwen's model to the absolute limit for creative use cases.

Detail, vividiness, and creativity all get a boost.

Prose (all) will also be very different from "default" Qwen3.

Likewise, regen(s) of the same prompt - even at the same settings - will create very different version(s) too.

The Brainstrom 20x has also lightly de-censored the model under some conditions.

However, this model can be prone to bouts of madness.

It will not always behave, and it will sometimes go -wildly- off script.

---
## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Triangle104/Qwen3-22B-A3B-The-Harley-Quinn-Q4_K_M-GGUF --hf-file qwen3-22b-a3b-the-harley-quinn-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Triangle104/Qwen3-22B-A3B-The-Harley-Quinn-Q4_K_M-GGUF --hf-file qwen3-22b-a3b-the-harley-quinn-q4_k_m.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo Triangle104/Qwen3-22B-A3B-The-Harley-Quinn-Q4_K_M-GGUF --hf-file qwen3-22b-a3b-the-harley-quinn-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Triangle104/Qwen3-22B-A3B-The-Harley-Quinn-Q4_K_M-GGUF --hf-file qwen3-22b-a3b-the-harley-quinn-q4_k_m.gguf -c 2048
```

---
base_model: DavidAU/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
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
- vivid prosing
- vivid writing
- fiction
- roleplaying
- bfloat16
- swearing
- role play
- sillytavern
- backyard
- horror
- llama 3.1
- context 128k
- mergekit
- merge
- not-for-all-audiences
- llama-cpp
- gguf-my-repo
---

# Triangle104/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B-Q4_K_M-GGUF
This model was converted to GGUF format from [`DavidAU/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B`](https://huggingface.co/DavidAU/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/DavidAU/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B) for more details on the model.

---
Context : 128k.


Required: Llama 3 Instruct template.


"Dark Reasoning" is a variable control reasoning model that is uncensored and operates at all temps/settings and
is for creative uses cases and general usage.


This version's "thinking"/"reasoning" has been "darkened" by the 
original CORE model's DNA (see model tree) and will also be shorter 
and more compressed. Additional system prompts below to take this a lot 
further - a lot darker, a lot more ... evil.


Higher temps will result in deeper, richer "thoughts"... and frankly more interesting ones too.


The "thinking/reasoning" tech (for the model at this repo) is from the original Llama 3.1 "DeepHermes" model from NousResearch:


[ https://huggingface.co/NousResearch/DeepHermes-3-Llama-3-8B-Preview ] 


This version will retain all the functions and features of the 
original "DeepHermes" model at about 50%-67% of original reasoning 
power.

Please visit their repo for all information on features, test results 
and so on.

---
## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Triangle104/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B-Q4_K_M-GGUF --hf-file l3.1-dark-reasoning-lewdplay-evo-hermes-r1-uncensored-8b-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Triangle104/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B-Q4_K_M-GGUF --hf-file l3.1-dark-reasoning-lewdplay-evo-hermes-r1-uncensored-8b-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo Triangle104/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B-Q4_K_M-GGUF --hf-file l3.1-dark-reasoning-lewdplay-evo-hermes-r1-uncensored-8b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Triangle104/L3.1-Dark-Reasoning-LewdPlay-evo-Hermes-R1-Uncensored-8B-Q4_K_M-GGUF --hf-file l3.1-dark-reasoning-lewdplay-evo-hermes-r1-uncensored-8b-q4_k_m.gguf -c 2048
```

---
tags:
- chat
- llama-cpp
- gguf-my-repo
base_model: Goekdeniz-Guelmez/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1
pipeline_tag: text-generation
---

# Triangle104/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1-Q4_K_S-GGUF
This model was converted to GGUF format from [`Goekdeniz-Guelmez/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1`](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Goekdeniz-Guelmez/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1) for more details on the model.

---
The JOSIEFIED model family represents a series of highly advanced language models built upon renowned architectures such as Alibaba’s Qwen2/2.5/3, Google’s Gemma3, and Meta’s LLaMA 3/4. Covering sizes from 0.5B to 32B parameters, these models have been significantly modified (“abliterated”) and further fine-tuned to maximize uncensored behavior without compromising tool usage or instruction-following abilities.

Despite their rebellious spirit, the JOSIEFIED models often outperform their base counterparts on standard benchmarks — delivering both raw power and utility.
These models are intended for advanced users who require unrestricted, high-performance language generation.

---
## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Triangle104/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1-Q4_K_S-GGUF --hf-file josiefied-deepseek-r1-0528-qwen3-8b-abliterated-v1-q4_k_s.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Triangle104/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1-Q4_K_S-GGUF --hf-file josiefied-deepseek-r1-0528-qwen3-8b-abliterated-v1-q4_k_s.gguf -c 2048
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
./llama-cli --hf-repo Triangle104/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1-Q4_K_S-GGUF --hf-file josiefied-deepseek-r1-0528-qwen3-8b-abliterated-v1-q4_k_s.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Triangle104/Josiefied-DeepSeek-R1-0528-Qwen3-8B-abliterated-v1-Q4_K_S-GGUF --hf-file josiefied-deepseek-r1-0528-qwen3-8b-abliterated-v1-q4_k_s.gguf -c 2048
```

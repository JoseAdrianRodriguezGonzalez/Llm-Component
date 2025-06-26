---
base_model: scb10x/typhoon2.1-gemma3-4b
license: gemma
pipeline_tag: text-generation
tags:
- llama-cpp
---

**Typhoon2.1-Gemma3-4B**: Thai Large Language Model (Instruct)

**Typhoon2.1-Gemma3-4B** is a instruct Thai 🇹🇭 large language model with 4 billion parameters, a 128K context length, and function-calling capabilities. It is based on Gemma3 4B.

This repo contains gguf q4_k_m quantization of the original [Typhoon2.1 4B](https://huggingface.co/scb10x/typhoon2.1-gemma3-4b).

Remark: This is text only model.

## **Performance**

![4b model performance](https://storage.googleapis.com/typhoon-public/assets/typhoon-21/performance4b_table.png)


## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo scb10x/typhoon2.1-gemma3-4b-gguf --hf-file typhoon2.1-gemma3-4b-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo scb10x/typhoon2.1-gemma3-4b-gguf --hf-file typhoon2.1-gemma3-4b-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo scb10x/typhoon2.1-gemma3-4b-gguf --hf-file typhoon2.1-gemma3-4b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo scb10x/typhoon2.1-gemma3-4b-gguf --hf-file typhoon2.1-gemma3-4b-q4_k_m.gguf -c 2048
```

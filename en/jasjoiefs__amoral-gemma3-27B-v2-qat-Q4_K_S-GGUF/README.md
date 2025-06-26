---
base_model: soob3123/amoral-gemma3-27B-v2-qat
datasets:
- TheDrummer/AmoralQA-v2
language:
- en
license: apache-2.0
pipeline_tag: text-generation
tags:
- text-generation-inference
- transformers
- gemma3
- analytical-tasks
- bias-neutralization
- uncensored
- llama-cpp
- gguf-my-repo
---

# jasjoiefs/amoral-gemma3-27B-v2-qat-Q4_K_S-GGUF
This model was converted to GGUF format from [`soob3123/amoral-gemma3-27B-v2-qat`](https://huggingface.co/soob3123/amoral-gemma3-27B-v2-qat) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/soob3123/amoral-gemma3-27B-v2-qat) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo jasjoiefs/amoral-gemma3-27B-v2-qat-Q4_K_S-GGUF --hf-file amoral-gemma3-27b-v2-qat-q4_k_s.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo jasjoiefs/amoral-gemma3-27B-v2-qat-Q4_K_S-GGUF --hf-file amoral-gemma3-27b-v2-qat-q4_k_s.gguf -c 2048
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
./llama-cli --hf-repo jasjoiefs/amoral-gemma3-27B-v2-qat-Q4_K_S-GGUF --hf-file amoral-gemma3-27b-v2-qat-q4_k_s.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo jasjoiefs/amoral-gemma3-27B-v2-qat-Q4_K_S-GGUF --hf-file amoral-gemma3-27b-v2-qat-q4_k_s.gguf -c 2048
```

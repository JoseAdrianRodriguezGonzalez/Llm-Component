---
language:
- en
license: cc-by-nc-sa-4.0
tags:
- llama-cpp
- gguf-my-repo
datasets:
- Xilabs/PIPPA-alpaca
pipeline_tag: text-generation
---

# DavidAU/calypso-3b-alpha-v2-Q8_0-GGUF
This model was converted to GGUF format from [`Xilabs/calypso-3b-alpha-v2`](https://huggingface.co/Xilabs/calypso-3b-alpha-v2) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Xilabs/calypso-3b-alpha-v2) for more details on the model.
## Use with llama.cpp

Install llama.cpp through brew.

```bash
brew install ggerganov/ggerganov/llama.cpp
```
Invoke the llama.cpp server or the CLI.

CLI:

```bash
llama-cli --hf-repo DavidAU/calypso-3b-alpha-v2-Q8_0-GGUF --model calypso-3b-alpha-v2.Q8_0.gguf -p "The meaning to life and the universe is"
```

Server:

```bash
llama-server --hf-repo DavidAU/calypso-3b-alpha-v2-Q8_0-GGUF --model calypso-3b-alpha-v2.Q8_0.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

```
git clone https://github.com/ggerganov/llama.cpp &&             cd llama.cpp &&             make &&             ./main -m calypso-3b-alpha-v2.Q8_0.gguf -n 128
```

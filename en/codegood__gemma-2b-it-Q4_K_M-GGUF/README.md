---
license: gemma
library_name: transformers
tags:
- llama-cpp
- gguf-my-repo
widget:
- messages:
  - role: user
    content: How does the brain work?
inference:
  parameters:
    max_new_tokens: 200
extra_gated_heading: Access Gemma on Hugging Face
extra_gated_prompt: To access Gemma on Hugging Face, you’re required to review and
  agree to Google’s usage license. To do this, please ensure you’re logged-in to Hugging
  Face and click below. Requests are processed immediately.
extra_gated_button_content: Acknowledge license
---

# codegood/gemma-2b-it-Q4_K_M-GGUF
This model was converted to GGUF format from [`google/gemma-2b-it`](https://huggingface.co/google/gemma-2b-it) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/google/gemma-2b-it) for more details on the model.
## Use with llama.cpp

Install llama.cpp through brew.

```bash
brew install ggerganov/ggerganov/llama.cpp
```
Invoke the llama.cpp server or the CLI.

CLI:

```bash
llama-cli --hf-repo codegood/gemma-2b-it-Q4_K_M-GGUF --model gemma-2b-it.Q4_K_M.gguf -p "The meaning to life and the universe is"
```

Server:

```bash
llama-server --hf-repo codegood/gemma-2b-it-Q4_K_M-GGUF --model gemma-2b-it.Q4_K_M.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

```
git clone https://github.com/ggerganov/llama.cpp &&             cd llama.cpp &&             make &&             ./main -m gemma-2b-it.Q4_K_M.gguf -n 128
```

---
language:
- it
- en
license: apache-2.0
tags:
- pretrained
- llama-cpp
- gguf-my-repo
datasets:
- uonlp/CulturaX
pipeline_tag: text-generation
widget:
- text: 'La capitale dell''Italia è '
  example_title: Example 1
- text: 'Nel mezzo del cammin di nostra vita '
  example_title: Example 2
- text: 'Una cena senza vino è come '
  example_title: Example 3
---

# mudler/Minerva-3B-base-v1.0-Q8_0-GGUF
This model was converted to GGUF format from [`sapienzanlp/Minerva-3B-base-v1.0`](https://huggingface.co/sapienzanlp/Minerva-3B-base-v1.0) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/sapienzanlp/Minerva-3B-base-v1.0) for more details on the model.
## Use with llama.cpp

Install llama.cpp through brew.

```bash
brew install ggerganov/ggerganov/llama.cpp
```
Invoke the llama.cpp server or the CLI.

CLI:

```bash
llama-cli --hf-repo mudler/Minerva-3B-base-v1.0-Q8_0-GGUF --model minerva-3b-base-v1.0.Q8_0.gguf -p "The meaning to life and the universe is"
```

Server:

```bash
llama-server --hf-repo mudler/Minerva-3B-base-v1.0-Q8_0-GGUF --model minerva-3b-base-v1.0.Q8_0.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

```
git clone https://github.com/ggerganov/llama.cpp &&             cd llama.cpp &&             make &&             ./main -m minerva-3b-base-v1.0.Q8_0.gguf -n 128
```

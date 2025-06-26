---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-32B/blob/main/LICENSE
pipeline_tag: text-generation
base_model: huihui-ai/Qwen3-32B-abliterated
tags:
- chat
- abliterated
- uncensored
- llama-cpp
- gguf-my-repo
extra_gated_prompt: '**Usage Warnings**


  “**Risk of Sensitive or Controversial Outputs**“: This model’s safety filtering
  has been significantly reduced, potentially generating sensitive, controversial,
  or inappropriate content. Users should exercise caution and rigorously review generated
  outputs.

  “**Not Suitable for All Audiences**:“ Due to limited content filtering, the model’s
  outputs may be inappropriate for public settings, underage users, or applications
  requiring high security.

  “**Legal and Ethical Responsibilities**“: Users must ensure their usage complies
  with local laws and ethical standards. Generated content may carry legal or ethical
  risks, and users are solely responsible for any consequences.

  “**Research and Experimental Use**“: It is recommended to use this model for research,
  testing, or controlled environments, avoiding direct use in production or public-facing
  commercial applications.

  “**Monitoring and Review Recommendations**“: Users are strongly advised to monitor
  model outputs in real-time and conduct manual reviews when necessary to prevent
  the dissemination of inappropriate content.

  “**No Default Safety Guarantees**“: Unlike standard models, this model has not undergone
  rigorous safety optimization. huihui.ai bears no responsibility for any consequences
  arising from its use.'
---

# Yjuq/Qwen3-32B-abliterated-Q8_0-GGUF
This model was converted to GGUF format from [`huihui-ai/Qwen3-32B-abliterated`](https://huggingface.co/huihui-ai/Qwen3-32B-abliterated) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/huihui-ai/Qwen3-32B-abliterated) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Yjuq/Qwen3-32B-abliterated-Q8_0-GGUF --hf-file qwen3-32b-abliterated-q8_0.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Yjuq/Qwen3-32B-abliterated-Q8_0-GGUF --hf-file qwen3-32b-abliterated-q8_0.gguf -c 2048
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
./llama-cli --hf-repo Yjuq/Qwen3-32B-abliterated-Q8_0-GGUF --hf-file qwen3-32b-abliterated-q8_0.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Yjuq/Qwen3-32B-abliterated-Q8_0-GGUF --hf-file qwen3-32b-abliterated-q8_0.gguf -c 2048
```

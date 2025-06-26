---
license: mit
base_model:
- AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3
- deepseek-ai/DeepSeek-R1-Distill-Qwen-32B
language:
- en
- tr
pipeline_tag: text-generation
library_name: transformers
tags:
- qwen2.5
- cybersecurity
- ethicalhacking
- informationsecurity
- pentest
---

<img src="https://huggingface.co/AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Safe/resolve/main/DALL%C2%B7E%202025-01-26%2005.35.30%20-%20A%20cute%20Fox%20Terrier%20dog%20in%20a%20cyberpunk%20style%2C%20running%20joyfully%20with%20a%20playful%20and%20friendly%20expression.%20The%20dog%20has%20wire-haired%20white%20and%20tan%20fur%20with%20g.webp" width="1000" />

Finetuned by Alican Kiraz

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://tr.linkedin.com/in/alican-kiraz) 
![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2FAlicanKiraz0) 
![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCEAiUT9FMFemDtcKo9G9nUQ) 

Links:
- Medium: https://alican-kiraz1.medium.com/
- Linkedin: https://tr.linkedin.com/in/alican-kiraz
- X: https://x.com/AlicanKiraz0
- YouTube: https://youtube.com/@alicankiraz0

With the release of the new DeepSeek-R1, I quickly began training SenecaLLM v1.3 based on this model. During training:
* About 20 hours on BF16 with 4×H200
* About 10 hours on BF16 with 8×A100
* About 12 hours on FP32 with 8×H200


**It does not pursue any profit.**

Thanks to DeepSeek R1’s Turkish support capability and the dataset used in SenecaLLM v1.3, it can now provide Turkish support! With the new dataset I’ve prepared, it can produce quite good outputs in the following areas:
* Information Security v1.4
* Incident Response v1.3
* Threat Hunting v1.3
* Ethical Exploit Development v1.2
* Purple Team Tactics v1.2
* Reverse Engineering v1.0

"Those who shed light on others do not remain in darkness..."

# AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Q4_K_M-GGUF
This model was converted to GGUF format from [`AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3`](https://huggingface.co/AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Q4_K_M-GGUF --hf-file seneca-x-deepseek-r1-distill-qwen-32b-v1.3-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Q4_K_M-GGUF --hf-file seneca-x-deepseek-r1-distill-qwen-32b-v1.3-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Q4_K_M-GGUF --hf-file seneca-x-deepseek-r1-distill-qwen-32b-v1.3-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo AlicanKiraz0/Seneca-x-DeepSeek-R1-Distill-Qwen-32B-v1.3-Q4_K_M-GGUF --hf-file seneca-x-deepseek-r1-distill-qwen-32b-v1.3-q4_k_m.gguf -c 2048
```
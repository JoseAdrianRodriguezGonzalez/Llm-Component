---
license: apache-2.0
datasets:
- anon8231489123/Omegle_logs_dataset
language:
- en
pipeline_tag: text-generation
---
My first quantization, this is a q4_0 GGML(ggjtv3) and GGUFv2 quantization of the model https://huggingface.co/acrastt/OmegLLaMA-3B
I hope it's working fine. 🤗

Prompt format:
```
Interests: {interests}
Conversation:
You: {prompt}
Stranger: 
```
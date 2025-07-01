---
license: apache-2.0
datasets:
- 64bits/lima_vicuna_format
language:
- en
pipeline_tag: text-generation
---
This contains the q4_0 GGML(ggjtv3) and GGUFv2 quantization of the model https://huggingface.co/acrastt/Bean-3B

Prompt template:
```
### HUMAN:
{prompt}

### RESPONSE:
<leave a newline for the model to answer>
```
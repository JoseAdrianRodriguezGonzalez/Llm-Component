---
datasets:
- IlyaGusev/saiga_scored
language:
- ru
inference: false
pipeline_tag: text-generation
license: other
license_name: llama3
license_link: https://llama.meta.com/llama3/license/
---

Llama.cpp compatible versions of an original [8B model](https://huggingface.co/IlyaGusev/saiga_llama3_8b).

Download one of the versions, for example `model-q4_K.gguf`.
```
wget https://huggingface.co/IlyaGusev/saiga_llama3_8b_gguf/resolve/main/model-q4_K.gguf
```

Download [interact_llama3_llamacpp.py](https://raw.githubusercontent.com/IlyaGusev/rulm/master/self_instruct/src/interact_llama3_llamacpp.py)
```
wget https://raw.githubusercontent.com/IlyaGusev/rulm/master/self_instruct/src/interact_llama3_llamacpp.py
```

How to run:
```
pip install llama-cpp-python fire

python3 interact_llama3_llamacpp.py model-q4_K.gguf
```

System requirements:
* 10GB RAM for q8_0 and less for smaller quantizations


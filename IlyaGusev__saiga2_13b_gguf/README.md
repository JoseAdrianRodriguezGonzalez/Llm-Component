---
datasets:
- IlyaGusev/ru_turbo_alpaca
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch
- IlyaGusev/ru_turbo_alpaca_evol_instruct
- lksy/ru_instruct_gpt4
language:
- ru
inference: false
pipeline_tag: conversational
license: llama2
---

Llama.cpp compatible versions of an original [13B model](https://huggingface.co/IlyaGusev/saiga2_13b_lora).

Download one of the versions, for example `model-q4_K.gguf`.
```
wget https://huggingface.co/IlyaGusev/saiga2_13b_gguf/resolve/main/model-q4_K.gguf
```

Download [interact_llamacpp.py](https://raw.githubusercontent.com/IlyaGusev/rulm/master/self_instruct/src/interact_llamacpp.py)
```
wget https://raw.githubusercontent.com/IlyaGusev/rulm/master/self_instruct/src/interact_llamacpp.py
```

How to run:
```
pip install llama-cpp-python fire

python3 interact_llamacpp.py model-q4_K.gguf
```

System requirements:
* 18GB RAM for q8_K
* 10GB RAM for q4_K

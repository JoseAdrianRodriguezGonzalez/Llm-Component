---
datasets:
- IlyaGusev/ru_turbo_saiga
- IlyaGusev/ru_sharegpt_cleaned
- IlyaGusev/oasst1_ru_main_branch
- IlyaGusev/gpt_roleplay_realm
- lksy/ru_instruct_gpt4
language:
- ru
inference: false
pipeline_tag: conversational
license: llama2
---

Llama.cpp compatible versions of an original [70B model](https://huggingface.co/IlyaGusev/saiga2_70b_lora).

* Download one of the versions, for example `ggml-model-q4_1.gguf`.
* Download [interact_llamacpp.py](https://raw.githubusercontent.com/IlyaGusev/rulm/master/self_instruct/src/interact_llamacpp.py)

How to run:
```
sudo apt-get install git-lfs
pip install llama-cpp-python fire

python3 interact_llamacpp.py ggml-model-q4_1.gguf
```

System requirements:
* 45GB RAM for q4_1

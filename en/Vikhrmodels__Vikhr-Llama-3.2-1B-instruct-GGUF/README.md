---
library_name: llamacpp
model_name: Vikhr-Gemma-2B-instruct
base_model:
- Vikhrmodels/Vikhr-Llama-3.2-1B
language:
- ru
- en
license: llama3.2
tags:
- instruct
datasets:
- Vikhrmodels/GrandMaster-PRO-MAX
pipeline_tag: text-generation
---

# 💨📱 Vikhr-Llama-3.2-1B-instruct

#### RU

Инструктивная модель на основе Llama-3.2-1B-Instruct, обученная на русскоязычном датасете GrandMaster-PRO-MAX. В 5 раз эффективнее базовой модели, и идеально подходит для запуска на слабых или мобильных устройствах.

#### EN

Instructive model based on Llama-3.2-1B-Instruct, trained on the Russian-language dataset GrandMaster-PRO-MAX. It is 5 times more efficient than the base model, making it perfect for deployment on low-power or mobile devices.
- [HF model](https://huggingface.co/Vikhrmodels/Vikhr-Llama-3.2-1B)

**Рекомендуемая температура для генерации: 0.3** / **Recommended generation temperature: 0.3**.

## Метрики на ru_arena_general / Metrics on ru_arena_general

| **Model**                                   | **Score** | **95% CI**      | **Avg Tokens** | **Std Tokens** | **LC Score** |
| ------------------------------------------- | --------- | --------------- | -------------- | -------------- | ------------ |
| kolibri-vikhr-mistral-0427                  | 22.41     | +1.6 / -1.6     | 489.89         | 566.29         | 46.04        |
| storm-7b                                    | 20.62     | +2.0 / -1.6     | 419.32         | 190.85         | 45.78        |
| neural-chat-7b-v3-3                         | 19.04     | +2.0 / -1.7     | 927.21         | 1211.62        | 45.56        |
| **Vikhrmodels-Vikhr-Llama-3.2-1B-instruct** | **19.04** | **+1.3 / -1.6** | **958.63**     | **1297.33**    | **45.56**    |
| gigachat_lite                               | 17.2      | +1.4 / -1.4     | 276.81         | 329.66         | 45.29        |
| Vikhrmodels-vikhr-qwen-1.5b-it              | 13.19     | +1.4 / -1.6     | 2495.38        | 741.45         | 44.72        |
| meta-llama-Llama-3.2-1B-Instruct            | 4.04      | +0.8 / -0.6     | 1240.53        | 1783.08        | 43.42        |

### Авторы / Authors
- Sergei Bratchikov, [NLP Wanderer](https://t.me/nlpwanderer), [Vikhr Team](https://t.me/vikhrlabs)
- Nikolay Kompanets, [LakoMoor](https://t.me/lakomoor), [Vikhr Team](https://t.me/vikhrlabs)
- Konstantin Korolev, [Vikhr Team](https://t.me/vikhrlabs)
- Aleksandr Nikolich, [Vikhr Team](https://t.me/vikhrlabs)
```
@article{nikolich2024vikhr,
  title={Vikhr: The Family of Open-Source Instruction-Tuned Large Language Models for Russian},
  author={Aleksandr Nikolich and Konstantin Korolev and Sergey Bratchikov and Nikolay Kompanets and Artem Shelmanov},
  journal={arXiv preprint arXiv:2405.13929},
  year={2024},
  url={https://arxiv.org/pdf/2405.13929}
}
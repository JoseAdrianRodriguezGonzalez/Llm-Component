
---

library_name: transformers
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
pipeline_tag: text-generation
language:
  - en
tags:
  - nvidia
  - reasoning
  - math
  - code
  - supervised fine-tuning
  - reinforcement learning
  - pytorch

---

[![QuantFactory Banner](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiuCm7c8lEwEJuRey9kiVZsRn2W-b4pWlu3-X534V3YmVuVc2ZL-NXg2RkzSOOS2JXGHutDuyyNAUtdJI65jGTo8jT9Y99tMi4H4MqL44Uc5QKG77B0d6-JfIkZHFaUA71-RtjyYZWVIhqsNZcx8-OMaA?key=xt3VSDoCbmTY7o-cwwOFwQ)](https://hf.co/QuantFactory)


# QuantFactory/AceReason-Nemotron-1.1-7B-GGUF
This is quantized version of [nvidia/AceReason-Nemotron-1.1-7B](https://huggingface.co/nvidia/AceReason-Nemotron-1.1-7B) created using llama.cpp

# Original Model Card


# AceReason-Nemotron 1.1: Advancing Math and Code Reasoning through SFT and RL Synergy

<p align="center">

[![Technical Report](https://img.shields.io/badge/2506.13284-Technical_Report-blue)](https://arxiv.org/abs/2506.13284)
[![SFT Dataset](https://img.shields.io/badge/🤗-SFT_Datset-blue)](https://huggingface.co/datasets/nvidia/AceReason-1.1-SFT)
[![Math RL Dataset](https://img.shields.io/badge/🤗-Math_RL_Datset-blue)](https://huggingface.co/datasets/nvidia/AceReason-Math)
[![Models](https://img.shields.io/badge/🤗-Models-blue)](https://huggingface.co/collections/nvidia/acereason-682f4e1261dc22f697fd1485)
[![Eval Toolkit](https://img.shields.io/badge/🤗-Eval_Code-blue)](https://huggingface.co/nvidia/AceReason-Nemotron-14B/blob/main/README_EVALUATION.md)
</p>

<img src="fig/main_fig.png" alt="main_fig" style="width: 1000px; max-width: 100%;" />

We're thrilled to introduce [AceReason-Nemotron-1.1-7B](https://huggingface.co/nvidia/AceReason-Nemotron-1.1-7B), a math and code reasoning model built upon the Qwen2.5-Math-7B base. The model is first trained with supervised fine-tuning (SFT) on math and code tasks, then further enhanced through reinforcement learning (RL) using the same recipe as [AceReason-Nemotron-1.0-7B](https://huggingface.co/nvidia/AceReason-Nemotron-7B). We initiate RL training from various SFT models and find that stronger SFT models continue to produce consistently better results after large-scale RL, although the performance gap narrows during RL training. Thanks to its stronger SFT backbone, AceReason-Nemotron-1.1-7B significantly outperforms its predecessor and sets a record-high performance among Qwen2.5-7B-based reasoning models on challenging math and code reasoning benchmarks. For more details, check our [technical report](https://arxiv.org/abs/2506.13284).

## Results

We evaluate our model against competitive reasoning models of comparable size on AIME 2024, AIME 2025, and LiveCodeBench (LCB) v5 (2024/08/01 - 2025/02/01) and v6 (2025/02/01-2025/05/01). 
For AceReason-Nemotron-1.0-7B, the RL training recipe improves its starting SFT model, DeepSeek-R1-Distill-Qwen-7B, by 13.5% on AIME24, 14.6% on AIME25, 14.2% on LCB v5, and 10.0% on LCB v6. 
In comparison, AceReason-Nemotron-1.1-7B, built on a stronger SFT model, also benefits substantially from the same RL recipe, achieving absolute improvements of 10.6% on AIME24, 16.4% on AIME25, 8.4% on LCB v5, and 8.3% on LCB v6.

| **Model** | **AIME 2024<br>(avg@64)** | **AIME 2025<br>(avg@64)** | **LCB v5<br>(avg@8)** | **LCB v6<br>(avg@8)** |
| :---: | :---: | :---: | :---: | :---: |
| <small>Skywork-OR1-7B</small> | 70.2 | 54.6 | 47.6 | 42.7 |
| <small>MiMo-7B-RL</small> | 68.2 | 55.4 | 57.8 | 49.3 |
| <small>o3-mini (low)</small> | 60.0 | 48.3 | 60.9 | - |
| <small>OpenMath-Nemotron-7B</small> | 74.8 | 61.2 | - | - |
| <small>OpenCodeReasoning-Nemotron-7B</small> | - | - | 51.3 | 46.1 |
| <small>Magistral Small (24B)</small> | 70.7 | 62.8 | 55.8 | 47.4 |
| DeepSeek-R1-Distill-Qwen-7B | 55.5 | 39.0 | 37.6 | 34.1 |
| AceReason-Nemotron-1.0-7B | 69.0 | 53.6 | 51.8 | 44.1 |
| Our SFT-7B (starting point of RL) | 62.0 | 48.4 | 48.8 | 43.8 |
| [AceReason-Nemotron-1.1-7B 🤗](https://huggingface.co/nvidia/AceReason-Nemotron-1.1-7B)| 72.6 | 64.8 | 57.2 | 52.1 |


## How to use
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = 'nvidia/AceReason-Nemotron-1.1-7B'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype="auto", device_map="auto")

prompt = "Jen enters a lottery by picking $4$ distinct numbers from $S=\\{1,2,3,\\cdots,9,10\\}.$ $4$ numbers are randomly chosen from $S.$ She wins a prize if at least two of her numbers were $2$ of the randomly chosen numbers, and wins the grand prize if all four of her numbers were the randomly chosen numbers. The probability of her winning the grand prize given that she won a prize is $\\tfrac{m}{n}$ where $m$ and $n$ are relatively prime positive integers. Find $m+n$."
messages = [{"role": "user", "content": prompt}]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to("cuda")

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768,
    temperature=0.6,
    top_p=0.95
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## Usage Recommendations
1. We recommend using the system prompt: "You are a helpful and harmless assistant. You should think step-by-step."
2. We recommend using the following instruction for math questions:
```python
math_question = "MATH_QUESTION"
math_instruction = "Please place your final answer inside \\boxed{}."
system_instruction = "You are a helpful and harmless assistant. You should think step-by-step."

final_prompt = "<|im_start|>system\n" + system_instruction + "<|im_end|>\n<|im_start|>user\n" + math_question + "\n\n" + math_instruction + "<|im_end|>\n<|im_start|>assistant\n<think>\n"
```
3. We recommend using the following instruction for code questions:
```python
code_question = "CODE_QUESTION"
starter_code = "STARTER_CODE" # starter code function header, set empty string ("") if there is no starter code

code_instruction_nostartercode = """Write Python code to solve the problem. Please place the solution code in the following format:\n```python\n# Your solution code here\n```"""
code_instruction_hasstartercode = """Please place the solution code in the following format:\n```python\n# Your solution code here\n```"""
if starter_code != "":
    code_question += "\n\n" + "Solve the problem starting with the provided function header.\n\nFunction header:\n" + "```\n" + starter_code + "\n```"
    code_question += "\n\n" + code_instruction_hasstartercode
else:
    code_question += "\n\n" + code_instruction_nostartercode

final_prompt = "<|im_start|>system\n" + system_instruction + "<|im_end|>\n<|im_start|>user\n" + code_question + "<|im_end|>\n<|im_start|>assistant\n<think>\n"
```
4. Our inference engine for evaluation is vLLM==0.7.3 using top-p=0.95, temperature=0.6, max_tokens=32768.


## Evaluation Toolkit
Please refer to the evaluation code and scripts in https://huggingface.co/nvidia/AceReason-Nemotron-14B/blob/main/README_EVALUATION.md. **For model inference, modify the prompt according to the guidelines in the [Usage Recommendations](#usage-recommendations) section**.

## Correspondence to
Zihan Liu (zihanl@nvidia.com), Zhuolin Yang (zhuoliny@nvidia.com), Yang Chen (yachen@nvidia.com), Chankyu Lee (chankyul@nvidia.com), Wei Ping (wping@nvidia.com)


## License
Your use of this model is governed by the [NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/).


## Release Date
June 16, 2025


## Citation
```
@article{liu2025acereason,
  title={AceReason-Nemotron 1.1: Advancing Math and Code Reasoning through SFT and RL Synergy},
  author={Liu, Zihan and Yang, Zhuolin and Chen, Yang and Lee, Chankyu and Shoeybi, Mohammad and Catanzaro, Bryan and Ping, Wei},
  journal={arXiv preprint arXiv:2506.13284},
  year={2025}
}
```


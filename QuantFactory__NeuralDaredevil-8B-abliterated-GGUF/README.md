---
license: other
tags:
- dpo
base_model: mlabonne/NeuralDaredevil-8B-abliterated
datasets:
- mlabonne/orpo-dpo-mix-40k
model-index:
- name: Daredevil-8B-abliterated-dpomix
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: AI2 Reasoning Challenge (25-Shot)
      type: ai2_arc
      config: ARC-Challenge
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: acc_norm
      value: 69.28
      name: normalized accuracy
    source:
      url: >-
        https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/Daredevil-8B-abliterated-dpomix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: HellaSwag (10-Shot)
      type: hellaswag
      split: validation
      args:
        num_few_shot: 10
    metrics:
    - type: acc_norm
      value: 85.05
      name: normalized accuracy
    source:
      url: >-
        https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/Daredevil-8B-abliterated-dpomix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU (5-Shot)
      type: cais/mmlu
      config: all
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 69.1
      name: accuracy
    source:
      url: >-
        https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/Daredevil-8B-abliterated-dpomix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: TruthfulQA (0-shot)
      type: truthful_qa
      config: multiple_choice
      split: validation
      args:
        num_few_shot: 0
    metrics:
    - type: mc2
      value: 60
    source:
      url: >-
        https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/Daredevil-8B-abliterated-dpomix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Winogrande (5-shot)
      type: winogrande
      config: winogrande_xl
      split: validation
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 78.69
      name: accuracy
    source:
      url: >-
        https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/Daredevil-8B-abliterated-dpomix
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GSM8k (5-shot)
      type: gsm8k
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 71.8
      name: accuracy
    source:
      url: >-
        https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=mlabonne/Daredevil-8B-abliterated-dpomix
      name: Open LLM Leaderboard
pipeline_tag: text-generation
---

# NeuralDaredevil-8B-abliterated-GGUF
This is quantized version of [mlabonne/NeuralDaredevil-8B-abliterated](https://huggingface.co/mlabonne/NeuralDaredevil-8B-abliterated) created using llama.cpp

# Model Description

![image/jpeg](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/gFEhcIDSKa3AWpkNfH91q.jpeg)

This is a DPO fine-tune of [mlabonne/Daredevil-8-abliterated](https://huggingface.co/mlabonne/Daredevil-8B-abliterated), trained on one epoch of [mlabonne/orpo-dpo-mix-40k](https://huggingface.co/datasets/mlabonne/orpo-dpo-mix-40k).
The DPO fine-tuning successfully recovers the performance loss due to the abliteration process, making it an excellent uncensored model.

## 🔎 Applications

NeuralDaredevil-8B-abliterated performs better than the Instruct model on my tests.

You can use it for any application that doesn't require alignment, like role-playing. Tested on LM Studio using the "Llama 3" preset.


## 🏆 Evaluation

### Open LLM Leaderboard

NeuralDaredevil-8B is the best-performing uncensored 8B model on the Open LLM Leaderboard (MMLU score).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/HQtd51mJfVRhJ0lJFLceM.png)

### Nous

Evaluation performed using [LLM AutoEval](https://github.com/mlabonne/llm-autoeval). See the entire leaderboard [here](https://huggingface.co/spaces/mlabonne/Yet_Another_LLM_Leaderboard).

| Model | Average | AGIEval | GPT4All | TruthfulQA | Bigbench |
|---|---:|---:|---:|---:|---:|
| [**mlabonne/NeuralDaredevil-8B-abliterated**](https://huggingface.co/mlabonne/NeuralDaredevil-8B-abliterated) [📄](https://gist.github.com/mlabonne/ae0bf16936cef900b72964b33c99edbc) | **55.87** | **43.73** | **73.6** | **59.36** | **46.8** |
| [mlabonne/Daredevil-8B](https://huggingface.co/mlabonne/Daredevil-8B) [📄](https://gist.github.com/mlabonne/080f9c5f153ea57a7ab7d932cf896f21) | 55.87 | 44.13 | 73.52 | 59.05 | 46.77 |
| [mlabonne/Daredevil-8B-abliterated](https://huggingface.co/mlabonne/Daredevil-8B-abliterated) [📄](https://gist.github.com/mlabonne/32cdd8460804662c856bcb2a20acd49e) | 55.06 | 43.29 | 73.33 | 57.47 | 46.17 |
| [NousResearch/Hermes-2-Theta-Llama-3-8B](https://huggingface.co/NousResearch/Hermes-2-Theta-Llama-3-8B) [📄](https://gist.github.com/mlabonne/5df2a3051dd6eb3368a77b684635dc05) | 54.28 | 43.9 | 72.62 | 56.36 | 44.23 |
| [openchat/openchat-3.6-8b-20240522](https://huggingface.co/openchat/openchat-3.6-8b-20240522) [📄](https://gist.github.com/mlabonne/95eef8e8d26b7b17910dcb78e1c95f4a) | 53.49 | 44.03 | 73.67 | 49.78 | 46.48 |
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) [📄](https://gist.github.com/mlabonne/8329284d86035e6019edb11eb0933628) | 51.34 | 41.22 | 69.86 | 51.65 | 42.64 |
| [meta-llama/Meta-Llama-3-8B](https://huggingface.co/meta-llama/Meta-Llama-3-8B) [📄](https://gist.github.com/mlabonne/616b6245137a9cfc4ea80e4c6e55d847) | 45.42 | 31.1 | 69.95 | 43.91 | 36.7 |

## 🌳 Model family tree

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/ekwRGgnjzEOyprT8sEBFt.png)

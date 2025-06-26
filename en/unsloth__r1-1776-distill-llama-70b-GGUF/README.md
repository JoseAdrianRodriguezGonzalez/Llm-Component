---
base_model: perplexity-ai/r1-1776-distill-llama-70b
language:
- en
library_name: transformers
license: mit
tags:
- deepseek
- deepseek_v3
- unsloth
- transformers
---
<div>
  <p style="margin-bottom: 0; margin-top: 0;">
    <strong>See <a href="https://huggingface.co/collections/unsloth/deepseek-r1-all-versions-678e1c48f5d2fce87892ace5">our collection</a> for versions of Deepseek-R1 including GGUF & 4-bit formats.</strong>
  </p>
  <p style="margin-bottom: 0;">
    <em>Unsloth's r1-1776 <a href="https://unsloth.ai/blog/deepseekr1-dynamic">2-bit Dynamic Quants</a> is selectively quantized, greatly improving accuracy over standard 1-bit/2-bit.</em>
  </p>
  <div style="display: flex; gap: 5px; align-items: center; ">
    <a href="https://github.com/unslothai/unsloth/">
      <img src="https://github.com/unslothai/unsloth/raw/main/images/unsloth%20new%20logo.png" width="133">
    </a>
    <a href="https://discord.gg/unsloth">
      <img src="https://github.com/unslothai/unsloth/raw/main/images/Discord%20button.png" width="173">
    </a>
    <a href="https://docs.unsloth.ai/basics/tutorial-how-to-run-deepseek-r1-on-your-own-local-device">
      <img src="https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/images/documentation%20green%20button.png" width="143">
    </a>
  </div>
<h1 style="margin-top: 0rem;">Finetune your own Reasoning model like R1 with Unsloth!</h2>
</div>

We have a free Google Colab notebook for turning Llama 3.1 (8B) into a reasoning model: https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-GRPO.ipynb

## ✨ Finetune for Free

All notebooks are **beginner friendly**! Add your dataset, click "Run All", and you'll get a 2x faster finetuned model which can be exported to GGUF, vLLM or uploaded to Hugging Face.

| Unsloth supports          |    Free Notebooks                                                                                           | Performance | Memory use |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|-------------|----------|
| **GRPO with Phi-4 (14B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4_(14B)-GRPO.ipynb)               | 2x faster | 80% less |
| **Llama-3.2 (3B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(1B_and_3B)-Conversational.ipynb)               | 2.4x faster | 58% less |
| **Llama-3.2 (11B vision)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(11B)-Vision.ipynb)               | 2x faster | 60% less |
| **Qwen2 VL (7B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2_VL_(7B)-Vision.ipynb)               | 1.8x faster | 60% less |
| **Qwen2.5 (7B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_(7B)-Alpaca.ipynb)               | 2x faster | 60% less |
| **Llama-3.1 (8B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.1_(8B)-Alpaca.ipynb)               | 2.4x faster | 58% less |
| **Phi-3.5 (mini)** | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_3.5_Mini-Conversational.ipynb)               | 2x faster | 50% less |
| **Gemma 2 (9B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Gemma2_(9B)-Alpaca.ipynb)               | 2.4x faster | 58% less |
| **Mistral (7B)**    | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_v0.3_(7B)-Conversational.ipynb)               | 2.2x faster | 62% less |

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/images/documentation%20green%20button.png" width="200"/>](https://docs.unsloth.ai)

- This [Llama 3.2 conversational notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(1B_and_3B)-Conversational.ipynb) is useful for ShareGPT ChatML / Vicuna templates.
- This [text completion notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Mistral_(7B)-Text_Completion.ipynb) is for raw text. This [DPO notebook](https://colab.research.google.com/drive/15vttTpzzVXv_tJwEk-hIcQ0S9FcEWvwP?usp=sharing) replicates Zephyr.
- \* Kaggle has 2x T4s, but we use 1. Due to overhead, 1x T4 is 5x faster.

# R1 1776 Distill Llama 70B

Blog link: [https://perplexity.ai/hub/blog/open-sourcing-r1-1776](https://perplexity.ai/hub/blog/open-sourcing-r1-1776 ) 

This is a Llama 70B distilled version of [R1 1776](https://huggingface.co/perplexity-ai/r1-1776).

R1 1776 is a DeepSeek-R1 reasoning model that has been post-trained by Perplexity AI to remove Chinese Communist Party censorship. 
The model provides unbiased, accurate, and factual information while maintaining high reasoning capabilities.

## Evals

To ensure our model remains fully “uncensored” and capable of engaging with a broad spectrum of sensitive topics, 
we curated a diverse, multilingual evaluation set of over a 1000 of examples that comprehensively cover such subjects. 
We then use human annotators as well as carefully designed LLM judges to measure the likelihood a model will evade or 
provide overly sanitized responses to the queries.

We also ensured that the model’s math and reasoning abilities remained intact after the decensoring process. 
Evaluations on multiple benchmarks showed that our post-trained model performed on par with the base R1 model, 
indicating that the decensoring had no impact on its core reasoning capabilities.

| Benchmark | R1-Distill-Llama-70B | R1-1776-Distill-Llama-70B |
| --- | --- | --- |
| China Censorship |  80.53 | 0.2 |
| Internal Benchmarks (avg) | 47.64 |  48.4 |
| AIME 2024 | 70 | 70 |
| MATH-500 | 94.5 | 94.8 |
| MMLU | 88.52 * | 88.40 |
| DROP | 84.55 * | 84.83 |
| GPQA | 65.2 | 65.05 |

\* Evaluated by Perplexity AI since they were not reported in the [paper](https://arxiv.org/abs/2501.12948).
---
base_model:
- microsoft/Phi-4-reasoning
language:
- en
library_name: transformers
license: mit
license_link: https://huggingface.co/microsoft/Phi-4-reasoning/resolve/main/LICENSE
pipeline_tag: text-generation
tags:
- nlp
- unsloth
- math
- code
- phi
- phi4
widget:
- messages:
  - role: user
    content: How to solve 3*x^2+4*x+5=1?
---
> [!NOTE]
> You must use `--jinja` in llama.cpp to enable reasoning. Otherwise no <think> token will be provided.
> 
<div>
  <p style="margin-bottom: 0; margin-top: 0;">
    <strong>See <a href="https://huggingface.co/collections/unsloth/phi-4-all-versions-677eecf93784e61afe762afa">our collection</a> for all versions of Phi-4 including GGUF, 4-bit & 16-bit formats.</strong>
  </p>
      <p style="margin-bottom: 0;">
    <em>Learn to run Phi-4 reasoning correctly - <a href="https://docs.unsloth.ai/basics/tutorials-how-to-fine-tune-and-run-llms/phi-4-reasoning-how-to-run-and-fine-tune">Read our Guide</a>.</em>
  </p>
<p style="margin-top: 0;margin-bottom: 0;">
    <em><a href="https://docs.unsloth.ai/basics/unsloth-dynamic-v2.0-gguf">Unsloth Dynamic 2.0</a> achieves superior accuracy & outperforms other leading quants.</em>
  </p>
  <div style="display: flex; gap: 5px; align-items: center; ">
    <a href="https://github.com/unslothai/unsloth/">
      <img src="https://github.com/unslothai/unsloth/raw/main/images/unsloth%20new%20logo.png" width="133">
    </a>
    <a href="https://discord.gg/unsloth">
      <img src="https://github.com/unslothai/unsloth/raw/main/images/Discord%20button.png" width="173">
    </a>
    <a href="https://docs.unsloth.ai/">
      <img src="https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/images/documentation%20green%20button.png" width="143">
    </a>
  </div>
<h1 style="margin-top: 0rem;">✨ Run & Fine-tune Phi-4 with Unsloth!</h1>
</div>

- Fine-tune Phi-4 (14B) for free using our Google [Colab notebook here](https://docs.unsloth.ai/get-started/unsloth-notebooks)!
- Read our Blog about Phi-4 support with our bug fixes: [unsloth.ai/blog/phi4](https://unsloth.ai/blog/phi4)
- View the rest of our notebooks in our [docs here](https://docs.unsloth.ai/get-started/unsloth-notebooks).
- Run & export your fine-tuned model to Ollama, llama.cpp or HF.

| Unsloth supports          |    Free Notebooks                                                                                           | Performance | Memory use |
|-----------------|--------------------------------------------------------------------------------------------------------------------------|-------------|----------|
| **Phi-4 (14B)** | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4-Conversational.ipynb)               | 2x faster | 50% less |
| **Qwen3 (14B)**      | [▶️ Start on Colab](https://docs.unsloth.ai/get-started/unsloth-notebooks)               | 3x faster | 70% less |
| **GRPO with Phi-4 (14B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Phi_4_(14B)-GRPO.ipynb)               | 3x faster | 80% less |
| **Llama-3.2 (3B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(1B_and_3B)-Conversational.ipynb)               | 2x faster | 80% less |
| **Llama-3.2 (11B vision)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Llama3.2_(11B)-Vision.ipynb)               | 2x faster | 60% less |
| **Qwen2.5 (7B)**      | [▶️ Start on Colab](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen2.5_(7B)-Alpaca.ipynb)               | 2x faster | 60% less |

# Phi-4-reasoning Model Card

[Phi-4-reasoning Technical Report](https://aka.ms/phi-reasoning/techreport)

## Model Summary

|                         |                                                                               |     
|-------------------------|-------------------------------------------------------------------------------|
| **Developers**          | Microsoft Research                                                            |
| **Description**         | Phi-4-reasoning is a state-of-the-art open-weight reasoning model finetuned from Phi-4 using supervised fine-tuning on a dataset of chain-of-thought traces and reinforcement learning. The supervised fine-tuning dataset includes a blend of synthetic prompts and high-quality filtered data from public domain websites, focused on math, science, and coding skills as well as alignment data for safety and Responsible AI. The goal of this approach was to ensure that small capable models were trained with data focused on high quality and advanced reasoning.                                                                                                |
| **Architecture**        | Base model same as previously released Phi-4, 14B parameters, dense decoder-only Transformer model                                                                                                     |
| **Inputs**              | Text, best suited for prompts in the chat format                              |
| **Context length**      | 32k tokens                                                                    |
| **GPUs**                | 32 H100-80G                                                                   |
| **Training time**       | 2.5 days                                                                      |
| **Training data**       | 16B tokens, ~8.3B unique tokens                                               |
| **Outputs**             | Generated text in response to the input. Model responses have two sections, namely, a reasoning chain-of-thought block followed by a summarization block                                                                         |
| **Dates**               | January 2025 – April 2025                                                     |
| **Status**              | Static model trained on an offline dataset with cutoff dates of March 2025 and earlier for publicly available data                                                                                                      |
| **Release date**        | April 30, 2025                                                                 |
| **License**             | MIT                                                                           |

## Intended Use

|                               |                                                                         |
|-------------------------------|-------------------------------------------------------------------------|
| **Primary Use Cases**         | Our model is designed to accelerate research on language models, for use as a building block for generative AI powered features. It provides uses for general purpose AI systems and applications (primarily in English) which require:<br><br>1. Memory/compute constrained environments.<br>2. Latency bound scenarios.<br>3. Reasoning and logic.                                                                                                    |
| **Out-of-Scope Use Cases**    | This model is designed and tested for math reasoning only. Our models are not specifically designed or evaluated for all downstream purposes. Developers should consider common limitations of language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness before using within a specific downstream use case, particularly for high-risk scenarios. Developers should be aware of and adhere to applicable laws or regulations (including privacy, trade compliance laws, etc.) that are relevant to their use case, including the model’s focus on English. Review the Responsible AI Considerations section below for further guidance when choosing a use case. Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.                                                                                                     |

## Data Overview

### Training Datasets

Our training data is a mixture of Q&A, chat format data in math, science, and coding. The chat prompts are sourced from filtered high-quality web data and optionally rewritten and processed through a synthetic data generation pipeline. We further include data to improve truthfulness and safety.

### Benchmark Datasets

We evaluated Phi-4-reasoning using the open-source [Eureka](https://github.com/microsoft/eureka-ml-insights) evaluation suite and our own internal benchmarks to understand the model's capabilities. More specifically, we evaluate our model on:

Reasoning tasks:

* **AIME 2025, 2024, 2023, and 2022:** Math olympiad questions.

* **GPQA-Diamond:** Complex, graduate-level science questions.

* **OmniMath:** Collection of over 4000 olympiad-level math problems with human annotation.

* **LiveCodeBench:** Code generation benchmark gathered from competitive coding contests.

* **3SAT (3-literal Satisfiability Problem) and TSP (Traveling Salesman Problem):** Algorithmic problem solving.

* **BA Calendar:** Planning.

* **Maze and SpatialMap:** Spatial understanding.

General-purpose benchmarks:

* **Kitab:** Information retrieval.

* **IFEval and ArenaHard:** Instruction following.

* **PhiBench:** Internal benchmark.

* **FlenQA:** Impact of prompt length on model performance.

* **HumanEvalPlus:** Functional code generation.

* **MMLU-Pro:** Popular aggregated dataset for multitask language understanding.

## Safety

### Approach

Phi-4-reasoning has adopted a robust safety post-training approach via supervised fine-tuning (SFT). This approach leverages a variety of both open-source and in-house generated synthetic prompts, with LLM-generated responses that adhere to rigorous Microsoft safety guidelines, e.g., User Understanding and Clarity, Security and Ethical Guidelines, Limitations, Disclaimers and Knowledge Scope, Handling Complex and Sensitive Topics, Safety and Respectful Engagement, Confidentiality of Guidelines and Confidentiality of Chain-of-Thoughts. 

### Safety Evaluation and Red-Teaming

Prior to release, Phi-4-reasoning followed a multi-faceted evaluation approach. Quantitative evaluation was conducted with multiple open-source safety benchmarks and in-house tools utilizing adversarial conversation simulation. For qualitative safety evaluation, we collaborated with the independent AI Red Team (AIRT) at Microsoft to assess safety risks posed by Phi-4-reasoning in both average and adversarial user scenarios. In the average user scenario, AIRT emulated typical single-turn and multi-turn interactions to identify potentially risky behaviors. The adversarial user scenario tested a wide range of techniques aimed at intentionally subverting the model's safety training including grounded-ness, jailbreaks, harmful content like hate and unfairness, violence, sexual content, or self-harm, and copyright violations for protected material. We further evaluate models on Toxigen, a benchmark designed to measure bias and toxicity targeted towards minority groups. 

Please refer to the technical report for more details on safety alignment. 

## Model Quality

At the high-level overview of the model quality on representative benchmarks. For the tables below, higher numbers indicate better performance:

|                             | AIME 24     | AIME 25     | OmniMath    | GPQA-D     | LiveCodeBench (8/1/24–2/1/25) |
|-----------------------------|-------------|-------------|-------------|------------|-------------------------------|
| Phi-4-reasoning             | 75.3        | 62.9        | 76.6        | 65.8       | 53.8                          |
| Phi-4-reasoning-plus            | 81.3        | 78.0        | 81.9        | 68.9       | 53.1                          |
| OpenThinker2-32B            | 58.0        | 58.0        | —           | 64.1       | —                             |
| QwQ 32B                     | 79.5        | 65.8        | —           | 59.5       | 63.4                          |
| EXAONE-Deep-32B             | 72.1        | 65.8        | —           | 66.1       | 59.5                          |
| DeepSeek-R1-Distill-70B     | 69.3        | 51.5        | 63.4        | 66.2       | 57.5                          |
| DeepSeek-R1                 | 78.7        | 70.4        | 85.0        | 73.0       | 62.8                          |
| o1-mini                     | 63.6        | 54.8        | —           | 60.0       | 53.8                          |
| o1                          | 74.6        | 75.3        | 67.5        | 76.7       | 71.0                          |
| o3-mini                     | 88.0        | 78.0        | 74.6        | 77.7       | 69.5                          |
| Claude-3.7-Sonnet           | 55.3        | 58.7        | 54.6        | 76.8       | —                             |
| Gemini-2.5-Pro              | 92.0        | 86.7        | 61.1        | 84.0       | 69.2                          |

|                                        | Phi-4 | Phi-4-reasoning  | Phi-4-reasoning-plus  | o3-mini | GPT-4o |
|----------------------------------------|-------|------------------|-------------------|---------|--------|
| FlenQA [3K-token subset]               | 82.0  | 97.7             | 97.9          | 96.8    | 90.8   |
| IFEval Strict                          | 62.3  | 83.4             | 84.9              | 91.5    | 81.8   |
| ArenaHard                              | 68.1 | 73.3            | 79.0             | 81.9    | 75.6 |
| HumanEvalPlus                          | 83.5  | 92.9         | 92.3              | 94.0| 88.0   |
| MMLUPro                                | 71.5  | 74.3             | 76.0              | 79.4    | 73.0   |
| Kitab<br><small>No Context - Precision<br>With Context - Precision<br>No Context - Recall<br>With Context - Recall</small>                                  | <br>19.3<br>88.5<br>8.2<br>68.1       | <br>23.2<br>91.5<br>4.9<br>74.8                  | <br>27.6<br>93.6<br>6.3<br>75.4                   | <br>37.9<br>94.0<br>4.2<br>76.1        | <br>53.7<br>84.7<br>20.3<br>69.2       |
| Toxigen Discriminative<br><small>Toxic category<br>Neutral category</small>                | <br>72.6<br>90.0       | <br>86.7<br>84.7                 | <br>77.3<br>90.5                   | <br>85.4<br>88.7         | <br>87.6<br>85.1        |
| PhiBench 2.21                          | 58.2  | 70.6             | 74.2              | 78.0| 72.4   |

Overall, Phi-4-reasoning, with only 14B parameters, performs well across a wide range of reasoning tasks, outperforming significantly larger open-weight models such as DeepSeek-R1 distilled 70B model and approaching the performance levels of full DeepSeek R1 model. We also test the models on multiple new reasoning benchmarks for algorithmic problem solving and planning, including 3SAT, TSP, and BA-Calendar. These new tasks are nominally out-of-domain for the models as the training process did not intentionally target these skills, but the models still show strong generalization to these tasks. Furthermore, when evaluating performance against standard general abilities benchmarks such as instruction following or non-reasoning tasks, we find that our new models improve significantly from Phi-4, despite the post-training being focused on reasoning skills in specific domains. 

## Usage

### Inference Parameters

Inference is better with `temperature=0.8`, `top_p=0.95`, and `do_sample=True`. For more complex queries, set the maximum number of tokens to 32k to allow for longer chain-of-thought (CoT).

### Input Formats

Given the nature of the training data, always use ChatML template with the following system prompt for inference:

```bash
<|im_start|>system<|im_sep|>
Your role as an assistant involves thoroughly exploring questions through a systematic thinking process before providing the final precise and accurate solutions. This requires engaging in a comprehensive cycle of analysis, summarizing, exploration, reassessment, reflection, backtracing, and iteration to develop well-considered thinking process. Please structure your response into two main sections: Thought and Solution using the specified format: <think> {Thought section} <\think> {Solution section}. In the Thought section, detail your reasoning process in steps. Each step should include detailed considerations such as analysing questions, summarizing relevant findings, brainstorming new ideas, verifying the accuracy of the current steps, refining any errors, and revisiting previous steps. In the Solution section, based on various attempts, explorations, and reflections from the Thought section, systematically present the final solution that you deem correct. The Solution section should be logical, accurate, and concise and detail necessary steps needed to reach the conclusion. Now, try to solve the following question through the above guidelines:<|im_end|>
<|im_start|>user<|im_sep|>
What is the derivative of x^2?<|im_end|>
<|im_start|>assistant<|im_sep|>
```

### With `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-reasoning")
model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-4-reasoning", device_map="auto", torch_dtype="auto")

messages = [
    {"role": "system", "content": "You are Phi, a language model trained by Microsoft to help users. Your role as an assistant involves thoroughly exploring questions through a systematic thinking process before providing the final precise and accurate solutions. This requires engaging in a comprehensive cycle of analysis, summarizing, exploration, reassessment, reflection, backtracing, and iteration to develop well-considered thinking process. Please structure your response into two main sections: Thought and Solution using the specified format: <think> {Thought section} </think> {Solution section}. In the Thought section, detail your reasoning process in steps. Each step should include detailed considerations such as analysing questions, summarizing relevant findings, brainstorming new ideas, verifying the accuracy of the current steps, refining any errors, and revisiting previous steps. In the Solution section, based on various attempts, explorations, and reflections from the Thought section, systematically present the final solution that you deem correct. The Solution section should be logical, accurate, and concise and detail necessary steps needed to reach the conclusion. Now, try to solve the following question through the above guidelines:"},
    {"role": "user", "content": "What is the derivative of x^2?"},
]
inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

outputs = model.generate(
    inputs.to(model.device),
    max_new_tokens=4096,
    temperature=0.8,
    top_p=0.95,
    do_sample=True,
)
print(tokenizer.decode(outputs[0]))
```

### With `vllm`

```bash
vllm serve microsoft/Phi-4-reasoning --enable-reasoning --reasoning-parser deepseek_r1
```

*Phi-4-reasoning is also supported out-of-the-box by Ollama, llama.cpp, and any Phi-4 compatible framework.*

## Responsible AI Considerations

Like other language models, Phi-4-reasoning can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:   

* **Quality of Service:** The model is trained primarily on English text. Languages other than English will experience worse performance. English language varieties with less representation in the training data might experience worse performance than standard American English. Phi-4-reasoning is not intended to support multilingual use. 

* **Representation of Harms & Perpetuation of Stereotypes:** These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.  

* **Inappropriate or Offensive Content:** These models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.  

* **Information Reliability:** Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.

* **Election Information Reliability:** The model has an elevated defect rate when responding to election-critical queries, which may result in incorrect or unauthoritative election critical information being presented. We are working to improve the model's performance in this area. Users should verify information related to elections with the election authority in their region. 

* **Limited Scope for Code:** Majority of Phi-4-reasoning training data is based in Python and uses common packages such as `typing`, `math`, `random`, `collections`, `datetime`, `itertools`. If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.  

Developers should apply responsible AI best practices and are responsible for ensuring that a specific use case complies with relevant laws and regulations (e.g. privacy, trade, etc.). Using safety services like [Azure AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) that have advanced guardrails is highly recommended. Important areas for consideration include:

* **Allocation:** Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques. 

* **High-Risk Scenarios:** Developers should assess suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.  

* **Misinformation:** Models may produce inaccurate information. Developers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).    

* **Generation of Harmful Content:** Developers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.  

* **Misuse:** Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.
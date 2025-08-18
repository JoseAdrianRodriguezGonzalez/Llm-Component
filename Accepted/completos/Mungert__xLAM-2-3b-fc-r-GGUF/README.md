---
license: cc-by-nc-4.0
datasets:
- Salesforce/APIGen-MT-5k
- Salesforce/xlam-function-calling-60k
language:
- en
pipeline_tag: text-generation
tags:
- function-calling
- LLM Agent
- tool-use
- llama
- qwen
- pytorch
- LLaMA-factory
library_name: transformers
---

# <span style="color: #7FFF7F;">xLAM-2-3b-fc-r GGUF Models</span>


## <span style="color: #7F7FFF;">Model Generation Details</span>

This model was generated using [llama.cpp](https://github.com/ggerganov/llama.cpp) at commit [`6adc3c3e`](https://github.com/ggerganov/llama.cpp/commit/6adc3c3ebc029af058ac950a8e2a825fdf18ecc6).





---

## <span style="color: #7FFF7F;">Quantization Beyond the IMatrix</span>

I've been experimenting with a new quantization approach that selectively elevates the precision of key layers beyond what the default IMatrix configuration provides.

In my testing, standard IMatrix quantization underperforms at lower bit depths, especially with Mixture of Experts (MoE) models. To address this, I'm using the `--tensor-type` option in `llama.cpp` to manually "bump" important layers to higher precision. You can see the implementation here:  
👉 [Layer bumping with llama.cpp](https://github.com/Mungert69/GGUFModelBuilder/blob/main/model-converter/tensor_list_builder.py)

While this does increase model file size, it significantly improves precision for a given quantization level.

### **I'd love your feedback—have you tried this? How does it perform for you?**




---

<a href="https://readyforquantum.com/huggingface_gguf_selection_guide.html" style="color: #7FFF7F;">
  Click here to get info on choosing the right GGUF model format
</a>

---



<!--Begin Original Model Card-->


<p align="center">
<img width="500px" alt="xLAM" src="https://huggingface.co/datasets/jianguozhang/logos/resolve/main/xlam-no-background.png">
</p>


<p align="center">
  <a href="https://arxiv.org/abs/2504.03601">[Paper]</a>  |
  <a href="https://apigen-mt.github.io/">[Homepage]</a>  |
  <a href="https://huggingface.co/datasets/Salesforce/APIGen-MT-5k">[Dataset]</a> |
  <a href="https://github.com/SalesforceAIResearch/xLAM">[Github]</a>
</p>
<hr>

# Welcome to the xLAM-2 Model Family!

[Large Action Models (LAMs)](https://blog.salesforceairesearch.com/large-action-models/) are advanced language models designed to enhance decision-making by translating user intentions into executable actions. As the **brains of AI agents**, LAMs autonomously plan and execute tasks to achieve specific goals, making them invaluable for automating workflows across diverse domains.  
**This model release is for research purposes only.**  

The new **xLAM-2** series, built on our most advanced data synthesis, processing, and training pipelines, marks a significant leap in **multi-turn conversation** and **tool usage**. Trained using our novel APIGen-MT framework, which generates high-quality training data through simulated agent-human interactions. Our models achieve state-of-the-art performance on [**BFCL**](https://gorilla.cs.berkeley.edu/leaderboard.html) and **τ-bench** benchmarks, outperforming frontier models like GPT-4o and Claude 3.5. Notably, even our smaller models demonstrate superior capabilities in multi-turn scenarios while maintaining exceptional consistency across trials.

We've also refined the **chat template** and **vLLM integration**, making it easier to build advanced AI agents. Compared to previous xLAM models, xLAM-2 offers superior performance and seamless deployment across applications.  

<p align="center">
<img width="100%" alt="Model Performance Overview" src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/model_board.png?raw=true">
<br>
<small><i>Comparative performance of larger xLAM-2-fc-r models (8B-70B, trained with APIGen-MT data) against state-of-the-art baselines on function-calling (BFCL v3, as of date 04/02/2025) and agentic (τ-bench) capabilities.</i></small>
</p>


## Table of Contents
- [Usage](#usage)
  - [Basic Usage with Huggingface Chat Template](#basic-usage-with-huggingface-chat-template)
  - [Using vLLM for Inference](#using-vllm-for-inference)
    - [Setup and Serving](#setup-and-serving)
    - [Testing with OpenAI API](#testing-with-openai-api)
- [Benchmark Results](#benchmark-results)
- [Citation](#citation)

---

## Model Series

[xLAM](https://huggingface.co/collections/Salesforce/xlam-models-65f00e2a0a63bbcd1c2dade4) series are significant better at many things including general tasks and function calling. 
For the same number of parameters, the model have been fine-tuned across a wide range of agent tasks and scenarios, all while preserving the capabilities of the original model.


| Model                  | # Total Params | Context Length | Category | Download Model  | Download GGUF files |
|------------------------|----------------|------------|-------|----------------|----------|
| Llama-xLAM-2-70b-fc-r | 70B            | 128k            | Multi-turn Conversation, Function-calling   | [🤗 Link](https://huggingface.co/Salesforce/Llama-xLAM-2-70b-fc-r)         |      NA               |
| Llama-xLAM-2-8b-fc-r      | 8B             | 128k            | Multi-turn Conversation, Function-calling     | [🤗 Link](https://huggingface.co/Salesforce/Llama-xLAM-2-8b-fc-r)              |   [🤗 Link](https://huggingface.co/Salesforce/Llama-xLAM-2-8b-fc-r-gguf)    |
| xLAM-2-32b-fc-r     | 32B            | 32k (max 128k)*            |  Multi-turn Conversation, Function-calling   | [🤗 Link](https://huggingface.co/Salesforce/xLAM-2-32b-fc-r)             |      NA               |
| xLAM-2-3b-fc-r      | 3B             | 32k (max 128k)*            |  Multi-turn Conversation, Function-calling    | [🤗 Link](https://huggingface.co/Salesforce/xLAM-2-3b-fc-r)              |      [🤗 Link](https://huggingface.co/Salesforce/xLAM-2-3b-fc-r-gguf)               |
| xLAM-2-1b-fc-r      | 1B             | 32k (max 128k)*            |  Multi-turn Conversation, Function-calling | [🤗 Link](https://huggingface.co/Salesforce/xLAM-2-1b-fc-r)              |      [🤗 Link](https://huggingface.co/Salesforce/xLAM-2-1b-fc-r-gguf)               |

***Note:** The default context length for Qwen-2.5-based models is 32k, but you can use techniques like YaRN (Yet Another Recursive Network) to achieve maximum 128k context length. Please refer to [here](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct#processing-long-texts) for more details.

You can also explore our previous xLAM series [here](https://huggingface.co/collections/Salesforce/xlam-models-65f00e2a0a63bbcd1c2dade4).

The `-fc` suffix indicates that the models are fine-tuned for **function calling** tasks, while the `-r` suffix signifies a **research** release.

✅ All models are fully compatible with vLLM and Transformers-based inference frameworks.


## Usage

### Framework versions

- Transformers 4.46.1 (or later)
- PyTorch 2.5.1+cu124 (or later)
- Datasets 3.1.0 (or later)
- Tokenizers 0.20.3 (or later)

### Basic Usage with Huggingface Chat Template

The new xLAM models are designed to work seamlessly with the Hugging Face Transformers library and utilize natural chat templates for an easy and intuitive conversational experience. Below are examples of how to use these models.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("Salesforce/Llama-xLAM-2-3b-fc-r")
model = AutoModelForCausalLM.from_pretrained("Salesforce/Llama-xLAM-2-3b-fc-r", torch_dtype=torch.bfloat16, device_map="auto")

# Example conversation with a tool call
messages = [
    {"role": "user", "content": "Hi, how are you?"},
    {"role": "assistant", "content": "Thanks. I am doing well. How can I help you?"},
    {"role": "user", "content": "What's the weather like in London?"},
]

tools = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"], "description": "The unit of temperature to return"}
            },
            "required": ["location"]
        }
    }
]

print("====== prompt after applying chat template ======")
print(tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, tokenize=False))

inputs = tokenizer.apply_chat_template(messages, tools=tools, add_generation_prompt=True, return_dict=True, return_tensors="pt")
input_ids_len = inputs["input_ids"].shape[-1] # Get the length of the input tokens
inputs = {k: v.to(model.device) for k, v in inputs.items()}
print("====== model response ======")
outputs = model.generate(**inputs, max_new_tokens=256)
generated_tokens = outputs[:, input_ids_len:] # Slice the output to get only the newly generated tokens
print(tokenizer.decode(generated_tokens[0], skip_special_tokens=True))
```

### Using vLLM for Inference

The xLAM models can also be efficiently served using vLLM for high-throughput inference. Please use `vllm>=0.6.5` since earlier versions will cause degraded performance for Qwen-based models.

#### Setup and Serving

1. Install vLLM with the required version:
```bash
pip install "vllm>=0.6.5"
```

2. Download the tool parser plugin to your local path:
```bash
wget https://huggingface.co/Salesforce/xLAM-2-1b-fc-r/raw/main/xlam_tool_call_parser.py
```

3. Start the OpenAI API-compatible endpoint:
```bash
vllm serve Salesforce/xLAM-2-1b-fc-r \
  --enable-auto-tool-choice \
  --tool-parser-plugin ./xlam_tool_call_parser.py \
  --tool-call-parser xlam \
  --tensor-parallel-size 1
```

Note: Ensure that the tool parser plugin file is downloaded and that the path specified in `--tool-parser-plugin` correctly points to your local copy of the file. The xLAM series models all utilize the **same** tool call parser, so you only need to download it **once** for all models.

#### Testing with OpenAI API

Here's a minimal example to test tool usage with the served endpoint:

```python
import openai
import json

# Configure the client to use your local vLLM endpoint
client = openai.OpenAI(
    base_url="http://localhost:8000/v1",  # Default vLLM server URL
    api_key="empty"  # Can be any string
)

# Define a tool/function
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature to return"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# Create a chat completion
response = client.chat.completions.create(
    model="Salesforce/xLAM-2-1b-fc-r",  # Model name doesn't matter, vLLM uses the served model
    messages=[
        {"role": "system", "content": "You are a helpful assistant that can use tools."},
        {"role": "user", "content": "What's the weather like in San Francisco?"}
    ],
    tools=tools,
    tool_choice="auto"
)

# Print the response
print("Assistant's response:")
print(json.dumps(response.model_dump(), indent=2))
```

For more advanced configurations and deployment options, please refer to the [vLLM documentation](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html).

## Benchmark Results

### Berkeley Function-Calling Leaderboard (BFCL v3)
<p align="center">
<img width="80%" alt="BFCL Results" src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/bfcl-result.png?raw=true">
<br>
<small><i>Performance comparison of different models on [BFCL leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html). The rank is based on the overall accuracy, which is a weighted average of different evaluation categories. "FC" stands for function-calling mode in contrast to using a customized "prompt" to extract the function calls.</i></small>
</p>

### τ-bench Benchmark

<p align="center">
<img width="80%" alt="Tau-bench Results" src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/taubench-result.png?raw=true">
<br>
<small><i>Success Rate (pass@1) on τ-bench benchmark averaged across at least 5 trials. Our xLAM-2-70b-fc-r model achieves an overall success rate of 56.2% on τ-bench, significantly outperforming the base Llama 3.1 70B Instruct model (38.2%) and other open-source models like DeepSeek v3 (40.6%). Notably, our best model even outperforms proprietary models such as GPT-4o (52.9%) and approaches the performance of more recent models like Claude 3.5 Sonnet (new) (60.1%).</i></small>
</p>

<p align="center">
<img width="80%" alt="Pass^k curves" src="https://github.com/apigen-mt/apigen-mt.github.io/blob/main/img/pass_k_curves_retail_airline.png?raw=true">
<br>
<small><i>Pass^k curves measuring the probability that all 5 independent trials succeed for a given task, averaged across all tasks for τ-retail (left) and τ-airline (right) domains. Higher values indicate better consistency of the models.</i></small>
</p>


## Ethical Considerations

This release is for research purposes only in support of an academic paper. Our models, datasets, and code are not specifically designed or evaluated for all downstream purposes. We strongly recommend users evaluate and address potential concerns related to accuracy, safety, and fairness before deploying this model. We encourage users to consider the common limitations of AI, comply with applicable laws, and leverage best practices when selecting use cases, particularly for high-risk scenarios where errors or misuse could significantly impact people's lives, rights, or safety. For further guidance on use cases, refer to our AUP and AI AUP. 

### Model Licenses

For all Llama relevant models, please also follow corresponding Llama license and terms. Meta Llama 3 is licensed under the Meta Llama 3 Community License, Copyright © Meta Platforms, Inc. All Rights Reserved.

## Citation

If you use our model or dataset in your work, please cite our paper:

```bibtex
@article{prabhakar2025apigen,
  title={APIGen-MT: Agentic PIpeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay},
  author={Prabhakar, Akshara and Liu, Zuxin and Zhu, Ming and Zhang, Jianguo and Awalgaonkar, Tulika and Wang, Shiyu and Liu, Zhiwei and Chen, Haolin and Hoang, Thai and others},
  journal={arXiv preprint arXiv:2504.03601},
  year={2025}
}
```

Additionally, please check our other awesome related works regarding xLAM series and consider citing them as well:


```bibtex
@article{zhang2025actionstudio,
  title={ActionStudio: A Lightweight Framework for Data and Training of Action Models},
  author={Zhang, Jianguo and Hoang, Thai and Zhu, Ming and Liu, Zuxin and Wang, Shiyu and Awalgaonkar, Tulika and Prabhakar, Akshara and Chen, Haolin and Yao, Weiran and Liu, Zhiwei and others},
  journal={arXiv preprint arXiv:2503.22673},
  year={2025}
}
```

```bibtex
@article{zhang2024xlam,
  title={xLAM: A Family of Large Action Models to Empower AI Agent Systems},
  author={Zhang, Jianguo and Lan, Tian and Zhu, Ming and Liu, Zuxin and Hoang, Thai and Kokane, Shirley and Yao, Weiran and Tan, Juntao and Prabhakar, Akshara and Chen, Haolin and others},
  journal={arXiv preprint arXiv:2409.03215},
  year={2024}
}

```

```bibtex
@article{liu2024apigen,
  title={Apigen: Automated pipeline for generating verifiable and diverse function-calling datasets},
  author={Liu, Zuxin and Hoang, Thai and Zhang, Jianguo and Zhu, Ming and Lan, Tian and Tan, Juntao and Yao, Weiran and Liu, Zhiwei and Feng, Yihao and RN, Rithesh and others},
  journal={Advances in Neural Information Processing Systems},
  volume={37},
  pages={54463--54482},
  year={2024}
}
```

```bibtex
@article{zhang2024agentohana,
  title={AgentOhana: Design Unified Data and Training Pipeline for Effective Agent Learning},
  author={Zhang, Jianguo and Lan, Tian and Murthy, Rithesh and Liu, Zhiwei and Yao, Weiran and Tan, Juntao and Hoang, Thai and Yang, Liangwei and Feng, Yihao and Liu, Zuxin and others},
  journal={arXiv preprint arXiv:2402.15506},
  year={2024}
}
```



<!--End Original Model Card-->

---

# <span id="testllm" style="color: #7F7FFF;">🚀 If you find these models useful</span>

Help me test my **AI-Powered Quantum Network Monitor Assistant** with **quantum-ready security checks**:  

👉 [Quantum Network Monitor](https://readyforquantum.com/?assistant=open&utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme)  


The full Open Source Code for the Quantum Network Monitor Service available at my github repos ( repos with NetworkMonitor in the name) : [Source Code Quantum Network Monitor](https://github.com/Mungert69). You will also find the code I use to quantize the models if you want to do it yourself [GGUFModelBuilder](https://github.com/Mungert69/GGUFModelBuilder)

💬 **How to test**:  
 Choose an **AI assistant type**:  
   - `TurboLLM` (GPT-4.1-mini)  
   - `HugLLM` (Hugginface Open-source models)  
   - `TestLLM` (Experimental CPU-only)  

### **What I’m Testing**  
I’m pushing the limits of **small open-source models for AI network monitoring**, specifically:  
- **Function calling** against live network services  
- **How small can a model go** while still handling:  
  - Automated **Nmap security scans**  
  - **Quantum-readiness checks**  
  - **Network Monitoring tasks**  

🟡 **TestLLM** – Current experimental model (llama.cpp on 2 CPU threads on huggingface docker space):  
- ✅ **Zero-configuration setup**  
- ⏳ 30s load time (slow inference but **no API costs**) . No token limited as the cost is low.
- 🔧 **Help wanted!** If you’re into **edge-device AI**, let’s collaborate!  

### **Other Assistants**  
🟢 **TurboLLM** – Uses **gpt-4.1-mini** :
- **It performs very well but unfortunatly OpenAI charges per token. For this reason tokens usage is limited. 
- **Create custom cmd processors to run .net code on Quantum Network Monitor Agents**
- **Real-time network diagnostics and monitoring**
- **Security Audits**
- **Penetration testing** (Nmap/Metasploit)  

🔵 **HugLLM** – Latest Open-source models:  
- 🌐 Runs on Hugging Face Inference API. Performs pretty well using the lastest models hosted on Novita.

### 💡 **Example commands you could test**:  
1. `"Give me info on my websites SSL certificate"`  
2. `"Check if my server is using quantum safe encyption for communication"`  
3. `"Run a comprehensive security audit on my server"`
4. '"Create a cmd processor to .. (what ever you want)" Note you need to install a [Quantum Network Monitor Agent](https://readyforquantum.com/Download/?utm_source=huggingface&utm_medium=referral&utm_campaign=huggingface_repo_readme) to run the .net code on. This is a very flexible and powerful feature. Use with caution!

### Final Word

I fund the servers used to create these model files, run the Quantum Network Monitor service, and pay for inference from Novita and OpenAI—all out of my own pocket. All the code behind the model creation and the Quantum Network Monitor project is [open source](https://github.com/Mungert69). Feel free to use whatever you find helpful.

If you appreciate the work, please consider [buying me a coffee](https://www.buymeacoffee.com/mahadeva) ☕. Your support helps cover service costs and allows me to raise token limits for everyone.

I'm also open to job opportunities or sponsorship.

Thank you! 😊

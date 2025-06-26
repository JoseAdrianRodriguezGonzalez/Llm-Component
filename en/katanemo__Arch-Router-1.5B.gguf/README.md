---
license: other
license_name: katanemo-research
license_link: >-
  https://huggingface.co/katanemo/Arch-Router-1.5B.gguf/blob/main/LICENSE
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
language:
- en
pipeline_tag: text-generation
library_name: transformers
---

# katanemo/Arch-Router-1.5B

## Overview

With the rapid proliferation of large language models (LLMs) -- each optimized for different strengths, style, or latency/cost profile -- routing has become an essential technique to operationalize the use of different models. However, existing LLM routing approaches are limited in two key ways: they evaluate performance using benchmarks that often fail to capture human preferences driven by subjective evaluation criteria, and they typically select from a limited pool of models. 

We introduce a preference-aligned routing framework that guides model selection by matching queries to user-defined domains (e.g., travel) or action types (e.g., image editing) -- offering a practical mechanism to encode preferences in routing decisions. Specifically, we introduce Arch-Router, a compact 1.5B model that learns to map queries to domain-action preferences for model routing decisions. Experiments on conversational datasets demonstrate that our approach achieves state-of-the-art (SOTA) results in matching queries with human preferences, outperforming top proprietary models. 

This model is described in the paper: https://arxiv.org/abs/2506.16655, and powers [Arch](https://github.com/katanemo/arch) the open-source AI-native proxy for agents to enable preference-based routing in a seamless way.

### How It Works

To support effective routing, Arch-Router introduces two key concepts:
- **Domain** – the high-level thematic category or subject matter of a request (e.g., legal, healthcare, programming).
- **Action** – the specific type of operation the user wants performed (e.g., summarization, code generation, booking appointment, translation).

Both domain and action configs are associated with preferred models or model variants. At inference time, Arch-Router analyzes the incoming prompt to infer its domain and action using semantic similarity, task indicators, and contextual cues. It then applies the user-defined routing preferences to select the model best suited to handle the request.

### Key Features

- **Structured Preference Routing**: Aligns prompt request with model strengths using explicit domain–action mappings.
- **Transparent and Controllable**: Makes routing decisions transparent and configurable, empowering users to customize system behavior.
- **Flexible and Adaptive**: Supports evolving user needs, model updates, and new domains/actions without retraining the router.
- **Production-Ready Performance**: Optimized for low-latency, high-throughput applications in multi-model environments.

# Requirements
The code of Arch-Router-1.5B has been in the Hugging Face `transformers` library and we advise you to install latest version:
```bash
pip install transformers>=4.37.0
```


# How to use
We use the following example to illustrate how to use our model to perform routing tasks. Please note that, our model works best with our provided prompt format. 
### Quickstart
````python
import json
from typing import Any, Dict, List
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "katanemo/Arch-Router-1.5B"
model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", torch_dtype="auto", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Please use our provided prompt for best performance
TASK_INSTRUCTION = """
You are a helpful assistant designed to find the best suited route.
You are provided with route description within <routes></routes> XML tags:
<routes>
\n{routes}\n
</routes>

<conversation>
\n{conversation}\n
</conversation>
"""

FORMAT_PROMPT = """
Your task is to decide which route is best suit with user intent on the conversation in <conversation></conversation> XML tags.  Follow the instruction:
1. If the latest intent from user is irrelevant or user intent is full filled, response with other route {"route": "other"}.
2. You must analyze the route descriptions and find the best match route for user latest intent. 
3. You only response the name of the route that best matches the user's request, use the exact name in the <routes></routes>.

Based on your analysis, provide your response in the following JSON formats if you decide to match any route:
{"route": "route_name"} 
"""


# Define route config
route_config = [
    {
        "name": "code_generation",
        "description": "Generating new code snippets, functions, or boilerplate based on user prompts or requirements",
    },
    {
        "name": "bug_fixing",
        "description": "Identifying and fixing errors or bugs in the provided code across different programming languages",
    },
    {
        "name": "performance_optimization",
        "description": "Suggesting improvements to make code more efficient, readable, or scalable",
    },
    {
        "name": "api_help",
        "description": "Assisting with understanding or integrating external APIs and libraries",
    },
    {
        "name": "programming",
        "description": "Answering general programming questions, theory, or best practices",
    },
]


# Helper function to create the system prompt for our model
def format_prompt(
    route_config: List[Dict[str, Any]], conversation: List[Dict[str, Any]]
):
    return (
        TASK_INSTRUCTION.format(
            routes=json.dumps(route_config), conversation=json.dumps(conversation)
        )
        + FORMAT_PROMPT
    )


# Define conversations

conversation = [
    {
        "role": "user",
        "content": "fix this module 'torch.utils._pytree' has no attribute 'register_pytree_node'. did you mean: '_register_pytree_node'?",
    }
]

route_prompt = format_prompt(route_config, conversation)

messages = [
    {"role": "user", "content": route_prompt},
]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

# 2. Generate
generated_ids = model.generate(
    input_ids=input_ids,  # or just positional: model.generate(input_ids, …)
    max_new_tokens=32768,
)

# 3. Strip the prompt from each sequence
prompt_lengths = input_ids.shape[1]  # same length for every row here
generated_only = [
    output_ids[prompt_lengths:]  # slice off the prompt tokens
    for output_ids in generated_ids
]

# 4. Decode if you want text
response = tokenizer.batch_decode(generated_only, skip_special_tokens=True)[0]
print(response)
````

Then you should be able to see the following output string in JSON format:
````python
{"route": "bug_fixing"}
````

To better understand how to create the route descriptions, please take a look at our [Katanemo API](https://docs.archgw.com/guides/llm_router.html).

# License
Katanemo Arch-Router model is distributed under the [Katanemo license](https://huggingface.co/katanemo/Arch-Router-1.5B.gguf/blob/main/LICENSE).
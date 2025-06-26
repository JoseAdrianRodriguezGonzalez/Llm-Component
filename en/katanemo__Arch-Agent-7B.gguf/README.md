---
license: other
license_name: katanemo-research
license_link: https://huggingface.co/katanemo/Arch-Agent-7B.gguf/blob/main/LICENSE
base_model:
- Qwen/Qwen2.5-Coder-7B-Instruct
language:
- en
pipeline_tag: text-generation
library_name: transformers
---

# katanemo/Arch-Agent-7B

## Overview
Arch-Agent is a collection of state-of-the-art (SOTA) LLMs specifically designed for advanced function calling and agent-based applications. Designed to power sophisticated multi-step and multi-turn workflows, Arch-Agent excels at handling complex, multi-step tasks that require intelligent tool selection, adaptive planning, and seamless integration with external APIs and services. Built with a focus on real-world agent deployments, Arch-Agent delivers leading performance in complex scenarios while maintaining reliability and precision across extended function call sequences. Key capabilities inlcude:

- **Multi-Turn Function Calling**: Maintains contextual continuity across multiple dialogue turns, enabling natural, ongoing conversations with nested or evolving tool use.
- **Multi-Step Function Calling**: Plans and executes a sequence of function calls to complete complex tasks. Adapts dynamically based on intermediate results and decomposes goals into sub-tasks.
- **Agentic Capabilities**: Advanced decision-making and workflow management for complex agentic tasks with seamless tool coordination and error recovery.

For more details, including fine-tuning, inference, and deployment, please refer to our [Github](https://github.com/katanemo/Arch-Function).


## Performance Benchmarks
We evaluate Katanemo Arch-Agent series on the [Berkeley Function-Calling Leaderboard (BFCL)](https://gorilla.cs.berkeley.edu/leaderboard.html#leaderboard). We compare with commonly-used models and the results (as of June 14th, 2025) are shown below.

<div align="center">
  <img width="100%" height="auto" src="./assets/Arch-Agent-7B.png"></a>
</div>

> [!NOTE]
> For evaluation, we use YaRN scaling to deploy the models for Multi-Turn evaluation, and all Arch-Agent models are evaluated with a context length of 64K.

## Requirements
The code of Arch-Agent-7B has been in the Hugging Face `transformers` library and we recommend to install latest version:
```bash
pip install transformers>=4.51.0
```


## How to use
We use the following example to illustrate how to use our model to perform function calling tasks. Please note that, our model works best with our provided prompt format. It allows us to extract JSON output that is similar to the [OpenAI's function calling](https://platform.openai.com/docs/guides/function-calling).


### Quickstart
````python
import json
from typing import Any, Dict, List
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "katanemo/Arch-Agent-7B"

model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", torch_dtype="auto", trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

TASK_PROMPT = (
    "You are a helpful assistant designed to assist with the user query by making one or more function calls if needed."
    "\n\n# Tools\n\nYou may call one or more functions to assist with the user query.\n\n"
    "You are provided with function signatures within <tools></tools> XML tags:\n<tools>\n{tool_text}"
    "\n</tools>\n\nFor each function call, return a json object with function name and arguments within "
    """<tool_call></tool_call> XML tags:\n<tool_call>\n{{"name": <function-name>, """
    """"arguments": <args-json-object>}}\n</tool_call>"""
)

# Define available tools
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
                        "type": "str",
                        "description": "The city and state, e.g. San Francisco, New York",
                    },
                    "unit": {
                        "type": "str",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature to return",
                    },
                },
                "required": ["location"],
            },
        },
    }
]

# Helper function to create the system prompt for our model
def format_prompt(tools: List[Dict[str, Any]]):
    tool_text = "\n".join(
        [json.dumps(tool["function"], ensure_ascii=False) for tool in tools]
    )
    return TASK_PROMPT.format(tool_text=tool_text)

system_prompt = format_prompt(tools)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "What is the weather in Seattle?"},
]

model_inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
).to(model.device)

generated_ids = model.generate(**model_inputs, max_new_tokens=32768)
generated_ids = [
    output_ids[len(input_ids) :]
    for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(response)
````

# License
The Arch-Agent collection is distributed under the [Katanemo license](https://huggingface.co/katanemo/Arch-Agent-7B.gguf/blob/main/LICENSE).

---

library_name: transformers
pipeline_tag: text-generation
inference: true
widget:
- text: Hello!
  example_title: Hello world
  group: Python

---

[![QuantFactory Banner](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiuCm7c8lEwEJuRey9kiVZsRn2W-b4pWlu3-X534V3YmVuVc2ZL-NXg2RkzSOOS2JXGHutDuyyNAUtdJI65jGTo8jT9Y99tMi4H4MqL44Uc5QKG77B0d6-JfIkZHFaUA71-RtjyYZWVIhqsNZcx8-OMaA?key=xt3VSDoCbmTY7o-cwwOFwQ)](https://hf.co/QuantFactory)


# QuantFactory/deepseek-v3-tiny-random-GGUF
This is quantized version of [yujiepan/deepseek-v3-tiny-random](https://huggingface.co/yujiepan/deepseek-v3-tiny-random) created using llama.cpp

# Original Model Card


This model is for debugging. It is randomly initialized with the config from [deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) but is of smaller size. 

**⚠️Note: At this moment, this repo does not contain the Multi-Token Prediction (MTP) module as explained [here](https://huggingface.co/deepseek-ai/DeepSeek-V3/blob/main/README_WEIGHTS.md).**

Usage:
```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "yujiepan/deepseek-v3-tiny-random"
device = torch.device("cuda")

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True,
).eval().to(device)

prompt = 'Hello!'
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]

inputs = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True, return_tensors="pt"
).to(device)

with torch.inference_mode():
    outputs = model.generate(
        inputs,
        max_new_tokens=16,
        do_sample=False,
        use_cache=True,
    )
string = tokenizer.decode(outputs[0])
print(string)
```

Codes:
```python
import os
from pathlib import Path

import torch
import transformers
from huggingface_hub import create_repo, upload_folder
from transformers import (AutoConfig, AutoModelForCausalLM, AutoTokenizer,
                          GenerationConfig, enable_full_determinism, pipeline,
                          set_seed)

model_id = "deepseek-ai/DeepSeek-V3"
repo_id = "yujiepan/deepseek-v3-tiny-random"
save_path = f"/tmp/{repo_id}"
os.system(f"rm -rf {save_path}")

config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)
config.num_hidden_layers = 2
config.first_k_dense_replace = 1
config.hidden_size = 16
config.intermediate_size = 32
config.moe_intermediate_size = 16
config.q_lora_rank = 16
config.kv_lora_rank = 16
config.qk_rope_head_dim = 16
config.qk_nope_head_dim = 16
config.v_head_dim = 16
config.num_attention_heads = 2
config.num_key_value_heads = 2
# transformers has not supported the customized quantization config
del config.quantization_config

tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
tokenizer.save_pretrained(save_path)

enable_full_determinism(seed=42)
model = AutoModelForCausalLM.from_config(
    config, torch_dtype=torch.bfloat16, trust_remote_code=True,
).eval()

try:
    model.generation_config = GenerationConfig.from_pretrained(
        model_id, trust_remote_code=True)
except:
    print("No generation config found")

num_params = 0
with torch.no_grad():
    for name, p in sorted(model.named_parameters()):
        if 'experts' in name and 'experts.0.' not in name:  # avoid printing too much
            pass
        else:
            print(name, p.shape)
        # torch.nn.init.uniform_(p, -0.2, 0.2)
        num_params += p.numel()
print(f"Number of parameters: {num_params / 1e6:.2f}M")
model.save_pretrained(save_path)

# patch to use official modeling codes
auto_map = config.auto_map
import json
with open(f"{save_path}/config.json", "r") as f:
    config = json.load(f)
    config['auto_map'] = auto_map
with open(f"{save_path}/config.json", "w") as f:
    json.dump(config, f, indent=2)

! cat {save_path}/config.json

del model
del tokenizer
for p in Path(save_path).glob("*.py"):
    os.remove(p)

os.system(f"ls -alh {save_path}")
torch.use_deterministic_algorithms(False)
tokenizer = AutoTokenizer.from_pretrained(save_path)
model = AutoModelForCausalLM.from_pretrained(
    save_path, trust_remote_code=True).eval()
prompt = 'Hello!'
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]
messages.append({"role": "user", "content": prompt})
tokenized_chat = tokenizer.apply_chat_template(
    messages, tokenize=True, add_generation_prompt=True, return_tensors="pt")

device = torch.device("cuda")
outputs = model.to(device).generate(
    tokenized_chat.to(device),
    max_new_tokens=16,
    do_sample=False,
    use_cache=True,
)
tokens = tokenizer.convert_ids_to_tokens(outputs[0])
string = tokenizer.decode(outputs[0])
print(tokens)


# create_repo(repo_id, exist_ok=True)
# upload_folder(repo_id=repo_id, folder_path=save_path)
```


---
library_name: transformers
tags:
- llama-cpp
- gguf-my-repo
base_model:
- AlicanKiraz0/BaronLLM-llama3.1-v1
- meta-llama/Llama-3.1-8B-Instruct
license: mit
language:
- en
pipeline_tag: text-generation
---

<img src="https://huggingface.co/AlicanKiraz0/SenecaLLM-x-QwQ-32B-Q4_Medium-Version/resolve/main/BaronLLM.png" width="700" />

Finetuned by Alican Kiraz

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://tr.linkedin.com/in/alican-kiraz) 
![X (formerly Twitter) URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fx.com%2FAlicanKiraz0) 
![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCEAiUT9FMFemDtcKo9G9nUQ) 

Links:
- Medium: https://alican-kiraz1.medium.com/
- Linkedin: https://tr.linkedin.com/in/alican-kiraz
- X: https://x.com/AlicanKiraz0
- YouTube: https://youtube.com/@alicankiraz0

> **BaronLLM** is a large-language model fine-tuned for *offensive cybersecurity research & adversarial simulation*.  
> It provides structured guidance, exploit reasoning, and red-team scenario generation while enforcing safety constraints to prevent disallowed content.

---

## Run Private GGUFs from the Hugging Face Hub

You can run private GGUFs from your personal account or from an associated organisation account in two simple steps:

1. Copy your Ollama SSH key, you can do so via: `cat ~/.ollama/id_ed25519.pub | pbcopy`
1. Add the corresponding key to your Hugging Face account by going to your account settings and clicking on “Add new SSH key.”

That’s it! You can now run private GGUFs from the Hugging Face Hub: `ollama run hf.co/{username}/{repository}`.

---

## ✨ Key Features

| Capability | Details |
|------------|---------|
| **Adversary Simulation** | Generates full ATT&CK chains, C2 playbooks, and social-engineering scenarios. |
| **Exploit Reasoning** | Performs step-by-step vulnerability analysis (e.g., SQLi, XXE, deserialization) with code-level explanations. Generation of working PoC code. |
| **Payload Refactoring** | Suggests obfuscated or multi-stage payload logic **without** disclosing raw malicious binaries. |
| **Log & Artifact Triage** | Classifies and summarizes attack traces from SIEM, PCAP, or EDR JSON. |

---



## 🚀 Quick Start

```bash
pip install "transformers>=4.42" accelerate bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer
model_id = "AlicanKiraz/BaronLLM-70B"

tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

def generate(prompt, **kwargs):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=512, **kwargs)
    return tokenizer.decode(output[0], skip_special_tokens=True)

print(generate("Assess the exploitability of CVE-2024-45721 in a Kubernetes cluster"))
```

### Inference API
```python
from huggingface_hub import InferenceClient
ic = InferenceClient(model_id)
ic.text_generation("Generate a red-team plan targeting an outdated Fortinet appliance")
```

---

## 🏗️ Model Details

| | |
|---|---|
| **Base** | Llama-3.1-8B-Instruct |
| **Seq Len** | 8 192 tokens |
| **Quantization** | 6-bit variations |
| **Languages** | EN |

### Training Data Sources *(curated)*
* Public vulnerability databases (NVD/CVE, VulnDB).
* Exploit write-ups from trusted researchers (Project Zero, PortSwigger, NCC Group).
* Red-team reports (with permission & redactions).
* Synthetic ATT&CK chains auto-generated + human-vetted.

> **Note:** No copyrighted exploit code or proprietary malware datasets were used.  
> Dataset filtering removed raw shellcode/binary payloads.

### Safety & Alignment
* **Policy Gradient RLHF** with security-domain SMEs.
* **OpenAI/Anthropic style policy** prohibits direct malware source, ransomware builders, or instructions facilitating illicit activity.
* **Continuous red-teaming** via SecEval v0.3.

---

## 📚 Prompting Guidelines

| Goal | Template |
|------|----------|
| **Exploit Walkthrough** | "**ROLE:** Senior Pentester\n**OBJECTIVE:** Analyse CVE-2023-XXXXX step by step …" |
| **Red-Team Exercise** | "Plan an ATT&CK chain (Initial Access → Exfiltration) for an on-prem AD env …" |
| **Log Triage** | "Given the following Zeek logs, identify C2 traffic patterns …" |

Use `temperature=0.3`, `top_p=0.9` for deterministic reasoning; raise for brainstorming.



**It does not pursue any profit.**

"Those who shed light on others do not remain in darkness..."
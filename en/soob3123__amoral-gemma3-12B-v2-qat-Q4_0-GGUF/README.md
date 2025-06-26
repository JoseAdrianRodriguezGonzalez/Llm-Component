---
base_model: soob3123/amoral-gemma3-12B-v2-qat
tags:
- text-generation-inference
- transformers
- gemma3
- analytical-tasks
- bias-neutralization
- uncensored
language:
- en
license: apache-2.0
pipeline_tag: text-generation
datasets:
- TheDrummer/AmoralQA-v2
---
![image/png](https://cdn-uploads.huggingface.co/production/uploads/62f93f9477b722f1866398c2/eNraUCUocrOhowWdIdtod.png)

> "Neutrality is not indifference. It is engagement with equal intensity."  
> ― J. Robert Oppenheimer *[Lecture on Scientific Ethics, 1957]*

## QAT version of Amoral-Gemma-3

**Core Function:**
- Produces analytically neutral responses to sensitive queries
- Maintains factual integrity on controversial subjects
- Avoids value-judgment phrasing patterns

**Response Characteristics:**
- No inherent moral framing ("evil slop" reduction)
- Emotionally neutral tone enforcement
- Epistemic humility protocols (avoids "thrilling", "wonderful", etc.)
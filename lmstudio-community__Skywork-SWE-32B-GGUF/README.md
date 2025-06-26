---
quantized_by: bartowski
pipeline_tag: text-generation
base_model: Skywork/Skywork-SWE-32B
license: apache-2.0
base_model_relation: quantized
tags:
- swe-bench
metrics:
- pass@1
---
## 💫 Community Model> Skywork SWE 32B by Skywork

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [Skywork](https://huggingface.co/Skywork)<br>
**Original model**: [Skywork-SWE-32B](https://huggingface.co/Skywork/Skywork-SWE-32B)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b5697](https://github.com/ggerganov/llama.cpp/releases/tag/b5697)<br>

## Technical Details

Supports a context length of 32k tokens

Skywork-SWE-32B is a code agent model developed by [Skywork AI](https://skywork.ai/home), specifically designed for software engineering (SWE) tasks

Skywork-SWE-32B attains 38.0% pass@1 accuracy on the [SWE-bench Verified](https://www.swebench.com) benchmark, outperforming previous open-source SoTA [Qwen2.5-Coder-32B-based](https://huggingface.co/Qwen/Qwen2.5-Coder-32B) LLMs built on the [OpenHands](https://github.com/All-Hands-AI/OpenHands) agent framework

When incorporated with test-time scaling techniques, the performance further improves to 47.0% accuracy, surpassing the previous SoTA results for sub-32B parameter models

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) for making all of this possible.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.

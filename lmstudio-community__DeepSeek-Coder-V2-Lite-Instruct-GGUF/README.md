---
license: other
license_name: deepseek-license
license_link: LICENSE
quantized_by: bartowski
pipeline_tag: text-generation
lm_studio:
  param_count: 16b
  use_case: coding
  release_date: 17-06-2024
  model_creator: DeepSeek
  prompt_template: DeepSeek Chat 
  system_prompt: none
  base_model: DeepSeek
  original_repo: deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct
base_model: deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct
---
## 💫 Community Model> DeepSeek-Coder-V2-Lite-Instruct by DeepSeek

*👾 [LM Studio](https://lmstudio.ai) Community models highlights program. Highlighting new & noteworthy models by the community. Join the conversation on [Discord](https://discord.gg/aPQfnNkxGC)*.

**Model creator:** [DeepSeek](https://huggingface.co/deepseek-ai)<br>
**Original model**: [DeepSeek-Coder-V2-Lite-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct)<br>
**GGUF quantization:** provided by [bartowski](https://huggingface.co/bartowski) based on `llama.cpp` release [b3166](https://github.com/ggerganov/llama.cpp/releases/tag/b3166)<br>

## Model Settings:

Requires LM Studio 0.2.25, update can be downloaded from here: https://lmstudio.ai

Flash attention MUST be **disabled** for this model to work.

## Model Summary:

This is a brand new Mixture of Export (MoE) model from DeepSeek, specializing in coding instructions.<br>
This model performs well across a series of coding benchmarks and should be used for both instruction following and code completion.

## Prompt template:

The best performing template is `Deepseek Coder` preset in your LM Studio.

This will format the prompt as follows:

```
You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science.",
### Instruction: {user_message}
### Response: {assistant_message}
```

The "official" template seems to tend towards generating Chinese, however if you'd like to use it you can set it up by choosing the `LM Studio Blank Preset` preset in your LM Studio and then:

Set your User Message Prefix to `User: `

Set your User Message Suffix to `\n\nAssistant: `

This will format the prompt as follows:

```
User: {user_message}

Assistant: {assistant_message}
```

## Technical Details

This model is an MoE architecture, using 16B total weights with only 2.4B activated to achieve excellent inference speed.

DeepSeek-Coder-V2 is based on the DeepSeek-V2 model, further trained on 6 trillion high quality coding tokens to enhance coding and mathematical reasoning. 

It supports an incredible 128k context length.

For more details, read their paper here: https://github.com/deepseek-ai/DeepSeek-Coder-V2/blob/main/paper.pdf

## Special thanks

🙏 Special thanks to [Georgi Gerganov](https://github.com/ggerganov) and the whole team working on [llama.cpp](https://github.com/ggerganov/llama.cpp/) 

🙏 Special thanks to [Kalomaze](https://github.com/kalomaze) and [Dampf](https://github.com/Dampfinchen) for their work on the dataset (linked [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)) that was used for calculating the imatrix for all sizes.

## Disclaimers

LM Studio is not the creator, originator, or owner of any Model featured in the Community Model Program. Each Community Model is created and provided by third parties. LM Studio does not endorse, support, represent or guarantee the completeness, truthfulness, accuracy, or reliability of any Community Model.  You understand that Community Models can produce content that might be offensive, harmful, inaccurate or otherwise inappropriate, or deceptive. Each Community Model is the sole responsibility of the person or entity who originated such Model. LM Studio may not monitor or control the Community Models and cannot, and does not, take responsibility for any such Model. LM Studio disclaims all warranties or guarantees about the accuracy, reliability or benefits of the Community Models.  LM Studio further disclaims any warranty that the Community Model will meet your requirements, be secure, uninterrupted or available at any time or location, or error-free, viruses-free, or that any errors will be corrected, or otherwise. You will be solely responsible for any damage resulting from your use of or access to the Community Models, your downloading of any Community Model, or use of any other Community Model provided by or through LM Studio.
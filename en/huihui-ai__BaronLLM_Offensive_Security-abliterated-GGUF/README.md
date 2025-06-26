---
library_name: transformers
tags:
- llama-cpp
- gguf-my-repo
- chat
- abliterated
- uncensored
base_model:
  - AlicanKiraz0/BaronLLM_Offensive_Security_LLM_Q6_K_GGUF
license: mit
language:
- en
pipeline_tag: text-generation
extra_gated_prompt: >-
    **Usage Warnings**


    “**Risk of Sensitive or Controversial Outputs**“: This model’s safety filtering has been significantly reduced, potentially generating sensitive, controversial, or inappropriate content. Users should exercise caution and rigorously review generated outputs.

    “**Not Suitable for All Audiences**:“ Due to limited content filtering, the model’s outputs may be inappropriate for public settings, underage users, or applications requiring high security.

    “**Legal and Ethical Responsibilities**“: Users must ensure their usage complies with local laws and ethical standards. Generated content may carry legal or ethical risks, and users are solely responsible for any consequences.

    “**Research and Experimental Use**“: It is recommended to use this model for research, testing, or controlled environments, avoiding direct use in production or public-facing commercial applications.

    “**Monitoring and Review Recommendations**“: Users are strongly advised to monitor model outputs in real-time and conduct manual reviews when necessary to prevent the dissemination of inappropriate content.

    “**No Default Safety Guarantees**“: Unlike standard models, this model has not undergone rigorous safety optimization. huihui.ai bears no responsibility for any consequences arising from its use.


---

# huihui-ai/BaronLLM_Offensive_Security-abliterated-GGUF
This is an uncensored version of [AlicanKiraz0/BaronLLM_Offensive_Security_LLM_Q6_K_GGUF](https://huggingface.co/AlicanKiraz0/BaronLLM_Offensive_Security_LLM_Q6_K_GGUF) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens. 


## ollama

You can use [huihui_ai/baronllm-abliterated](https://ollama.com/huihui_ai/baronllm-abliterated) directly, 

```
ollama run huihui_ai/baronllm-abliterated
```





### Donation

If you like it, please click 'like' and follow us for more updates.  
You can follow [x.com/support_huihui](https://x.com/support_huihui) to get the latest model information from huihui.ai.

If you have any questions, insights, or specific ablation models you want to request, please send an email to support@huihui.ai

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin（BTC):
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```

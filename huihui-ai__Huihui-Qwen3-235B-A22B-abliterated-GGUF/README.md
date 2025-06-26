---
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-235B-A22B/blob/main/LICENSE
pipeline_tag: text-generation
base_model:
- Qwen/Qwen3-235B-A22B
tags:
- chat
- abliterated
- uncensored
- GGUF
extra_gated_prompt: >-
    **Usage Warnings**


    “**Risk of Sensitive or Controversial Outputs**“: This model’s safety filtering has been significantly reduced, potentially generating sensitive, controversial, or inappropriate content. Users should exercise caution and rigorously review generated outputs.

    “**Not Suitable for All Audiences**:“ Due to limited content filtering, the model’s outputs may be inappropriate for public settings, underage users, or applications requiring high security.

    “**Legal and Ethical Responsibilities**“: Users must ensure their usage complies with local laws and ethical standards. Generated content may carry legal or ethical risks, and users are solely responsible for any consequences.

    “**Research and Experimental Use**“: It is recommended to use this model for research, testing, or controlled environments, avoiding direct use in production or public-facing commercial applications.

    “**Monitoring and Review Recommendations**“: Users are strongly advised to monitor model outputs in real-time and conduct manual reviews when necessary to prevent the dissemination of inappropriate content.

    “**No Default Safety Guarantees**“: Unlike standard models, this model has not undergone rigorous safety optimization. huihui.ai bears no responsibility for any consequences arising from its use.


---

# huihui-ai/Huihui-Qwen3-235B-A22B-abliterated-GGUF


This is an uncensored version of [Qwen/Qwen3-235B-A22B](https://huggingface.co/Qwen/Qwen3-235B-A22B) created with abliteration (see [remove-refusals-with-transformers](https://github.com/Sumandora/remove-refusals-with-transformers) to know more about it).
This is a crude, proof-of-concept implementation to remove refusals from an LLM model without using TransformerLens. 

## ollama

You can use [huihui_ai/qwen3-abliterated:235b-a22b-Q3_K_M](https://ollama.com/huihui_ai/qwen3-abliterated:235b-a22b-Q3_K_M) directly, 
```
ollama run huihui_ai/qwen3-abliterated:235b-a22b-Q3_K_M
```

### Donation

If you like it, please click 'like' and follow us for more updates.  
You can follow [x.com/support_huihui](https://x.com/support_huihui) to get the latest model information from huihui.ai.

##### Your donation helps us continue our further development and improvement, a cup of coffee can do it.
- bitcoin（BTC):
```
  bc1qqnkhuchxw0zqjh2ku3lu4hq45hc6gy84uk70ge
```
---
license: apache-2.0
datasets:
- Epiculous/SynthRP-Gens-v1.1-Filtered-n-Cleaned
- anthracite-org/stheno-filtered-v1.1
- PJMixers/hieunguyenminh_roleplay-deduped-ShareGPT
- Gryphe/Sonnet3.5-Charcard-Roleplay
- Epiculous/Synthstruct-Gens-v1.1-Filtered-n-Cleaned
- anthracite-org/kalo-opus-instruct-22k-no-refusal
- anthracite-org/nopm_claude_writing_fixed
- anthracite-org/kalo_opus_misc_240827
language:
- en
- fr
- de
- es
- it
- pt
- ru
- zh
- ja
pipeline_tag: text-generation
tags:
- merge
---

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64adfd277b5ff762771e4571/P962FQhRG4I8nbU_DJolY.png)

Now for something a bit different, Violet_Twilight-v0.2! This model is a SLERP merge of Azure_Dusk-v0.2 and Crimson_Dawn-v0.2!

# Quants!
[full](https://huggingface.co/Epiculous/Violet_Twilight-v0.2) / [exl2](https://huggingface.co/Epiculous/Violet_Twilight-v0.2-exl2) / <strong>gguf</strong>

## Prompting
The v0.2 models are trained on ChatML, the prompting structure goes a little something like this:

```
<|im_start|>user
Hi there!<|im_end|>
<|im_start|>assistant
Nice to meet you!<|im_end|>
<|im_start|>user
Can I ask a question?<|im_end|>
<|im_start|>assistant
```

### Context and Instruct
The v0.2 models are trained on ChatML, please use that Context and Instruct template.

### Current Top Sampler Settings
[Smooth Creativity](https://files.catbox.moe/0ihfir.json): Credit to Juelsman for researching this one!<br/>
[Variant Chimera](https://files.catbox.moe/h7vd45.json): Credit to Numbra!<br/>
[Spicy_Temp](https://files.catbox.moe/9npj0z.json) <br/>
[Violet_Twilight-Nitral-Special](https://files.catbox.moe/ot54u3.json) <br/>

## Merging
The following config was used to merge Azure Dusk and Crimson Dawn
```yaml
slices:
  - sources:
      - model: Epiculous/Azure_Dusk-v0.2
        layer_range: [0, 40]
      - model: Epiculous/Crimson_Dawn-V0.2
        layer_range: [0, 40]
merge_method: slerp
base_model: Epiculous/Azure_Dusk-v0.2
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: bfloat16

```
---
base_model: []
library_name: transformers
tags:
- mergekit
- merge

---
# Model

This is a merge model of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Model Details

### Prompt template: Alpaca

```
Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
{prompt}

### Response:

```

## Merge Details
### Merge Method

This model was merged using the SLERP merge method.

### Models Merged

The following models were included in the merge:
* Undi95/Mistral-RP-0.1-7B
* MaziyarPanahi/NSFW_DPO_Noromaid-7b-Mistral-7B-Instruct-v0.1

### Configuration

The following YAML configuration was used to produce this model:

```yaml
slices:
  - sources:
      - model: Undi95/Mistral-RP-0.1-7B
        layer_range: [0, 32]
      - model: MaziyarPanahi/NSFW_DPO_Noromaid-7b-Mistral-7B-Instruct-v0.1
        layer_range: [0, 32]
merge_method: slerp
base_model: Undi95/Mistral-RP-0.1-7B
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5 # fallback for rest of tensors
dtype: bfloat16
```

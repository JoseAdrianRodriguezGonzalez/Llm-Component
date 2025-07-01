
---

tags:
- merge
- mergekit
- lazymergekit
- not-for-all-audiences
- nsfw
- rp
- roleplay
- role-play
license: llama3
language:
- en
pipeline_tag: text-generation
base_model:
- Sao10K/L3-8B-Stheno-v3.2
- ChaoticNeutrals/Poppy_Porpoise-1.0-L3-8B
- Nitral-AI/Hathor_Stable-v0.2-L3-8B
- NeverSleep/Llama-3-Lumimaid-8B-v0.1-OAS
- Hastagaras/Jamet-8B-L3-MK.V-Blackroot
- openlynn/Llama-3-Soliloquy-8B-v2
- NousResearch/Meta-Llama-3-8B-Instruct
- turboderp/llama3-turbcat-instruct-8b
- VAGOsolutions/Llama-3-SauerkrautLM-8b-Instruct
- TIGER-Lab/MAmmoTH2-8B-Plus
- jondurbin/bagel-8b-v1.0
- abacusai/Llama-3-Smaug-8B
- failspy/Meta-Llama-3-8B-Instruct-abliterated-v3
- AwanLLM/Awanllm-Llama-3-8B-Cumulus-v1.0
- lodrick-the-lafted/Limon-8B
- vicgalle/Configurable-Llama-3-8B-v0.3
- Undi95/Llama3-Unholy-8B-OAS
- Undi95/Unholy-8B-DPO-OAS
- WhiteRabbitNeo/Llama-3-WhiteRabbitNeo-8B-v2.0
- migtissera/Tess-2.0-Llama-3-8B
- defog/llama-3-sqlcoder-8b
- HPAI-BSC/Llama3-Aloe-8B-Alpha
- maldv/llama-3-fantasy-writer-8b
- lodrick-the-lafted/Olethros-8B
- Magpie-Align/Llama-3-8B-ShareGPT-112K
- Magpie-Align/Llama-3-8B-WildChat
- Magpie-Align/Llama-3-8B-Tulu-330K
- Magpie-Align/Llama-3-8B-OpenHermes-243K
- Magpie-Align/Llama-3-8B-WizardLM-196K
- Magpie-Align/Llama-3-8B-Ultrachat-200K
- refuelai/Llama-3-Refueled
- Danielbrdz/Barcenas-Llama3-8b-ORPO
- migtissera/Llama-3-8B-Synthia-v3.5
- chujiezheng/Llama-3-Instruct-8B-SimPO-ExPO
- chujiezheng/LLaMA3-iterative-DPO-final-ExPO
- chargoddard/prometheus-2-llama-3-8b

---

![](https://cdn.discordapp.com/attachments/791342238541152306/1264099835221381251/image.png?ex=669ca436&is=669b52b6&hm=129f56187c31e1ed22cbd1bcdbc677a2baeea5090761d2f1a458c8b1ec7cca4b&)

# QuantFactory/L3-Deluxe-Scrambled-Eggs-On-Toast-8B-GGUF
This is quantized version of [Casual-Autopsy/L3-Deluxe-Scrambled-Eggs-On-Toast-8B](https://huggingface.co/Casual-Autopsy/L3-Deluxe-Scrambled-Eggs-On-Toast-8B) created using llama.cpp

# Original Model Card


# L3-Deluxe-Scrambled-Eggs-On-Toast-8B

**L3-Deluxe-Scrambled-Eggs-On-Toast-8B** is a role-play model merger **using 36 models** that was made **in 23 merging steps.**

The goal is to create both a creative and smart model by using gradients.
Each model has their own section in the gradient where they have a larger weight to promote intelligence whereas the rest of the models in the section of the gradient have a small weight to promote creativity.

The following models were used as inspiration:
* [grimjim/kunoichi-lemon-royale-v3-32K-7B](https://huggingface.co/grimjim/kunoichi-lemon-royale-v3-32K-7B)
* [invisietch/EtherealRainbow-v0.3-8B](https://huggingface.co/invisietch/EtherealRainbow-v0.3-8B)
* [PJMixers/LLaMa-3-CursedStock-v2.0-8B](https://huggingface.co/PJMixers/LLaMa-3-CursedStock-v2.0-8B)

## Instruct Format

Llama 3

## Settings/Presets

### Instruct/Context

Virt-io's [SillyTavern Presets](https://huggingface.co/Virt-io/SillyTavern-Presets/tree/main/Prompts/LLAMA-3/v1.9) is recommended.

### Sampler Settings

Here are the current recommended settings for **more creativity**.
```
Top K: 60
Min P: 0.035
Rep Pen: 1.05
Rep Pen Range: 2048
Pres Pen: 0.15
Smoothing Factor: 0.25
Dyna Temp:
  Min Temp: 0.75
  Max Temp: 1.5
  Expo: 0.85
```

No known presets for **more adherencey**. Please recommend some if you can!

## Quants

Weighted quants by:
- [mradermacher](https://huggingface.co/mradermacher/L3-Deluxe-Scrambled-Eggs-On-Toast-8B-i1-GGUF)

Static quants by:
- [mradermacher](https://huggingface.co/mradermacher/L3-Deluxe-Scrambled-Eggs-On-Toast-8B-GGUF)

# Secret Sauce

## Models Used

L3-Scrambled-Eggs-On-Toast-8B is a merge of the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [Sao10K/L3-8B-Stheno-v3.2](https://huggingface.co/Sao10K/L3-8B-Stheno-v3.2)
* [ChaoticNeutrals/Poppy_Porpoise-1.0-L3-8B](https://huggingface.co/ChaoticNeutrals/Poppy_Porpoise-1.0-L3-8B)
* [Nitral-AI/Hathor_Stable-v0.2-L3-8B](https://huggingface.co/Nitral-AI/Hathor_Stable-v0.2-L3-8B)
* [NeverSleep/Llama-3-Lumimaid-8B-v0.1-OAS](https://huggingface.co/NeverSleep/Llama-3-Lumimaid-8B-v0.1-OAS)
* [Hastagaras/Jamet-8B-L3-MK.V-Blackroot](https://huggingface.co/Hastagaras/Jamet-8B-L3-MK.V-Blackroot)
* [openlynn/Llama-3-Soliloquy-8B-v2](https://huggingface.co/openlynn/Llama-3-Soliloquy-8B-v2)
* [NousResearch/Meta-Llama-3-8B-Instruct](https://huggingface.co/NousResearch/Meta-Llama-3-8B-Instruct)
* [turboderp/llama3-turbcat-instruct-8b](https://huggingface.co/turboderp/llama3-turbcat-instruct-8b)
* [VAGOsolutions/Llama-3-SauerkrautLM-8b-Instruct](https://huggingface.co/VAGOsolutions/Llama-3-SauerkrautLM-8b-Instruct)
* [TIGER-Lab/MAmmoTH2-8B-Plus](https://huggingface.co/TIGER-Lab/MAmmoTH2-8B-Plus)
* [jondurbin/bagel-8b-v1.0](https://huggingface.co/jondurbin/bagel-8b-v1.0)
* [abacusai/Llama-3-Smaug-8B](https://huggingface.co/abacusai/Llama-3-Smaug-8B)
* [failspy/Meta-Llama-3-8B-Instruct-abliterated-v3](https://huggingface.co/failspy/Meta-Llama-3-8B-Instruct-abliterated-v3)
* [AwanLLM/Awanllm-Llama-3-8B-Cumulus-v1.0](https://huggingface.co/AwanLLM/Awanllm-Llama-3-8B-Cumulus-v1.0)
* [lodrick-the-lafted/Limon-8B](https://huggingface.co/lodrick-the-lafted/Limon-8B)
* [vicgalle/Configurable-Llama-3-8B-v0.3](https://huggingface.co/vicgalle/Configurable-Llama-3-8B-v0.3)
* [Undi95/Llama3-Unholy-8B-OAS](https://huggingface.co/Undi95/Llama3-Unholy-8B-OAS)
* [Undi95/Unholy-8B-DPO-OAS](https://huggingface.co/Undi95/Unholy-8B-DPO-OAS)
* [WhiteRabbitNeo/Llama-3-WhiteRabbitNeo-8B-v2.0](https://huggingface.co/WhiteRabbitNeo/Llama-3-WhiteRabbitNeo-8B-v2.0)
* [migtissera/Tess-2.0-Llama-3-8B](https://huggingface.co/migtissera/Tess-2.0-Llama-3-8B)
* [defog/llama-3-sqlcoder-8b](https://huggingface.co/defog/llama-3-sqlcoder-8b)
* [HPAI-BSC/Llama3-Aloe-8B-Alpha](https://huggingface.co/HPAI-BSC/Llama3-Aloe-8B-Alpha)
* [maldv/llama-3-fantasy-writer-8b](https://huggingface.co/maldv/llama-3-fantasy-writer-8b)
* [lodrick-the-lafted/Olethros-8B](https://huggingface.co/lodrick-the-lafted/Olethros-8B)
* [Magpie-Align/Llama-3-8B-ShareGPT-112K](https://huggingface.co/Magpie-Align/Llama-3-8B-ShareGPT-112K)
* [Magpie-Align/Llama-3-8B-WildChat](https://huggingface.co/Magpie-Align/Llama-3-8B-WildChat)
* [Magpie-Align/Llama-3-8B-Tulu-330K](https://huggingface.co/Magpie-Align/Llama-3-8B-Tulu-330K)
* [Magpie-Align/Llama-3-8B-OpenHermes-243K](https://huggingface.co/Magpie-Align/Llama-3-8B-OpenHermes-243K)
* [Magpie-Align/Llama-3-8B-WizardLM-196K](https://huggingface.co/Magpie-Align/Llama-3-8B-WizardLM-196K)
* [Magpie-Align/Llama-3-8B-Ultrachat-200K](https://huggingface.co/Magpie-Align/Llama-3-8B-Ultrachat-200K)
* [refuelai/Llama-3-Refueled](https://huggingface.co/refuelai/Llama-3-Refueled)
* [Danielbrdz/Barcenas-Llama3-8b-ORPO](https://huggingface.co/Danielbrdz/Barcenas-Llama3-8b-ORPO)
* [migtissera/Llama-3-8B-Synthia-v3.5](https://huggingface.co/migtissera/Llama-3-8B-Synthia-v3.5)
* [chujiezheng/Llama-3-Instruct-8B-SimPO-ExPO](https://huggingface.co/chujiezheng/Llama-3-Instruct-8B-SimPO-ExPO)
* [chujiezheng/LLaMA3-iterative-DPO-final-ExPO](https://huggingface.co/chujiezheng/LLaMA3-iterative-DPO-final-ExPO)
* [chargoddard/prometheus-2-llama-3-8b](https://huggingface.co/chargoddard/prometheus-2-llama-3-8b)

## YAML Configs Used

The following YAML configs were used to make this mode

### Eggs-and-Bread-RP-pt.1

```yaml
models:
  - model: Sao10K/L3-8B-Stheno-v3.2
  - model: ChaoticNeutrals/Poppy_Porpoise-1.0-L3-8B
    parameters:
      density: 0.5
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
  - model: Nitral-AI/Hathor_Stable-v0.2-L3-8B
    parameters:
      density: 0.5
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: NeverSleep/Llama-3-Lumimaid-8B-v0.1-OAS
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: Hastagaras/Jamet-8B-L3-MK.V-Blackroot
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: openlynn/Llama-3-Soliloquy-8B-v2
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
merge_method: dare_ties
base_model: Sao10K/L3-8B-Stheno-v3.2
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-RP-pt.2

```yaml
models:
  - model: Sao10K/L3-8B-Stheno-v3.2
  - model: ChaoticNeutrals/Poppy_Porpoise-1.0-L3-8B
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
  - model: Nitral-AI/Hathor_Stable-v0.2-L3-8B
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: NeverSleep/Llama-3-Lumimaid-8B-v0.1-OAS
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: Hastagaras/Jamet-8B-L3-MK.V-Blackroot
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: openlynn/Llama-3-Soliloquy-8B-v2
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
merge_method: breadcrumbs_ties
base_model: Sao10K/L3-8B-Stheno-v3.2
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Egg-and-Bread-RP

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-RP-pt.1
  - model: Casual-Autopsy/Eggs-and-Bread-RP-pt.2
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-RP-pt.1
parameters:
  t:
    - filter: self_attn
      value: [0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5]
    - filter: mlp
      value: [0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5]
    - value: 0.5
dtype: bfloat16
```

### Eggs-and-Bread-IQ-pt.1

```yaml
models:
  - model: NousResearch/Meta-Llama-3-8B-Instruct
  - model: turboderp/llama3-turbcat-instruct-8b
    parameters:
      density: 0.5
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
  - model: VAGOsolutions/Llama-3-SauerkrautLM-8b-Instruct
    parameters:
      density: 0.5
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: TIGER-Lab/MAmmoTH2-8B-Plus
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: jondurbin/bagel-8b-v1.0
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: abacusai/Llama-3-Smaug-8B
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
merge_method: dare_ties
base_model: NousResearch/Meta-Llama-3-8B-Instruct
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-IQ-pt.2

```yaml
models:
  - model: NousResearch/Meta-Llama-3-8B-Instruct
  - model: turboderp/llama3-turbcat-instruct-8b
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
  - model: VAGOsolutions/Llama-3-SauerkrautLM-8b-Instruct
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: TIGER-Lab/MAmmoTH2-8B-Plus
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: jondurbin/bagel-8b-v1.0
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: abacusai/Llama-3-Smaug-8B
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
merge_method: breadcrumbs_ties
base_model: NousResearch/Meta-Llama-3-8B-Instruct
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-IQ

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-IQ-pt.1
  - model: Casual-Autopsy/Eggs-and-Bread-IQ-pt.2
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-IQ-pt.1
parameters:
  t:
    - filter: self_attn
      value: [0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5]
    - filter: mlp
      value: [0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5]
    - value: 0.5
dtype: bfloat16
```

### Eggs-and-Bread-Uncen-pt.1

```yaml
models:
  - model: failspy/Meta-Llama-3-8B-Instruct-abliterated-v3
  - model: AwanLLM/Awanllm-Llama-3-8B-Cumulus-v1.0
    parameters:
      density: 0.5
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
  - model: lodrick-the-lafted/Limon-8B
    parameters:
      density: 0.5
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: vicgalle/Configurable-Llama-3-8B-v0.3
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: Undi95/Llama3-Unholy-8B-OAS
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: Undi95/Unholy-8B-DPO-OAS
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
merge_method: dare_ties
base_model: failspy/Meta-Llama-3-8B-Instruct-abliterated-v3
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-Uncen-pt.2

```yaml
models:
  - model: failspy/Meta-Llama-3-8B-Instruct-abliterated-v3
  - model: AwanLLM/Awanllm-Llama-3-8B-Cumulus-v1.0
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
  - model: lodrick-the-lafted/Limon-8B
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: vicgalle/Configurable-Llama-3-8B-v0.3
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: Undi95/Llama3-Unholy-8B-OAS
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: Undi95/Unholy-8B-DPO-OAS
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
merge_method: breadcrumbs_ties
base_model: failspy/Meta-Llama-3-8B-Instruct-abliterated-v3
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-Uncen

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-Uncen-pt.1
  - model: Casual-Autopsy/Eggs-and-Bread-Uncen-pt.2
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-Uncen-pt.1
parameters:
  t:
    - filter: self_attn
      value: [0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5]
    - filter: mlp
      value: [0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5]
    - value: 0.5
dtype: bfloat16
```

### Scrambled-Eggs-On-Toast-1

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-RP
  - model: Casual-Autopsy/Eggs-and-Bread-Uncen
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-RP
parameters:
  t:
    - value: [0.1, 0.15, 0.2, 0.4, 0.6, 0.4, 0.2, 0.15, 0.1]
dtype: bfloat16
```

### L3-Scrambled-Eggs-On-Toast-8B

```yaml
models:
  - model: Casual-Autopsy/Scrambled-Eggs-On-Toast-1
  - model: Casual-Autopsy/Eggs-and-Bread-IQ
merge_method: slerp
base_model: Casual-Autopsy/Scrambled-Eggs-On-Toast-1
parameters:
  t:
    - value: [0.7, 0.5, 0.3, 0.25, 0.2, 0.25, 0.3, 0.5, 0.7]
dtype: bfloat16
```
### Eggs-and-Bread-Misc1-pt.1

```yaml
models:
  - model: WhiteRabbitNeo/Llama-3-WhiteRabbitNeo-8B-v2.0
  - model: migtissera/Tess-2.0-Llama-3-8B
    parameters:
      density: 0.5
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
  - model: defog/llama-3-sqlcoder-8b
    parameters:
      density: 0.5
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: HPAI-BSC/Llama3-Aloe-8B-Alpha
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: maldv/llama-3-fantasy-writer-8b
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: lodrick-the-lafted/Olethros-8B
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
merge_method: dare_ties
base_model: WhiteRabbitNeo/Llama-3-WhiteRabbitNeo-8B-v2.0
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-Misc1-pt.2

```yaml
models:
  - model: WhiteRabbitNeo/Llama-3-WhiteRabbitNeo-8B-v2.0
  - model: migtissera/Tess-2.0-Llama-3-8B
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
  - model: defog/llama-3-sqlcoder-8b
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: HPAI-BSC/Llama3-Aloe-8B-Alpha
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: maldv/llama-3-fantasy-writer-8b
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: lodrick-the-lafted/Olethros-8B
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
merge_method: breadcrumbs_ties
base_model: WhiteRabbitNeo/Llama-3-WhiteRabbitNeo-8B-v2.0
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-Misc1

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-Misc1-pt.1
  - model: Casual-Autopsy/Eggs-and-Bread-Misc1-pt.2
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-Misc1-pt.1
parameters:
  t:
    - filter: self_attn
      value: [0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5]
    - filter: mlp
      value: [0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5]
    - value: 0.5
dtype: bfloat16
```

### Eggs-and-Bread-FFT-pt.1

```yaml
models:
  - model: Magpie-Align/Llama-3-8B-ShareGPT-112K
  - model: Magpie-Align/Llama-3-8B-WildChat
    parameters:
      density: 0.5
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
  - model: Magpie-Align/Llama-3-8B-Tulu-330K
    parameters:
      density: 0.5
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: Magpie-Align/Llama-3-8B-OpenHermes-243K
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: Magpie-Align/Llama-3-8B-WizardLM-196K
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: Magpie-Align/Llama-3-8B-Ultrachat-200K
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
merge_method: dare_ties
base_model: Magpie-Align/Llama-3-8B-ShareGPT-112K
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-FFT-pt.2

```yaml
models:
  - model: Magpie-Align/Llama-3-8B-ShareGPT-112K
  - model: Magpie-Align/Llama-3-8B-WildChat
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
  - model: Magpie-Align/Llama-3-8B-Tulu-330K
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: Magpie-Align/Llama-3-8B-OpenHermes-243K
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: Magpie-Align/Llama-3-8B-WizardLM-196K
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: Magpie-Align/Llama-3-8B-Ultrachat-200K
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
merge_method: breadcrumbs_ties
base_model: Magpie-Align/Llama-3-8B-ShareGPT-112K
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-FFT

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-FFT-pt.1
  - model: Casual-Autopsy/Eggs-and-Bread-FFT-pt.2
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-FFT-pt.1
parameters:
  t:
    - filter: self_attn
      value: [0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5]
    - filter: mlp
      value: [0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5]
    - value: 0.5
dtype: bfloat16
```

### Eggs-and-Bread-Misc2-pt.1

```yaml
models:
  - model: refuelai/Llama-3-Refueled
  - model: Danielbrdz/Barcenas-Llama3-8b-ORPO
    parameters:
      density: 0.5
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
  - model: migtissera/Llama-3-8B-Synthia-v3.5
    parameters:
      density: 0.5
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: chujiezheng/Llama-3-Instruct-8B-SimPO-ExPO
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: chujiezheng/LLaMA3-iterative-DPO-final-ExPO
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: chargoddard/prometheus-2-llama-3-8b
    parameters:
      density: 0.5
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
merge_method: dare_ties
base_model: refuelai/Llama-3-Refueled
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-Misc2-pt.2

```yaml
models:
  - model: refuelai/Llama-3-Refueled
  - model: Danielbrdz/Barcenas-Llama3-8b-ORPO
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.0825, 0.33]
  - model: migtissera/Llama-3-8B-Synthia-v3.5
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.0825, 0.33, 0.0825]
  - model: chujiezheng/Llama-3-Instruct-8B-SimPO-ExPO
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.0825, 0.33, 0.0825, 0.0825]
  - model: chujiezheng/LLaMA3-iterative-DPO-final-ExPO
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.0825, 0.33, 0.0825, 0.0825, 0.0825]
  - model: chargoddard/prometheus-2-llama-3-8b
    parameters:
      gamma: 0.01
      density: 0.9
      weight: [0.33, 0.0825, 0.0825, 0.0825, 0.0825]
merge_method: breadcrumbs_ties
base_model: refuelai/Llama-3-Refueled
parameters:
  normalize: false
  int8_mask: true
dtype: bfloat16
```

### Eggs-and-Bread-Misc2

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-Misc2-pt.1
  - model: Casual-Autopsy/Eggs-and-Bread-Misc2-pt.2
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-Misc2-pt.1
parameters:
  t:
    - filter: self_attn
      value: [0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5]
    - filter: mlp
      value: [0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5, 0.7, 0.3, 0.5, 0.3, 0.7, 0.5]
    - value: 0.5
dtype: bfloat16
```

### Scrambled-Eggs-On-Toast-2

```yaml
models:
  - model: Casual-Autopsy/Eggs-and-Bread-Misc1
  - model: Casual-Autopsy/Eggs-and-Bread-Misc2
merge_method: slerp
base_model: Casual-Autopsy/Eggs-and-Bread-Misc1
parameters:
  t:
    - value: [0.1, 0.15, 0.2, 0.4, 0.6, 0.4, 0.2, 0.15, 0.1]
dtype: bfloat16
```

### Scrambled-Eggs-On-Toast-3

```yaml
models:
  - model: Casual-Autopsy/Scrambled-Eggs-On-Toast-2
  - model: Casual-Autopsy/Eggs-and-Bread-FFT
merge_method: slerp
base_model: Casual-Autopsy/Scrambled-Eggs-On-Toast-2
parameters:
  t:
    - value: [0.7, 0.5, 0.3, 0.25, 0.2, 0.25, 0.3, 0.5, 0.7]
dtype: bfloat16
```

### L3-Deluxe-Scrambled-Eggs-On-Toast-8B

```yaml
models:
  - model: Casual-Autopsy/L3-Scrambled-Eggs-On-Toast-8B
  - model: Casual-Autopsy/Scrambled-Eggs-On-Toast-3
merge_method: slerp
base_model: Casual-Autopsy/L3-Scrambled-Eggs-On-Toast-8B
parameters:
  t:
    - value: [0.2, 0.25, 0.3, 0.4, 0.3, 0.25, 0.2, 0.25, 0.3, 0.4, 0.3, 0.25, 0.2]
dtype: bfloat16
```

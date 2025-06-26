---
base_model:
- Steelskull/L3.3-Electra-R1-70b
pipeline_tag: text-generation
library_name: transformers
quantized_by: ddh0
---

# Steelskull/L3.3-Electra-R1-70b-GGUF

This repo provides several GGUF imatrix quantizations of [Steelskull/L3.3-Electra-R1-70b](https://huggingface.co/Steelskull/L3.3-Electra-R1-70b).

#### Quantizations (worst to best)
- IQ2_M
- IQ3_XS
- IQ3_M
- Q4_K_S
- IQ4_XS
- Q4_K_M
- Q5_K_S
- Q5_K_M
- Q6_K
- Q8_0

The imatrix was generated using the same calibration data as Bartowski, and both the calibration data as well as the imatrix itself are provided here.
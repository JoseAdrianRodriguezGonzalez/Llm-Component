---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: deepseek-ai/DeepSeek-R1-0528
license: mit
base_model_relation: quantized
tags:
- mla
- imatrix
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix MLA Quantizations of DeepSeek-R1-0528
This quant collection **REQUIRES** [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/) fork to support advanced non-linear SotA quants and Multi-Head Latent Attention (MLA). Do **not** download these big files and expect them to run on mainline vanilla llama.cpp, ollama, LM Studio, KoboldCpp, etc!

These quants provide best in class perplexity for the given memory footprint. MLA support allows 32k+ context length in under 24GB GPU VRAM for `R1` and `V3` while offloading MoE layers to RAM.

These quants are specifically designed for CPU+GPU systems with under 16GB or 24GB VRAM as well as also CPU *only* rigs using dynamic quant repacking (for maximum memory throughput). If you have more VRAM, you can now load `_R4` repacked quants onto GPUs as of [ik_llama.cpp PR462](https://github.com/ikawrakow/ik_llama.cpp/pull/462). So these quants are good for multi-GPU setups as well now!

You could try `ik_llama.cpp` quickly with your *existing* quants, as it computes MLA tensors and repacks quants on the fly at startup (if you have enough RAM+VRAM to fit entire model). Then come check out these fat quants here once you see the difference.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community here and on `r/LocalLLaMA` for tips and tricks helping each other run all the fun new models!

Excited to share and learn together. Thanks!

## Quant Collection
So far these are my best recipes offering the lowest perplexity per GiB models suitable for a wide variety of CPU+GPU or CPU *only* rigs.

![Perplexity Chart](images/perplexity.png "Chart showing Perplexity improving as BPW increases.")

* `DeepSeek-R1-0528-Q8_0` 666GiB
  - `Final estimate: PPL = 3.2130 +/- 0.01698`
  - I didn't upload this, it is for baseline reference only.
* `DeepSeek-R1-0528-IQ4_KS_R4` 368GiB
  - `Final estimate: PPL = 3.2286 +/- 0.01710`
  - Fits 32k context in under 24GiB VRAM
* `DeepSeek-R1-0528-IQ3_K_R4` 301GiB
  - `Final estimate: PPL = 3.2730 +/- 0.01738`
  - Fits 32k context in under 24GiB VRAM
* `DeepSeek-R1-0528-IQ2_K_R4` 220GiB
  - `Final estimate: PPL = 3.5069 +/- 0.01893`
  - Fits 32k context in under 16GiB VRAM
  - Fits 64k context in under 24GiB VRAM
* `DeepSeek-R1-0528-IQ1_S_R4` 131GiB
  - `Final estimate: PPL = 4.8805 +/- 0.02876`
  - The world's smallest working DeepSeek-R1-0528 Quant!
  - Run on AM5 class gaming rig with 2x64GB DDR5 DIMM kit and single GPU!
  - Support for this is bleeding edge you need [PR494](https://github.com/ikawrakow/ik_llama.cpp/pull/494)
  - Fits 32k+ context in under 16GiB VRAM
  - Should fit in 128GiB RAM + 24GB VRAM by offloading layers to GPU.
  - "Only for the desperate."
  - Technically "better" (lower) PPL than `Qwen3-235B-A22B-Q8_0 @ ~5.31` though you can't really make comparisons like this.

#### `IQ4_KS_R4` 4.701 BPW (368GiB)
Special mix `IQ5_KS_R4` `ffn_down` and `IQ4_KS_R4` `ffn_(up|gate)` routed experts. All other layers `q8_0` for CPU+GPU offload. For max speed on CPU *only* rigs use `--run-time-repack`.

<details>

<summary>👈 Secret Recipe</summary>

This quant might be fairly fast despite the larger size given `_KS` quant inferencing optimizations. Made this as there were some requests for a larger size. This on *might* fit on 368GB RAM if you have more than average VRAM, or comfortably on a 512GB RAM rig preferably with 24GB VRAM though fine for CPU only as well.

```bash
#!/usr/bin/env bash

custom="
# Token embedding and output tensors (GPU)
token_embd\.weight=q8_0
output\.weight=q8_0
output_norm\.weight=q8_0

# First 3 dense layers (0-3) (GPU)
blk\.[0-2]\..*=q8_0

# All attention, weights, and bias tensors for MoE layers (3-60) (GPU)
blk\.[3-9]\.attn_.*=q8_0
blk\.[1-5][0-9]\.attn_.*=q8_0
blk\.60\.attn_.*=q8_0

blk\.[3-9]\.ffn_norm\.weight=q8_0
blk\.[1-5][0-9]\.ffn_norm\.weight=q8_0
blk\.60\.ffn_norm\.weight=q8_0

blk\.[3-9]\.exp_probs_b\.bias=q8_0
blk\.[1-5][0-9]\.exp_probs_b\.bias=q8_0
blk\.60\.exp_probs_b\.bias=q8_0

# Shared Experts (3-60) (GPU)
blk\.[3-9]\.ffn_down_shexp\.weight=q8_0
blk\.[1-5][0-9]\.ffn_down_shexp\.weight=q8_0
blk\.60\.ffn_down_shexp\.weight=q8_0

blk\.[3-9]\.ffn_(gate|up)_shexp\.weight=q8_0
blk\.[1-5][0-9]\.ffn_(gate|up)_shexp\.weight=q8_0
blk\.60\.ffn_(gate|up)_shexp\.weight=q8_0

# MoE Experts (3-60) (CPU)
blk\.[3-9]\.ffn_down_exps\.weight=iq5_ks_r4
blk\.[1-5][0-9]\.ffn_down_exps\.weight=iq5_ks_r4
blk\.60\.ffn_down_exps\.weight=iq5_ks_r4

blk\.[3-9]\.ffn_(gate|up)_exps\.weight=iq4_ks_r4
blk\.[1-5][0-9]\.ffn_(gate|up)_exps\.weight=iq4_ks_r4
blk\.60\.ffn_(gate|up)_exps\.weight=iq4_ks_r4
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/imatrix-DeepSeek-R1-0528.dat \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-256x21B-0528-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ4_KS_R4.gguf \
    IQ4_KS_R4 \
    24
```

</details>

#### `IQ3_K_R4` 3.847 BPW (301GiB)
Special mix `IQ4_KS_R4` `ffn_down` and `IQ3_K_R4` `ffn_(up|gate)` routed experts. All other layers `q8_0` for CPU+GPU offload. For max speed on CPU *only* rigs use `--run-time-repack`.

<details>

<summary>👈 Possible VRAM & RAM Combinations</summary>

This is probably a good size quant for a 368GB RAM rig preferably with at least a single 24GB VRAM GPU.
It is probably a little out of reach for a 256GB RAM rig unless you have 80+GB VRAM.
You could still run "troll rig" style and page off disk for maybe 5 tok/sec and some hot NVMe drives hahah...

I'm still testing this out, but initial test am seeing ~12 tok/sec with 256GB RAM and 2x RTX A6000 48GB VRAM on 24x Thread Ripper Pro rig. Can probably get more by offloading a couple more layers.

Feel free to report in the comments section your configuration for others to see too. Thanks!

```bash
    --n-gpu-layers 63 \
    -ot "blk\.(3|4|5|6|7)\.ffn_.*=CUDA0" \
    -ot "blk\.(8|9|10|11|12)\.ffn_.*=CUDA1" \
    --override-tensor exps=CPU \

llm_load_tensors:        CPU buffer size = 252646.07 MiB
llm_load_tensors:        CPU buffer size =   938.98 MiB
llm_load_tensors:      CUDA0 buffer size = 33753.38 MiB
llm_load_tensors:      CUDA1 buffer size = 33900.64 MiB
...
llama_kv_cache_init:      CUDA0 KV buffer size =   592.89 MiB
llama_kv_cache_init:      CUDA1 KV buffer size =   573.76 MiB
llama_new_context_with_model: KV self size  = 1166.62 MiB, c^KV (q8_0): 1166.62 MiB, kv^T: not used
llama_new_context_with_model:  CUDA_Host  output buffer size =     0.99 MiB
llama_new_context_with_model: pipeline parallelism enabled (n_copies=1)
llama_new_context_with_model:      CUDA0 compute buffer size =  3425.00 MiB
llama_new_context_with_model:      CUDA1 compute buffer size =  3386.00 MiB
llama_new_context_with_model:  CUDA_Host compute buffer size =    78.01 MiB
```

</details>

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# Token embedding and output tensors (GPU)
token_embd\.weight=q8_0
output\.weight=q8_0
output_norm\.weight=q8_0

# First 3 dense layers (0-3) (GPU)
blk\.[0-2]\..*=q8_0

# All attention, weights, and bias tensors for MoE layers (3-60) (GPU)
blk\.[3-9]\.attn_.*=q8_0
blk\.[1-5][0-9]\.attn_.*=q8_0
blk\.60\.attn_.*=q8_0

blk\.[3-9]\.ffn_norm\.weight=q8_0
blk\.[1-5][0-9]\.ffn_norm\.weight=q8_0
blk\.60\.ffn_norm\.weight=q8_0

blk\.[3-9]\.exp_probs_b\.bias=q8_0
blk\.[1-5][0-9]\.exp_probs_b\.bias=q8_0
blk\.60\.exp_probs_b\.bias=q8_0

# Shared Experts (3-60) (GPU)
blk\.[3-9]\.ffn_down_shexp\.weight=q8_0
blk\.[1-5][0-9]\.ffn_down_shexp\.weight=q8_0
blk\.60\.ffn_down_shexp\.weight=q8_0

blk\.[3-9]\.ffn_(gate|up)_shexp\.weight=q8_0
blk\.[1-5][0-9]\.ffn_(gate|up)_shexp\.weight=q8_0
blk\.60\.ffn_(gate|up)_shexp\.weight=q8_0

# MoE Experts (3-60) (CPU)
blk\.[3-9]\.ffn_down_exps\.weight=iq4_ks_r4
blk\.[1-5][0-9]\.ffn_down_exps\.weight=iq4_ks_r4
blk\.60\.ffn_down_exps\.weight=iq4_ks_r4

blk\.[3-9]\.ffn_(gate|up)_exps\.weight=iq3_k_r4
blk\.[1-5][0-9]\.ffn_(gate|up)_exps\.weight=iq3_k_r4
blk\.60\.ffn_(gate|up)_exps\.weight=iq3_k_r4
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/imatrix-DeepSeek-R1-0528.dat \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-256x21B-0528-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ3_K_R4.gguf \
    IQ3_K_R4 \
    24
```

</details>

#### `IQ2_K_R4` 2.799 BPW (220GiB)
Special mix `IQ3_K_R4` `ffn_down` and `IQ2_K_R4` `ffn_(up|gate)` routed experts. All other layers *roughly* `iq5_ks` for CPU+GPU offload. For max speed on CPU *only* rigs use `--run-time-repack` or manually ofline repack if you want to mmap() off disk.

Can fit 32k context in under 16GB VRAM and getting almost 15 tok/sec in early testing! Could go faster offloading more exps layers!

<details>

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

# Notes:
# https://github.com/ikawrakow/ik_llama.cpp/issues/296#issuecomment-2765210993
# https://github.com/ikawrakow/ik_llama.cpp/issues/296#issuecomment-2768567062
custom="
# Token embedding and output tensors (GPU)
# note token_embd cannot be repacked quant type
token_embd\.weight=iq5_ks
output\.weight=iq5_ks
output_norm\.weight=iq5_ks

# First 3 dense layers (0-3) (GPU)
# Except blk.*.attn_k_b.weight is not divisible by 256 so only supports qN_0
blk\.[0-2]\.attn_k_b.*=q5_0
blk\.[0-2]\.attn_.*=iq5_ks
blk\.[0-2]\..*=iq5_ks

# All attention, norm weights, and bias tensors for MoE layers (3-60) (GPU)
# Except blk.*.attn_k_b.weight is not divisible by 256 so only supports qN_0
blk\.[3-9]\.attn_k_b.*=q5_0
blk\.[1-5][0-9]\.attn_k_b.*=q5_0
blk\.60\.attn_k_b.*=q5_0

blk\.[3-9]\.attn_.*=iq5_ks
blk\.[1-5][0-9]\.attn_.*=iq5_ks
blk\.60\.attn_.*=iq5_ks

blk\.[3-9]\.ffn_norm\.weight=iq5_ks
blk\.[1-5][0-9]\.ffn_norm\.weight=iq5_ks
blk\.60\.ffn_norm\.weight=iq5_ks

blk\.[3-9]\.exp_probs_b\.bias=iq5_ks
blk\.[1-5][0-9]\.exp_probs_b\.bias=iq5_ks
blk\.60\.exp_probs_b\.bias=iq5_ks

# Shared Experts (3-60) (GPU)
blk\.[3-9]\.ffn_down_shexp\.weight=iq5_ks
blk\.[1-5][0-9]\.ffn_down_shexp\.weight=iq5_ks
blk\.60\.ffn_down_shexp\.weight=iq5_ks

blk\.[3-9]\.ffn_(gate|up)_shexp\.weight=iq4_ks
blk\.[1-5][0-9]\.ffn_(gate|up)_shexp\.weight=iq4_ks
blk\.60\.ffn_(gate|up)_shexp\.weight=iq4_ks

# Routed Experts (3-60) (CPU)
blk\.[3-9]\.ffn_down_exps\.weight=iq3_k_r4
blk\.[1-5][0-9]\.ffn_down_exps\.weight=iq3_k_r4
blk\.60\.ffn_down_exps\.weight=iq3_k_r4

blk\.[3-9]\.ffn_(gate|up)_exps\.weight=iq2_k_r4
blk\.[1-5][0-9]\.ffn_(gate|up)_exps\.weight=iq2_k_r4
blk\.60\.ffn_(gate|up)_exps\.weight=iq2_k_r4
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/imatrix-DeepSeek-R1-0528.dat \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-256x21B-0528-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ2_K_R4.gguf \
    IQ2_K_R4 \
    24
```

</details>

#### `IQ2_KT` Not Yet Released
I might release my `iq2_kt` "QTIP/exl3/trellis" style quant, but it is rather experimental and the inferencing implementation needs more time to bake. Quality wise it is slightly smaller than the above `IQ2_K_R4` with slightly worse perplexity and KLD.

#### `IQ1_S_R4` 130.203 GiB (1.664 BPW)

The world's smallest working DeepSeek-R1-0528 quant!

![KLD Smol Boi Comparison](images/kld-r1-0528-smol-bois.png "Chart showing competitive KLD quality of smallest R1-0528 quants.")
The Delta P numbers for average RMS, 99% percentile, and absolute max divergence from the baseline pure `Q8_0`. Lower is better.

If you can fit a larger model completely in RAM+VRAM I would recommend that, but if you have 128GB RAM + 24GB VRAM then give this a try as it is surprisingly usable despite heavy quantization.

Support for this is bleeding edge you need [PR494](https://github.com/ikawrakow/ik_llama.cpp/pull/494)!

Special mix `IQ1_M_R4` `ffn_down` and `IQ1_S_R4` `ffn_(up|gate)` routed experts. All other layers mostly `iq4_ks` for CPU+GPU offload. For max speed on CPU *only* rigs use `--run-time-repack` (only appleis to the `iq4_ks` tensors etc.).

Also released [ubergarm/DeepSeek-V3-0324-IQ1_S_R4](https://huggingface.co/ubergarm/DeepSeek-V3-0324-GGUF/tree/main/DeepSeek-V3-0324-IQ1_S_R4) with the same recipe and size if you don't want thinking.

<details>

<summary>👈 How to run in 128GiB RAM + 24GB VRAM</summary>

Thanks for all the help and feedback to figure this out and so I uploaded the non `_R4` variant which *does* allow for GPU offload to run.

A lot of [good discussion](https://huggingface.co/ubergarm/DeepSeek-R1-0528-GGUF/discussions/6#683fbbb9c43f1c9609843e08) on [running this quant](https://github.com/ikawrakow/ik_llama.cpp/discussions/477#discussioncomment-13361099).

Keep in mind if you can fit the next size up it will likely actually run faster as it has more optimized quant types.

This will fit in ~116.1GiB RAM plus 22448MiB VRAM. You can strip it down more and get another layer on GPU possibly too or increase context. Good luck!
```bash
# You can use more CUDA devices just set them all visibile and do *not* use `-ts ...` with this `-ot ...` strategy.
CUDA_VISIBLE_DEVICES="0" \
./build/bin/llama-server \
    --model /mnt/raid/hf/DeepSeek-R1-0528-GGUF/IQ1_S_R4/DeepSeek-R1-0528-IQ1_S_R4-00001-of-00003.gguf \
    --alias ubergarm/DeepSeek-R1-0528-IQ1_S_R4 \
    --ctx-size 32768 \
    -ctk q8_0 \
    -mla 3 -fa \
    -amb 256 \
    -fmoe \
    --n-gpu-layers 99 \
    -ot "blk\.(3|4|5|6)\.ffn_.*=CUDA0" \
    --override-tensor exps=CPU \
    -rtr \
    --parallel 1 \
    --threads 24 \
    --host 127.0.0.1 \
    --port 8080

llm_load_tensors:        CPU buffer size = 117936.00 MiB
llm_load_tensors:  CUDA_Host buffer size =   469.99 MiB
llm_load_tensors:      CUDA0 buffer size = 17851.01 MiB
....................................................................................................
llama_kv_cache_init:      CUDA0 KV buffer size =  2196.00 MiB
llama_new_context_with_model: KV self size  = 2196.00 MiB, c^KV (f16): 2196.00 MiB, kv^T: not used
llama_new_context_with_model:  CUDA_Host  output buffer size =     0.99 MiB
llama_new_context_with_model:      CUDA0 compute buffer size =  3041.00 MiB
llama_new_context_with_model:  CUDA_Host compute buffer size =    78.01 MiB
```

</details>

<details>

![Reverse Buff Mokey Meme](images/buff-mokey-meme.png "Reverse Buff Mokey Meme Comparing full R1-671B fp8 to smol iq1_s_r4 quant.")

Possibly useful for 128GiB RAM + 16GB+ VRAM? Maybe? It does actually work and can read python code okay. For all I know it might be better than Qwen3-235B-A22B given the iq1_s_r4 actually has lower PPL!

Not recommended and slower than a larger quant unless this is the *only* thing you can fit completely in RAM+VRAM as this quant seems slower and less optimized for inferencing and in testing has slower TG and worse quality (higher perplexity). Plus I'm not sure that you can use it with multi-GPU offload so check the ik_llama.cpp PRs as these tiny quants are less used.

I recommend to *not* use the `IQ1_S` so use the `IQ1_S_R4` now with the recent updates supporting GPU offload and better speeds with the repacked quant on CUDA.

<summary>👈 Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# Token embedding and output tensors (GPU)
# note token_embd cannot be repacked quant type
token_embd\.weight=iq4_ks
output\.weight=iq4_ks
output_norm\.weight=iq4_ks

# First 3 dense layers (0-3) (GPU)
# Except blk.*.attn_k_b.weight is not divisible by 256 so only supports qN_0
blk\.[0-2]\.attn_k_b.*=q4_0
blk\.[0-2]\.attn_.*=iq4_ks
blk\.[0-2]\..*=iq4_ks

# All attention, norm weights, and bias tensors for MoE layers (3-60) (GPU)
# Except blk.*.attn_k_b.weight is not divisible by 256 so only supports qN_0
blk\.[3-9]\.attn_k_b.*=q4_0
blk\.[1-5][0-9]\.attn_k_b.*=q4_0
blk\.60\.attn_k_b.*=q4_0

blk\.[3-9]\.attn_.*=iq4_ks
blk\.[1-5][0-9]\.attn_.*=iq4_ks
blk\.60\.attn_.*=iq4_ks

blk\.[3-9]\.ffn_norm\.weight=iq4_ks
blk\.[1-5][0-9]\.ffn_norm\.weight=iq4_ks
blk\.60\.ffn_norm\.weight=iq4_ks

blk\.[3-9]\.exp_probs_b\.bias=iq4_ks
blk\.[1-5][0-9]\.exp_probs_b\.bias=iq4_ks
blk\.60\.exp_probs_b\.bias=iq4_ks

# Shared Experts (3-60) (GPU)
blk\.[3-9]\.ffn_down_shexp\.weight=iq4_ks
blk\.[1-5][0-9]\.ffn_down_shexp\.weight=iq4_ks
blk\.60\.ffn_down_shexp\.weight=iq4_ks

blk\.[3-9]\.ffn_(gate|up)_shexp\.weight=iq4_ks
blk\.[1-5][0-9]\.ffn_(gate|up)_shexp\.weight=iq4_ks
blk\.60\.ffn_(gate|up)_shexp\.weight=iq4_ks

# Routed Experts (3-60) (CPU)
blk\.[3-9]\.ffn_down_exps\.weight=iq1_m_r4
blk\.[1-5][0-9]\.ffn_down_exps\.weight=iq1_m_r4
blk\.60\.ffn_down_exps\.weight=iq1_m_r4

blk\.[3-9]\.ffn_(gate|up)_exps\.weight=iq1_s_r4
blk\.[1-5][0-9]\.ffn_(gate|up)_exps\.weight=iq1_s_r4
blk\.60\.ffn_(gate|up)_exps\.weight=iq1_s_r4
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/imatrix-DeepSeek-R1-0528.dat \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-256x21B-0528-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ1_S_R4.gguf \
    IQ1_S_R4 \
    24
```

</details>


## Quick Start
#### `ik_llama.cpp` API server for GPU+CPU
```bash
# Fits 32k context in under 24GB VRAM
# Optional `-ser 6,1` improves speed at some cost to quality
# Recommended sampling: --temp 0.6 --top-p 0.95
CUDA_VISIBLE_DEVICES="0," \
./build/bin/llama-server \
    --model /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ3_K_R4.gguf \
    --alias ubergarm/DeepSeek-R1-0528-IQ3_K_R4 \
    --ctx-size 32768 \
    -ctk q8_0 \
    -mla 3 -fa \
    -amb 512 \
    -fmoe \
    --n-gpu-layers 63 \
    --override-tensor exps=CPU \
    --parallel 1 \
    --threads 16 \
    --host 127.0.0.1 \
    --port 8080
```

#### `ik_llama.cpp` API server for MultiGPU(+CPU)
```bash
# Adjust number of routed expert layers for additional VRAM on each GPU
# Compile with -DGGML_SCHED_MAX_COPIES=1 for multi-GPUs
# Compile with -DGGML_CUDA_IQK_FORCE_BF16=1 if putting `_R4` tensors on GPU (for DeepSeek only)
# (might go faster or slower with FORCE_BF16 depending on GPU model)
# If you have extra VRAM go with `-b 4096 -ub 4096` for potential big PP gains!
./build/bin/llama-server \
    --model /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ3_K_R4.gguf \
    --alias ubergarm/DeepSeek-R1-0528-IQ3_K_R4 \
    --ctx-size 32768 \
    -ctk q8_0 \
    -mla 3 -fa \
    -amb 512 \
    -fmoe \
    --n-gpu-layers 63 \
    -ot "blk\.(3|4)\.ffn_.*=CUDA0" \
    -ot "blk\.(5|6)\.ffn_.*=CUDA1" \
    --override-tensor exps=CPU \
    --parallel 1 \
    --threads 16 \
    --host 127.0.0.1 \
    --port 8080
```

#### `ik_llama.cpp` API server for CPU *only*
```
# The goal for now is as much RAM bandwidth in a single NUMA node e.g.
# Use BIOS `NPS0` on AMD Epyc or single socket of Intel Xeon in BIOS `SNC=Disable` & Snoop Interleave
# Tune your `--threads` for token generation, and `--threads-batch` for prompt processing (prefill)
# Note `--run-time-repack` will pre-allocate enough RAM for model weights instead of mmap()'ing off disk
# Note there are options for both Explicit and Transparent Huge Pages with tuning discussions in [git repo](https://github.com/ikawrakow/ik_llama.cpp/pull/278#issuecomment-2746381515)
numactl -N 0 -m 0 \
./build/bin/llama-server \
    --model /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ3_K_R4.gguf \
    --alias ubergarm/DeepSeek-R1-0528-IQ3_K_R4 \
    --run-time-repack \
    --ctx-size 65536 \
    -ctk q8_0 \
    -mla 3 -fa \
    -amb 512 \
    -fmoe \
    --parallel 1 \
    --threads 88 \
    --threads-batch 128 \
    --numa numactl \
    --host 127.0.0.1 \
    --port 8080
```

## Quant Comparisons
Check out [The Great Quant Wars of 2025](https://www.reddit.com/r/LocalLLaMA/comments/1khwxal/the_great_quant_wars_of_2025/)
r/LocalLLaMA post for some more discussion on quantization and
methodology.

#### imatrix

<details>

<summary>Importance Matrix Details Here</summary>

This time I threw in extra material from [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3/tree/master/exllamav3/conversion/standard_cal_data)'s
`standard_cal_data` in addition to my usual `calibration_data_v5_rc.txt` linked below.

```bash
cat calibration_data_v5_rc.txt > ubergarm-imatrix-calibration-corpus-v02.txt
cat c4.utf8 >> ubergarm-imatrix-calibration-corpus-v02.txt
cat code.utf8 >> ubergarm-imatrix-calibration-corpus-v02.txt
cat multilingual.utf8 >> ubergarm-imatrix-calibration-corpus-v02.txt
cat technical.utf8 >> ubergarm-imatrix-calibration-corpus-v02.txt
cat tiny.utf8 >> ubergarm-imatrix-calibration-corpus-v02.txt
# Do *not* use the wiki.utf8 to avoid potential over-fitting on wiki.test.raw common test corpus
# 1.7MiB total size of ubergarm-imatrix-calibration-corpus-v02.txt

./build/bin/llama-imatrix \
    -m /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-Q8_0.gguf \
    -f ubergarm-imatrix-calibration-corpus-v02.txt \
    -o /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/imatrix-DeepSeek-R1-0528.dat \
    --verbosity 1 \
    --ctx-size 512 \
    --layer-similarity \
    --threads 128
```

</details>

#### Perplexity

I use the `Q8_0` without imatrix as the baseline against `wiki.test.raw`:

<details>

<summary>👈 Perplexity Logs</summary>

```bash
$ ./build/bin/llama-perplexity \
    --model /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ3_K_R4.gguf \
    -f wiki.test.raw \
    --seed 1337 \
    --ctx-size 512 \
    -mla 3 -fa \
    -amb 512 \
    -fmoe \
    --n-gpu-layers 63 \
    -ot "blk\.(3|4|5|6|7|8)\.ffn_.*=CUDA0" \
    -ot "blk\.(9|10|11|12|13)\.ffn_.*=CUDA1" \
    --override-tensor exps=CPU \
    --threads 24

Final estimate: PPL = 3.2730 +/- 0.01738
```

</details>

#### Split

<details>

<summary>👈 Split GGUF</summary>

*TODO*: Add key value metadata information before publishing.

```bash
$ ./build/bin/llama-gguf-split \
    --dry-run \
    --split \
    --split-max-size 50G \
    /mnt/raid/models/ubergarm/DeepSeek-R1-0528-GGUF/DeepSeek-R1-0528-IQ3_K_R4.gguf
    /mnt/raid/hf/DeepSeek-R1-0528-GGUF/IQ3_K_R4/DeepSeek-R1-0528-IQ3_K_R4
```

</details>

## References
* [ik_llama.cpp DeepSeek-R1-0528 Discussion](https://github.com/ikawrakow/ik_llama.cpp/discussions/477)
* [turboderp-org/exllamav3](https://github.com/turboderp-org/exllamav3/pull/26)
* [imatrix calibration_data_v5_rc.txt](https://gist.github.com/tristandruyen/9e207a95c7d75ddf37525d353e00659c#file-calibration_data_v5_rc-txt)

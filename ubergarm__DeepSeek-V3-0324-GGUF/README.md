---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: deepseek-ai/DeepSeek-V3-0324
license: mit
base_model_relation: quantized
tags:
- mla
- imatrix
- deepseek_v3
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix MLA Quantizations of DeepSeek-V3-0324

This quant collection **REQUIRES** [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/) fork to support advanced non-linear SotA quants and Multi-Head Latent Attention (MLA). Do **not** download these big files and expect them to run on mainline vanilla llama.cpp, ollama, LM Studio, KoboldCpp, etc!

These quants provide best in class perplexity for the given memory footprint. MLA support allows 32k+ context length in under 24GB GPU VRAM for `R1` and `V3` while offloading MoE layers to RAM.

These quants are specifically designed for CPU+GPU systems with 24-48GB VRAM, and also CPU *only* rigs using dynamic quant repacking (for maximum memory throughput). If you have more VRAM, I suggest a different quant with at least some routed expert layers optimized for GPU offload.

You could try `ik_llama.cpp` quickly with your *existing* quants, as it computes MLA tensors and repacks quants on the fly at startup (if you have enough RAM+VRAM to fit entire model). Then come check out these fat quants here once you see the difference.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community here and on `r/LocalLLaMA` for tips and tricks helping each other run all the fun new models!

Excited to share and learn together. Thanks!

## Quant Collection
So far these are my best recipes offering the lowest perplexity per GiB models suitable for a wide variety of CPU+GPU or CPU *only* rigs.

#### `IQ4_K_R4` 4.936 BPW
Special mix `IQ5_K_R4`/`IQ4_K_R4` routed experts with all other layers full `q8_0` for CPU+GPU offload or `--run-time-repack` for max speed CPU *only* rigs.
Great for big 384+ GB RAM rig with 24GB+ GPU

#### `IQ2_K_R4` 2.889 BPW
Special mix `IQ3_K_R4`/`IQ2_K_R4` routed experts with all other layers full `q8_0` for CPU+GPU offload or `--run-time-repack` for max speed CPU *only* rigs.
Great for CPU+GPU "troll rig" high end gamer systems e.g. 9950X 96 GB RAM + 3090TI 24 GB VRAM + Gen 5 NVMe SSD.

#### `IQ1_S_R4` 130.203 GiB 1.664 BPW
Special mix `IQ1_M_R4`/`IQ1_S_R4` routed experts with all other layers `iq4_ks` for CPU+GPU offload or `--run-time-repack` for max speed CPU *only* rigs.
Great for CPU+GPU "troll rig" high end gamer systems e.g. 2x 64GiB DDR5 plus 24GB VRAM.

#### Custom Mixes
If you have more than 48GB VRAM across multiple GPUs, consider rolling your own custom quants to optimize size and performance with whatever hardware you have using custom `-ot` expression. If you have less VRAM, you could make a custom quant leaner in the non routed expert layers or get 64k+ context in 24GB VRAM. Also you can use the offline repack tool if you want to do CPU only with `mmap()` still enabled.

## Quick Start
#### `ik_llama.cpp` API server for GPU+CPU
```bash
# Fits 32k context in under 24GB VRAM
# Optional `-ser 6,1` improves speed at minimal cost to quality
CUDA_VISIBLE_DEVICES="0," \
./build/bin/llama-server \
    --model /mnt/raid/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-IQ2_K_R4.gguf \
    --alias ubergarm/DeepSeek-R1-V3-0324-IQ2_K_R4 \
    --ctx-size 32768 \
    -ctk q8_0 \
    -mla 2 -fa \
    -amb 512 \
    -fmoe \
    --temp 0.3 \
    --min-p 0.05 \
    --n-gpu-layers 63 \
    --override-tensor exps=CPU \
    --parallel 1 \
    --threads 16 \
    --host 127.0.0.1 \
    --port 8080
```

#### `ik_llama.cpp` API server for CPU *only*
```
# The goal for now is as much RAM bandwidth in a single NUMA node e.g.
# Use BIOS `NPS0` on AMD Epyc or single socket of Intel Xeon in BIOS `SNC=Disable`
# Tune your `--threads` for token generation, and `--threads-batch` for prompt processing (prefill)
# Note `--run-time-repack` will pre-allocate enough RAM for model weights instead of mmap()'ing off disk
# Note there are options for both Explicit and Transparent Huge Pages with tuning discussions in [git repo](https://github.com/ikawrakow/ik_llama.cpp/pull/278#issuecomment-2746381515)
numactl -N 0 -m 0 \
./build/bin/llama-server \
    --model /mnt/ai/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-IQ4_K_R4.gguf \
    --alias ubergarm/DeepSeek-V3-0324-IQ4_K_R4 \
    --run-time-repack \
    --ctx-size 65536 \
    -ctk q8_0 \
    -mla 3 -fa \
    -amb 512 \
    -fmoe \
    --temp 0.3 \
    --min-p 0.05 \
    --parallel 1 \
    --threads 88 \
    --threads-batch 128 \
    --numa numactl \
    --host 127.0.0.1 \
    --port 8080
```

## Quant Comparisons

These are probably among the **best quants available in this size class** for `V3-0324`!

![Benchmarks showing these quants are smaller in size yet similar in performance to the `Q8_0`](images/benchmarks-01.png "Benchmarks showing these quants are smaller in size yet similar in performance to the `Q8_0`")

![VRAM Usage Chart](images/vram-usage.png "Chart showing linear VRAM usage vs context length.")

ubergarm made no sacrifices for token embedding, attention, dense
layers, or shared experts. This is possible because `ik_llama.cpp` MLA
implementation saves so much GPU VRAM enabling 32k context in under 24GB
VRAM. Also these quants use a new high quality imatrix including various
coding samples and multiple written languages.  Routed expert layers
make use of SotA CPU `IQx_K_R4` non-linear quants as well for likely
best perplexity per GiB. Both the `IQ2_K_R4` and `IQ4_K_R4` are designed
for ~17.33GiB weights offloaded to GPU VRAM with remaining VRAM available
for context.

bartowski uses full token embedding quality but lower attention, dense
layers, and shared expert quants. He does use a good quality imatrix with
perplexity performance within the measurement error relative to this one.
*UPDATE*: Also check out bartowski's new customized ["V2" flavors](https://huggingface.co/bartowski/deepseek-ai_DeepSeek-V3-0324-GGUF#v2-uploads)
recipes with improved perplexity for the size!!! The table below is his
original flavor quants.

unsloth sacrifices token embedding with middle quality attention and
dense layers, but no importance matrix.

mradermacher modelcard side-bar is not showing so was more difficult to
compare exact recipe. Their team graciously ran some commands to
provide details on [their recipe as well here](https://huggingface.co/mradermacher/DeepSeek-V3-0324-i1-GGUF/discussions/1#67eb113b5efb3c1d5ef491e5).

#### Comparison Details

<details>

<summary>Detailed Comparison of ~Q2 Class Quants</summary>

| | [ubergarm/DeepSeek-V3-0324-IQ2_K_R4](https://huggingface.co/ubergarm/DeepSeek-V3-0324-GGUF?show_file_info=DeepSeek-V3-0324-IQ2_K_R4%2FDeepSeek-V3-0324-IQ2_K_R4-00001-of-00005.gguf) | [bartowski/DeepSeek-V3-0324-Q2_K_L](https://huggingface.co/bartowski/deepseek-ai_DeepSeek-V3-0324-GGUF?show_file_info=deepseek-ai_DeepSeek-V3-0324-Q2_K_L%2Fdeepseek-ai_DeepSeek-V3-0324-Q2_K_L-00001-of-00007.gguf) | [unsloth/DeepSeek-V3-0324-UD-Q2_K_XL](https://huggingface.co/unsloth/DeepSeek-V3-0324-GGUF?show_file_info=UD-Q2_K_XL%2FDeepSeek-V3-0324-UD-Q2_K_XL-00001-of-00006.gguf) | [mradermacher/DeepSeek-V3-0324-i1-GGUF-Q2_K](https://huggingface.co/mradermacher/DeepSeek-V3-0324-i1-GGUF) |
| --- | --- | --- | --- | --- |
| **Overview**                       |            | "V1"   |        |         |
| `split.tensors.count`              |  1147      |  1025  |  1025  |         |
| `token_embd.weight`                | `Q8_0`     | `Q8_0` | `Q4_K` | `IQ3_S` |
| `output.weight`                    |            |        |        | `Q5_K`  |
| File Size (GiB)                    |   227      |   228  |   231  |         |
| **Multi-Head Latent Attention**    |            |        |        |         |
| `blk.*.attn_kv_b.weight`           | `Q8_0`     |   n/a  |   n/a  |   n/a   |
| `blk.*.attn_k_b.weight`            | `Q8_0`     |   n/a  |   n/a  |   n/a   |
| `blk.*.attn_v_b.weight`            | `Q8_0`     |   n/a  |   n/a  |   n/a   |
| **Dense Layers**                   |            |        |        |         |
| `blk.[0-2].attn_kv_a_mqa.weight`   | `Q8_0`     | `Q2_K` | `Q6_K` | `IQ2_XS`|
| `blk.[0-2].attn_kv_a_norm.weight`  | `F32`      |  `F32` |  `F32` |  `F32`  |
| `blk.[0-2].attn_kv_b.weight`       | `Q8_0`     | `Q2_K` | `Q6_K` | `IQ2_XS`|
| `blk.[0-2].attn_norm.weight`       | `F32`      |  `F32` |  `F32` |  `F32`  |
| `blk.[0-2].attn_q_a.weight`        | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[0-2].attn_q_a_norm.weight`   | `F32`      |  `F32` |  `F32` |  `F32`  |
| `blk.[0-2].attn_q_b.weight`        | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[0-2].ffn_down.weight`        | `Q8_0`     | `Q3_K` | `Q6_K` | `IQ3_S` |
| `blk.[0-2].ffn_gate.weight`        | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[0-2].ffn_norm.weight`        | `F32`      |  `F32` |  `F32` |  `F32`  |
| `blk.[0-2].ffn_up.weight`          | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[0-2].attn_output.weight`     | `Q8_0`     | `Q3_K` | `Q4_K` | `IQ3_S` |
| **Shared & Routed MoE Layers**     |            |        |        |         |
| `blk.[3-60].attn_kv_a_mqa.weight`  | `Q8_0`     | `Q2_K` | `Q6_K` | `IQ2_XS`|
| `blk.[3-60].attn_kv_a_norm.weight` | `F32`      | `F32`  | `F32`  |  `F32`  |
| `blk.[3-60].attn_kv_b.weight`      | `Q8_0`     | `Q2_K` | `Q6_K` | `IQ2_XS`|
| `blk.[3-60].attn_norm.weight`      | `F32`      | `F32`  | `F32`  |  `F32`  |
| `blk.[3-60].attn_q_a.weight`       | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[3-60].attn_q_a_norm.weight`  | `F32`      | `F32`  | `F32`  |  `F32`  |
| `blk.[3-60].attn_q_b.weight`       | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[3-60].exp_probs_b.bias`      | `F32`      | `F32`  | `F32`  |  `F32`  |
| `blk.[3-60].ffn_down_exps.weight`  | `IQ3_K_R4` | `Q3_K` | `Q3_K` | `IQ3_S` |
| `blk.[3-60].ffn_down_shexp.weight` | `Q8_0`     | `Q3_K` | `Q6_K` | `IQ3_S` |
| `blk.[3-60].ffn_gate_exps.weight`  | `IQ2_K_R4` | `Q2_K` | `Q2_K` | `IQ2_XS`|
| `blk.[3-60].ffn_gate_inp.weight`   | `F32`      | `F32`  | `F32`  |  `F32`  |
| `blk.[3-60].ffn_gate_shexp.weight` | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[3-60].ffn_norm.weight`       | `F32`      | `F32`  | `F32`  |  `F32`  |
| `blk.[3-60].ffn_up_exps.weight`    | `IQ2_K_R4` | `Q2_K` | `Q2_K` | `IQ2_XS`|
| `blk.[3-60].ffn_up_shexp.weight`   | `Q8_0`     | `Q2_K` | `Q4_K` | `IQ2_XS`|
| `blk.[3-60].attn_output.weight`    | `Q8_0`     | `Q3_K` | `Q4_K` | `IQ3_S` |
| **Important Matrix & Perplexity**  |            |        |        |         |
| `imatrix.dataset`                  | `calibration_data_v5_rc.txt`| `calibration_datav3.txt` | none | `imatrix-training-full-3` |
| Final PPL (wiki.test.raw)          | 3.5614 +/- 0.02001  |  3.9012 (V1) | ?  | ?  |

For reference the `Q8_0` achieves `PPL = 3.3482 +/- 0.01847` on same `wiki.test.raw` file.

</details>

#### imatrix

<details>

<summary>Importance Matrix Details Here</summary>

```bash
# run on single socket of dual Intel Xeon 6980P CPU *only*
numactl -N 0 -m 0 \
./build/bin/llama-imatrix \
    --verbosity 1 \
    -m /mnt/ai/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-Q8_0.gguf \
    -f calibration_data_v5_rc.txt \
    -o DeepSeek-V3-0324.imatrix \
    --ctx-size 512 \
    --numa numactl \
    --threads 128

.
.
.

compute_imatrix: computing over 213 chunks with batch_size 512
compute_imatrix: 41.77 seconds per pass - ETA 2 hours 28.28 minutes
[1]60.9029,[2]10.8011,[3]5.8709,[4]3.7872,[5]2.9688,[6]2.5088,[7]2.2214,[8]2.0224,[9]1.9110,
save_imatrix: entry '             blk.60.ffn_down_exps.weight' has partial data (99.61%) 1 out of 256 experts are missing data Storing **but be aware**
save_imatrix: entry '             blk.60.ffn_gate_exps.weight' has partial data (99.61%) 1 out of 256 experts are missing data Storing **but be aware**
save_imatrix: entry '               blk.60.ffn_up_exps.weight' has partial data (99.61%) 1 out of 256 experts are missing data Storing **but be aware**

save_imatrix: stored collected data after 10 chunks in /mnt/ai/models/ubergarm/DeepSeek-V3-0324-GGUF/imatrix-ubergarm-DeepSeek-V3-0324-ik_llamacpp-2089147a.dat

.
.
.

llama_print_timings:        load time =   42726.11 ms
llama_print_timings:      sample time =       0.00 ms /     1 runs   (    0.00 ms per token,      inf tokens per second)
llama_print_timings: prompt eval time = 7125661.28 ms / 109056 tokens (   65.34 ms per token,    15.30 tokens per second)
llama_print_timings:        eval time =       0.00 ms /     1 runs   (    0.00 ms per token,      inf tokens per second)
llama_print_timings:       total time = 7201368.59 ms / 109057 tokens

Final estimate: PPL = 3.4755 +/- 0.03305
```


</details>

#### Quant Cookers Secret Recipe

<details>

<summary>Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# Token embedding (GPU)
# NOTE: cannot be a repacked type due to tensor size
token_embd\.weight=q8_0
# output tensors (GPU)
output\.weight=q8_0
output_norm\.weight=q8_0

# First 3 dense layers (0-3) (GPU)
blk\.[0-2]\..*=q8_0

# All attention, weights, and bias tensors for MoE layers (3-60) (GPU)
# NOTE: attn_k_b.weight can't be k-, i-, or iqk-quant because its row size is 128
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

# Routed Experts (3-60) (CPU)
# NOTE: Traditional wisdom suggests earlier layers use higher quants
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
    --imatrix /mnt/raid/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324.imatrix \
    --token-embedding-type q8_0 \
    --output-tensor-type q8_0 \
    --custom-q "$custom" \
    /mnt/raid/models/deepseek-ai/DeepSeek-V3-0324-bf16-GGUF/DeepSeek-256x21B-V3-0324-BF16-00001-of-00030.gguf \
    /mnt/raid/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-IQ2_K_R4.gguf \
    IQ2_K_R4 \
    24
```

</details>

#### Perplexity

<details>

<summary>Perplexity Logs</summary>

```bash
$ CUDA_VISIBLE_DEVICES="0," \
./build/bin/llama-perplexity \
    --model /mnt/raid/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-IQ2_K_R4.gguf \
    -ctk q8_0 \
    -mla 2 -fa \
    -amb 512 \
    -fmoe \
    --ctx-size 512 \
    --ubatch-size 512 \
    -f wiki.test.raw \
    --seed 1337 \
    --n-gpu-layers 63 \
    --override-tensor exps=CPU \
    --threads 24

ggml_cuda_init: GGML_CUDA_FORCE_MMQ:    no
ggml_cuda_init: GGML_CUDA_FORCE_CUBLAS: no
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA RTX A6000, compute capability 8.6, VMM: yes
main: build = 3614 (b9c25fe7)
main: built with cc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0 for x86_64-linux-gnu
main: seed  = 1337
llama_model_loader: loaded meta data with 50 key-value pairs and 1147 tensors from /mnt/raid/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-IQ2_K_R4.gguf (version GGUF V3 (latest))
llama_model_loader: Dumping metadata keys/values. Note: KV overrides do not apply in this output.
llama_model_loader: - kv   0:                       general.architecture str              = deepseek2
llama_model_loader: - kv   1:                               general.type str              = model
llama_model_loader: - kv   2:                               general.name str              = DeepSeek V3 0324
llama_model_loader: - kv   3:                            general.version str              = V3-0324
llama_model_loader: - kv   4:                           general.basename str              = DeepSeek
llama_model_loader: - kv   5:                         general.size_label str              = 256x21B
llama_model_loader: - kv   6:                            general.license str              = mit
llama_model_loader: - kv   7:                      deepseek2.block_count u32              = 61
llama_model_loader: - kv   8:                   deepseek2.context_length u32              = 163840
llama_model_loader: - kv   9:                 deepseek2.embedding_length u32              = 7168
llama_model_loader: - kv  10:              deepseek2.feed_forward_length u32              = 18432
llama_model_loader: - kv  11:             deepseek2.attention.head_count u32              = 128
llama_model_loader: - kv  12:          deepseek2.attention.head_count_kv u32              = 128
llama_model_loader: - kv  13:                   deepseek2.rope.freq_base f32              = 10000.000000
llama_model_loader: - kv  14: deepseek2.attention.layer_norm_rms_epsilon f32              = 0.000001
llama_model_loader: - kv  15:                deepseek2.expert_used_count u32              = 8
llama_model_loader: - kv  16:                          general.file_type u32              = 338
llama_model_loader: - kv  17:        deepseek2.leading_dense_block_count u32              = 3
llama_model_loader: - kv  18:                       deepseek2.vocab_size u32              = 129280
llama_model_loader: - kv  19:            deepseek2.attention.q_lora_rank u32              = 1536
llama_model_loader: - kv  20:           deepseek2.attention.kv_lora_rank u32              = 512
llama_model_loader: - kv  21:             deepseek2.attention.key_length u32              = 192
llama_model_loader: - kv  22:           deepseek2.attention.value_length u32              = 128
llama_model_loader: - kv  23:       deepseek2.expert_feed_forward_length u32              = 2048
llama_model_loader: - kv  24:                     deepseek2.expert_count u32              = 256
llama_model_loader: - kv  25:              deepseek2.expert_shared_count u32              = 1
llama_model_loader: - kv  26:             deepseek2.expert_weights_scale f32              = 2.500000
llama_model_loader: - kv  27:              deepseek2.expert_weights_norm bool             = true
llama_model_loader: - kv  28:               deepseek2.expert_gating_func u32              = 2
llama_model_loader: - kv  29:             deepseek2.rope.dimension_count u32              = 64
llama_model_loader: - kv  30:                deepseek2.rope.scaling.type str              = yarn
llama_model_loader: - kv  31:              deepseek2.rope.scaling.factor f32              = 40.000000
llama_model_loader: - kv  32: deepseek2.rope.scaling.original_context_length u32              = 4096
llama_model_loader: - kv  33: deepseek2.rope.scaling.yarn_log_multiplier f32              = 0.100000
llama_model_loader: - kv  34:                       tokenizer.ggml.model str              = gpt2
llama_model_loader: - kv  35:                         tokenizer.ggml.pre str              = deepseek-v3
llama_model_loader: - kv  36:                      tokenizer.ggml.tokens arr[str,129280]  = ["
llama_model_loader: - kv  37:                  tokenizer.ggml.token_type arr[i32,129280]  = [3
llama_model_loader: - kv  38:                      tokenizer.ggml.merges arr[str,127741]  = ["
llama_model_loader: - kv  39:                tokenizer.ggml.bos_token_id u32              = 0
llama_model_loader: - kv  40:                tokenizer.ggml.eos_token_id u32              = 1
llama_model_loader: - kv  41:            tokenizer.ggml.padding_token_id u32              = 1
llama_model_loader: - kv  42:               tokenizer.ggml.add_bos_token bool             = true
llama_model_loader: - kv  43:               tokenizer.ggml.add_eos_token bool             = false
llama_model_loader: - kv  44:                    tokenizer.chat_template str              = {% if not add_generation_prompt is de...
llama_model_loader: - kv  45:               general.quantization_version u32              = 2
llama_model_loader: - kv  46:                      quantize.imatrix.file str              = /mnt/raid/models/ubergarm/DeepSeek-V3...
llama_model_loader: - kv  47:                   quantize.imatrix.dataset str              = calibration_data_v5_rc.txt
llama_model_loader: - kv  48:             quantize.imatrix.entries_count i32              = 720
llama_model_loader: - kv  49:              quantize.imatrix.chunks_count i32              = 213
llama_model_loader: - type  f32:  361 tensors
llama_model_loader: - type q8_0:  612 tensors
llama_model_loader: - type iq2_k_r4:  116 tensors
llama_model_loader: - type iq3_k_r4:   58 tensors
llm_load_vocab: special tokens cache size = 818
llm_load_vocab: token to piece cache size = 0.8223 MB
llm_load_print_meta: format           = GGUF V3 (latest)
llm_load_print_meta: arch             = deepseek2
llm_load_print_meta: vocab type       = BPE
llm_load_print_meta: n_vocab          = 129280
llm_load_print_meta: n_merges         = 127741
llm_load_print_meta: vocab_only       = 0
llm_load_print_meta: n_ctx_train      = 163840
llm_load_print_meta: n_embd           = 7168
llm_load_print_meta: n_layer          = 61
llm_load_print_meta: n_head           = 128
llm_load_print_meta: n_head_kv        = 128
llm_load_print_meta: n_rot            = 64
llm_load_print_meta: n_swa            = 0
llm_load_print_meta: n_embd_head_k    = 192
llm_load_print_meta: n_embd_head_v    = 128
llm_load_print_meta: n_gqa            = 1
llm_load_print_meta: n_embd_k_gqa     = 24576
llm_load_print_meta: n_embd_v_gqa     = 16384
llm_load_print_meta: f_norm_eps       = 0.0e+00
llm_load_print_meta: f_norm_rms_eps   = 1.0e-06
llm_load_print_meta: f_clamp_kqv      = 0.0e+00
llm_load_print_meta: f_max_alibi_bias = 0.0e+00
llm_load_print_meta: f_logit_scale    = 0.0e+00
llm_load_print_meta: n_ff             = 18432
llm_load_print_meta: n_expert         = 256
llm_load_print_meta: n_expert_used    = 8
llm_load_print_meta: causal attn      = 1
llm_load_print_meta: pooling type     = 0
llm_load_print_meta: rope type        = 0
llm_load_print_meta: rope scaling     = yarn
llm_load_print_meta: freq_base_train  = 10000.0
llm_load_print_meta: freq_scale_train = 0.025
llm_load_print_meta: n_ctx_orig_yarn  = 4096
llm_load_print_meta: rope_finetuned   = unknown
llm_load_print_meta: ssm_d_conv       = 0
llm_load_print_meta: ssm_d_inner      = 0
llm_load_print_meta: ssm_d_state      = 0
llm_load_print_meta: ssm_dt_rank      = 0
llm_load_print_meta: model type       = 671B
llm_load_print_meta: model ftype      = IQ2_K_R4 - 2.375 bpw
llm_load_print_meta: model params     = 672.050 B
llm_load_print_meta: model size       = 226.003 GiB (2.889 BPW) 
llm_load_print_meta: repeating layers = 224.169 GiB (2.873 BPW, 670.196 B parameters)
llm_load_print_meta: general.name     = DeepSeek V3 0324
llm_load_print_meta: BOS token        = 0 '<｜begin▁of▁sentence｜>'
llm_load_print_meta: EOS token        = 1 '<｜end▁of▁sentence｜>'
llm_load_print_meta: PAD token        = 1 '<｜end▁of▁sentence｜>'
llm_load_print_meta: LF token         = 131 'Ä'
llm_load_print_meta: max token length = 256
llm_load_print_meta: n_layer_dense_lead   = 3
llm_load_print_meta: n_lora_q             = 1536
llm_load_print_meta: n_lora_kv            = 512
llm_load_print_meta: n_ff_exp             = 2048
llm_load_print_meta: n_expert_shared      = 1
llm_load_print_meta: expert_weights_scale = 2.5
llm_load_print_meta: expert_weights_norm  = 1
llm_load_print_meta: expert_gating_func   = sigmoid
llm_load_print_meta: rope_yarn_log_mul    = 0.1000
llm_load_tensors: ggml ctx size =    0.93 MiB
Tensor blk.3.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.3.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.3.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.4.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.4.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.4.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.5.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.5.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.5.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.6.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.6.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.6.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.7.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.7.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.7.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.8.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.8.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.8.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.9.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.9.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.9.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.10.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.10.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.10.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.11.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.11.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.11.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.12.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.12.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.12.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.13.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.13.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.13.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.14.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.14.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.14.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.15.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.15.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.15.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.16.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.16.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.16.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.17.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.17.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.17.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.18.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.18.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.18.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.19.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.19.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.19.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.20.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.20.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.20.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.21.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.21.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.21.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.22.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.22.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.22.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.23.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.23.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.23.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.24.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.24.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.24.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.25.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.25.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.25.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.26.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.26.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.26.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.27.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.27.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.27.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.28.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.28.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.28.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.29.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.29.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.29.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.30.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.30.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.30.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.31.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.31.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.31.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.32.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.32.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.32.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.33.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.33.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.33.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.34.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.34.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.34.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.35.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.35.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.35.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.36.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.36.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.36.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.37.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.37.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.37.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.38.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.38.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.38.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.39.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.39.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.39.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.40.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.40.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.40.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.41.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.41.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.41.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.42.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.42.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.42.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.43.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.43.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.43.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.44.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.44.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.44.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.45.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.45.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.45.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.46.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.46.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.46.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.47.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.47.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.47.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.48.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.48.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.48.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.49.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.49.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.49.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.50.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.50.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.50.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.51.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.51.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.51.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.52.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.52.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.52.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.53.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.53.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.53.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.54.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.54.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.54.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.55.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.55.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.55.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.56.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.56.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.56.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.57.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.57.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.57.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.58.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.58.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.58.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.59.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.59.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.59.ffn_up_exps.weight buffer type overriden to CPU
Tensor blk.60.ffn_gate_exps.weight buffer type overriden to CPU
Tensor blk.60.ffn_down_exps.weight buffer type overriden to CPU
Tensor blk.60.ffn_up_exps.weight buffer type overriden to CPU
llm_load_tensors: offloading 61 repeating layers to GPU
llm_load_tensors: offloading non-repeating layers to GPU
llm_load_tensors: offloaded 62/62 layers to GPU
llm_load_tensors:        CPU buffer size = 228404.85 MiB
llm_load_tensors:        CPU buffer size =   938.98 MiB
llm_load_tensors:      CUDA0 buffer size = 17744.02 MiB
....................................................................................................
llama_new_context_with_model: n_ctx      = 2048
llama_new_context_with_model: n_batch    = 2048
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 1
llama_new_context_with_model: mla_attn   = 2
llama_new_context_with_model: attn_max_b = 512
llama_new_context_with_model: fused_moe  = 1
llama_new_context_with_model: ser        = -1, 0
llama_new_context_with_model: freq_base  = 10000.0
llama_new_context_with_model: freq_scale = 0.025
llama_kv_cache_init: layer 0: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 1: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 2: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 3: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 4: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 5: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 6: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 7: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 8: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 9: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 10: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 11: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 12: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 13: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 14: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 15: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 16: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 17: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 18: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 19: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 20: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 21: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 22: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 23: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 24: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 25: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 26: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 27: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 28: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 29: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 30: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 31: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 32: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 33: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 34: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 35: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 36: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 37: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 38: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 39: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 40: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 41: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 42: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 43: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 44: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 45: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 46: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 47: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 48: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 49: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 50: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 51: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 52: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 53: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 54: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 55: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 56: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 57: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 58: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 59: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init: layer 60: n_embd_head_qk_rope = 64, kv_lora_rank = 512
llama_kv_cache_init:      CUDA0 KV buffer size =    72.94 MiB
llama_new_context_with_model: KV self size  =   72.91 MiB, c^KV (q8_0):   72.91 MiB, kv^T: not used
llama_new_context_with_model:  CUDA_Host  output buffer size =     1.97 MiB
llama_new_context_with_model:      CUDA0 compute buffer size =   503.00 MiB
llama_new_context_with_model:  CUDA_Host compute buffer size =   162.01 MiB
llama_new_context_with_model: graph nodes  = 3548
llama_new_context_with_model: graph splits = 118

system_info: n_threads = 24 / 48 | AVX = 1 | AVX_VNNI = 0 | AVX2 = 1 | AVX512 = 1 | AVX512_VBMI = 1 | AVX512_VNNI = 1 | AVX512_BF16 = 1 | FMA = 1 | NEON = 0 | SVE = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 1 | SSSE3 = 1 | VSX = 0 | MATMUL_INT8 = 0 | LLAMAFILE = 1 | 
perplexity: tokenizing the input ..
perplexity: tokenization took 617.314 ms
perplexity: calculating perplexity over 561 chunks, n_ctx=512, batch_size=2048, n_seq=4
perplexity: 20.43 seconds per pass - ETA 47.75 minutes
[1]2.7687,[2]3.5402,[3]2.5152,[4]2.1223,[5]1.9022,[6]1.7765,[7]1.6869,[8]1.6282,[9]1.5856,[10]1.5431,[11]1.5379,[12]1.5781,[13]1.5947,[14]1.7232,[15]1.8539,[16]1.9054,[17]2.0733,[18]2.1998,[19]2.1545,[20]2.1438,[21]2.2433,[22]2.2143,[23]2.1801,[24]2.1951,[25]2.1614,[26]2.1344,[27]2.1796,[28]2.1874,[29]2.2426,[30]2.2752,[31]2.3094,[32]2.3270,[33]2.3654,[34]2.4142,[35]2.4636,[36]2.5196,[37]2.5536,[38]2.6038,[39]2.6420,[40]2.7049,[41]2.7453,[42]2.7591,[43]2.8110,[44]2.8248,[45]2.9060,[46]2.9548,[47]2.9179,[48]2.8736,[49]2.8574,[50]2.8805,[51]2.9241,[52]2.9352,[53]2.9930,[54]3.0074,[55]3.0389,[56]3.0729,[57]3.0906,[58]3.1289,[59]3.1400,[60]3.1872,[61]3.2286,[62]3.2827,[63]3.3128,[64]3.3584,[65]3.3660,[66]3.3592,[67]3.3366,[68]3.3659,[69]3.3658,[70]3.3835,[71]3.4002,[72]3.4111,[73]3.4239,[74]3.4442,[75]3.4233,[76]3.3758,[77]3.3326,[78]3.3303,[79]3.3130,[80]3.2983,[81]3.2648,[82]3.2686,[83]3.2416,[84]3.2081,[85]3.1745,[86]3.1530,[87]3.1529,[88]3.1288,[89]3.1175,[90]3.0963,[91]3.0711,[92]3.0476,[93]3.0211,[94]2.9999,[95]2.9825,[96]2.9833,[97]2.9927,[98]2.9829,[99]2.9668,[100]2.9680,[101]2.9599,[102]2.9779,[103]3.0038,[104]3.0240,[105]3.0204,[106]3.0449,[107]3.0697,[108]3.0899,[109]3.1240,[110]3.1566,[111]3.1776,[112]3.1502,[113]3.1382,[114]3.1169,[115]3.1009,[116]3.0955,[117]3.0743,[118]3.0530,[119]3.0316,[120]3.0096,[121]2.9932,[122]2.9731,[123]2.9560,[124]2.9358,[125]2.9177,[126]2.9016,[127]2.8884,[128]2.8807,[129]2.8715,[130]2.8593,[131]2.8514,[132]2.8569,[133]2.8658,[134]2.8729,[135]2.8841,[136]2.8996,[137]2.9132,[138]2.9206,[139]2.9316,[140]2.9307,[141]2.9306,[142]2.9272,[143]2.9268,[144]2.9227,[145]2.9142,[146]2.9109,[147]2.9136,[148]2.9117,[149]2.9118,[150]2.9045,[151]2.9008,[152]2.8968,[153]2.8916,[154]2.8899,[155]2.8930,[156]2.8931,[157]2.8978,[158]2.9057,[159]2.9076,[160]2.9166,[161]2.9246,[162]2.9344,[163]2.9420,[164]2.9627,[165]2.9857,[166]3.0037,[167]3.0164,[168]3.0418,[169]3.0653,[170]3.0882,[171]3.1102,[172]3.0929,[173]3.0748,[174]3.0617,[175]3.0500,[176]3.0377,[177]3.0267,[178]3.0141,[179]3.0021,[180]3.0052,[181]3.0197,[182]3.0349,[183]3.0493,[184]3.0624,[185]3.0716,[186]3.0873,[187]3.1029,[188]3.1162,[189]3.1261,[190]3.1263,[191]3.1330,[192]3.1349,[193]3.1393,[194]3.1599,[195]3.1691,[196]3.1822,[197]3.1921,[198]3.1960,[199]3.2012,[200]3.1993,[201]3.2141,[202]3.2085,[203]3.2130,[204]3.2147,[205]3.2140,[206]3.2168,[207]3.2250,[208]3.2347,[209]3.2436,[210]3.2429,[211]3.2373,[212]3.2379,[213]3.2456,[214]3.2470,[215]3.2523,[216]3.2521,[217]3.2455,[218]3.2449,[219]3.2453,[220]3.2444,[221]3.2445,[222]3.2436,[223]3.2447,[224]3.2492,[225]3.2506,[226]3.2411,[227]3.2394,[228]3.2405,[229]3.2439,[230]3.2492,[231]3.2556,[232]3.2476,[233]3.2406,[234]3.2426,[235]3.2421,[236]3.2507,[237]3.2588,[238]3.2680,[239]3.2784,[240]3.2870,[241]3.2980,[242]3.3129,[243]3.3258,[244]3.3340,[245]3.3461,[246]3.3567,[247]3.3546,[248]3.3498,[249]3.3471,[250]3.3394,[251]3.3362,[252]3.3375,[253]3.3407,[254]3.3468,[255]3.3525,[256]3.3556,[257]3.3577,[258]3.3586,[259]3.3614,[260]3.3636,[261]3.3641,[262]3.3625,[263]3.3674,[264]3.3696,[265]3.3698,[266]3.3714,[267]3.3732,[268]3.3765,[269]3.3796,[270]3.3775,[271]3.3755,[272]3.3686,[273]3.3688,[274]3.3615,[275]3.3506,[276]3.3398,[277]3.3414,[278]3.3514,[279]3.3572,[280]3.3649,[281]3.3719,[282]3.3773,[283]3.3837,[284]3.3896,[285]3.4035,[286]3.4052,[287]3.4076,[288]3.4123,[289]3.4143,[290]3.4063,[291]3.3989,[292]3.4003,[293]3.4002,[294]3.3985,[295]3.3973,[296]3.3992,[297]3.4007,[298]3.4059,[299]3.4120,[300]3.4151,[301]3.4186,[302]3.4206,[303]3.4218,[304]3.4201,[305]3.4319,[306]3.4388,[307]3.4495,[308]3.4378,[309]3.4322,[310]3.4227,[311]3.4258,[312]3.4287,[313]3.4348,[314]3.4368,[315]3.4397,[316]3.4407,[317]3.4420,[318]3.4426,[319]3.4432,[320]3.4472,[321]3.4472,[322]3.4485,[323]3.4545,[324]3.4549,[325]3.4602,[326]3.4643,[327]3.4680,[328]3.4700,[329]3.4715,[330]3.4776,[331]3.4810,[332]3.4845,[333]3.4828,[334]3.4827,[335]3.4826,[336]3.4819,[337]3.4828,[338]3.4829,[339]3.4850,[340]3.4883,[341]3.4937,[342]3.5027,[343]3.5120,[344]3.5171,[345]3.5093,[346]3.5022,[347]3.4991,[348]3.4918,[349]3.4879,[350]3.4865,[351]3.4911,[352]3.5060,[353]3.5152,[354]3.5281,[355]3.5370,[356]3.5432,[357]3.5550,[358]3.5655,[359]3.5685,[360]3.5745,[361]3.5839,[362]3.5924,[363]3.5975,[364]3.6038,[365]3.6091,[366]3.6193,[367]3.6280,[368]3.6342,[369]3.6417,[370]3.6499,[371]3.6633,[372]3.6725,[373]3.6756,[374]3.6789,[375]3.6833,[376]3.6959,[377]3.7072,[378]3.7094,[379]3.7088,[380]3.7053,[381]3.7103,[382]3.7160,[383]3.7190,[384]3.7229,[385]3.7265,[386]3.7323,[387]3.7382,[388]3.7409,[389]3.7299,[390]3.7200,[391]3.7099,[392]3.7042,[393]3.6954,[394]3.6870,[395]3.6790,[396]3.6692,[397]3.6606,[398]3.6507,[399]3.6408,[400]3.6318,[401]3.6214,[402]3.6109,[403]3.6021,[404]3.5911,[405]3.5808,[406]3.5703,[407]3.5604,[408]3.5516,[409]3.5429,[410]3.5373,[411]3.5385,[412]3.5339,[413]3.5373,[414]3.5406,[415]3.5383,[416]3.5384,[417]3.5403,[418]3.5345,[419]3.5357,[420]3.5327,[421]3.5318,[422]3.5329,[423]3.5331,[424]3.5372,[425]3.5368,[426]3.5376,[427]3.5367,[428]3.5397,[429]3.5405,[430]3.5433,[431]3.5445,[432]3.5429,[433]3.5394,[434]3.5394,[435]3.5334,[436]3.5277,[437]3.5235,[438]3.5219,[439]3.5200,[440]3.5245,[441]3.5297,[442]3.5373,[443]3.5347,[444]3.5352,[445]3.5360,[446]3.5408,[447]3.5439,[448]3.5462,[449]3.5488,[450]3.5524,[451]3.5560,[452]3.5581,[453]3.5595,[454]3.5578,[455]3.5603,[456]3.5603,[457]3.5624,[458]3.5674,[459]3.5675,[460]3.5673,[461]3.5639,[462]3.5674,[463]3.5746,[464]3.5799,[465]3.5733,[466]3.5721,[467]3.5710,[468]3.5729,[469]3.5704,[470]3.5678,[471]3.5682,[472]3.5695,[473]3.5684,[474]3.5670,[475]3.5680,[476]3.5669,[477]3.5660,[478]3.5668,[479]3.5685,[480]3.5709,[481]3.5669,[482]3.5704,[483]3.5695,[484]3.5728,[485]3.5790,[486]3.5820,[487]3.5853,[488]3.5908,[489]3.5930,[490]3.5979,[491]3.6040,[492]3.6085,[493]3.6080,[494]3.6086,[495]3.6109,[496]3.6127,[497]3.6156,[498]3.6160,[499]3.6153,[500]3.6191,[501]3.6235,[502]3.6223,[503]3.6207,[504]3.6229,[505]3.6260,[506]3.6343,[507]3.6372,[508]3.6405,[509]3.6328,[510]3.6289,[511]3.6229,[512]3.6191,[513]3.6132,[514]3.6120,[515]3.6142,[516]3.6099,[517]3.6103,[518]3.6094,[519]3.6100,[520]3.6145,[521]3.6133,[522]3.6114,[523]3.6172,[524]3.6158,[525]3.6143,[526]3.6100,[527]3.6046,[528]3.6021,[529]3.5989,[530]3.5958,[531]3.5925,[532]3.5864,[533]3.5800,[534]3.5762,[535]3.5767,[536]3.5794,[537]3.5827,[538]3.5859,[539]3.5887,[540]3.5944,[541]3.5979,[542]3.6007,[543]3.5961,[544]3.5918,[545]3.5918,[546]3.5850,[547]3.5790,[548]3.5722,[549]3.5657,[550]3.5601,[551]3.5546,[552]3.5491,[553]3.5435,[554]3.5431,[555]3.5418,[556]3.5443,[557]3.5479,[558]3.5539,[559]3.5582,[560]3.5635,[561]3.5614,
llama_print_timings:        load time =   39774.62 ms
llama_print_timings:      sample time =       0.00 ms /     1 runs   (    0.00 ms per token,      inf tokens per second)
llama_print_timings: prompt eval time = 2837909.33 ms / 287232 tokens (    9.88 ms per token,   101.21 tokens per second)
llama_print_timings:        eval time =       0.00 ms /     1 runs   (    0.00 ms per token,      inf tokens per second)
llama_print_timings:       total time = 2841519.57 ms / 287233 tokens

Final estimate: PPL = 3.5614 +/- 0.02001
```

</details>

#### Split

<details>

<summary>Split GGUF</summary>

*TODO*: Add key value metadata information before publishing.

```bash
$ ./build/bin/llama-gguf-split \
    --dry-run \
    --split \
    --split-max-size 50G \
    /mnt/raid/models/ubergarm/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-IQ2_K_R4.gguf \
    /mnt/raid/hf/DeepSeek-V3-0324-GGUF/DeepSeek-V3-0324-IQ2_K_R4/DeepSeek-V3-0324-IQ2_K_R4
```

</details>

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/)
* [ik_llama.cpp Getting Started Guide](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
* [imatrix calibration_data_v5_rc.txt](https://gist.github.com/tristandruyen/9e207a95c7d75ddf37525d353e00659c#file-calibration_data_v5_rc-txt)

---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: Qwen/Qwen3-235B-A22B
license: mit
base_model_relation: quantized
tags:
- imatrix
- qwen3_moe
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix Quantizations of Qwen/Qwen3-235B-A22B

This quant collection **REQUIRES** [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/) fork to support advanced non-linear SotA quants. Do **not** download these big files and expect them to run on mainline vanilla llama.cpp, ollama, LM Studio, KoboldCpp, etc!

These quants provide best in class quality for the given memory footprint.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community here and on `r/LocalLLaMA` for tips and tricks helping each other run all the fun new models!

Excited to share and learn together. Thanks!

## Quant Collection
So far these are my best recipes offering the great quality in good memory footprint breakpoints.

#### ubergarm/Qwen3-235B-A22B-mix-IQ3_K.gguf
This quant is designed to run at max speed with just under ~110GiB (V)RAM combinations e.g. 24GB VRAM + 96GB RAM (perfect for AM5 or LGA 1700 gamer rigs with 2x48GiB DDR5 DIMMs for max performance). This will allow for `-rtr` run-time repacking for maximum CPU throughput. You can still omit `-rtr` and use default `mmap()` behavior to run in less RAM at a penalty to speed. Or you can also "offline repack" to fit your exact setup and get the best of both worlds with quicker startup with `mmap()` and max CPU throughput. However, you might have to `--no-mmap` anyway depending on how Transparent Hugepages (THPs) are configured and effect performance on your rig.
```
106.830 GiB (3.903 BPW)

  f32:  471 tensors
 q8_0:    2 tensors
iq3_k:  188 tensors
iq4_k:   94 tensors
iq6_k:  376 tensors

Final estimate: PPL = 5.4403 +/- 0.03421 (wiki.test.raw, compare to Q8_0 at 5.3141 +/- 0.03321) (*TODO*: more benchmarking)
```

## Quick Start
#### `ik_llama.cpp` API server for hybrid GPU+CPU inferencing
```bash
# This example for 24GB VRAM + 96 GB RAM + 16 physical core CPU
# Offload first ffn layers  0-11 on GPU VRAM.
# Offload final ffn layers 12-93 on CPU RAM.
./build/bin/llama-server
  --model ubergarm/Qwen3-235B-A22B-GGUF/Qwen3-235B-A22B-mix-IQ3_K-00001-of-00003.gguf \
  --alias ubergarm/Qwen3-235B-A22B-mix-IQ3_K \
  -fa \
  -ctk q8_0 -ctv q8_0 \
  -c 32768 \
  -fmoe \
  -amb 512 \
  -rtr \
  -ot blk\.1[2-9]\.ffn.*=CPU \
  -ot blk\.[2-8][0-9]\.ffn.*=CPU \
  -ot blk\.9[0-3]\.ffn.*=CPU \
  -ngl 99 \
  --threads 16
  --host 127.0.0.1 \
  --port 8080
```

If you want more context and/or less VRAM usage, you can try:
* Smaller KV Cache quantization `-ctk q4_0 -ctv q4_0`

## Model Architechture

The original model architechture has 94 repeating layers/blocks with the unquantized `bf16` version being `448501.04 MB` total:

| Tensor                    | Dimension                    | Data Type | Size    |
|                       --- |                          --- |  --- |         ---  |
|token_embd.weight          | [ 4096, 151936,    1,     1] | bf16 | 1187.00 MiB  |
|                           |                              |      |              |
|blk.1.attn_k_norm.weight   | [  128,      1,    1,     1] |  f32 |    0.000 MiB |
|blk.1.attn_q_norm.weight   | [  128,      1,    1,     1] |  f32 |    0.000 MiB |
|blk.1.attn_norm.weight     | [ 4096,      1,    1,     1] |  f32 |    0.016 MiB |
|blk.1.ffn_gate_inp.weight  | [ 4096,    128,    1,     1] |  f32 |    2.000 MiB |
|blk.1.ffn_norm.weight      | [ 4096,      1,    1,     1] |  f32 |    0.016 MiB |
|                           |                              |      |              |
|blk.1.attn_k.weight        | [ 4096,    512,    1,     1] | bf16 |    4.00 MiB  |
|blk.1.attn_q.weight        | [ 4096,   8192,    1,     1] | bf16 |   64.00 MiB  |
|blk.1.attn_v.weight        | [ 4096,    512,    1,     1] | bf16 |    4.00 MiB  |
|blk.1.attn_output.weight   | [ 8192,   4096,    1,     1] | bf16 |   64.00 MiB  |
|                           |                              |      |              |
|blk.1.ffn_down_exps.weight | [ 1536,   4096,  128,     1] | bf16 | 1536.00 MiB  |
|blk.1.ffn_gate_exps.weight | [ 4096,   1536,  128,     1] | bf16 | 1536.00 MiB  |
|blk.1.ffn_up_exps.weight   | [ 4096,   1536,  128,     1] | bf16 | 1536.00 MiB  |
|                           |                              |      |              |
|output.weight              | [ 4096, 151936,     1,    1] | bf16 | 1187.00 MiB  |
|output.norm_weight         | [ 4096,     1,     1,     1] |  f32 |    0.016MiB  |

*TODO*: Compare this and other popular quants tensor choices.

## Quantization
<details>

<summary>👈Secret Recipe</summary>

```
#!/usr/bin/env bash

custom="
# Attention
blk\..*\.attn_k.*=iq6_k
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_v.*=iq6_k
blk\..*\.attn_output.*=iq6_k

# Token Embedding (put these second so attn_output regex doesn't become q8_0)
token_embd\.weight=q8_0
output\.weight=q8_0

# Experts
blk\..*\.ffn_down_exps\.weight=iq4_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq3_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

    #--token-embedding-type q8_0 \
    #--output-tensor-type q8_0 \
./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/Qwen3-235B-A22B-GGUF/imatrix-Qwen3-235B-A22B.dat \
    /mnt/raid/models/Qwen/Qwen3-235B-A22B/Qwen3-235B-A22B-BF16-00001-of-00011.gguf \
    /mnt/raid/models/ubergarm/Qwen3-235B-A22B-GGUF/Qwen3-235B-A22B-mix-IQ3_K.gguf \
    IQ3_K \
    24
```

</details>

## Discussion
*TODO*: Discuss some about comparing quants e.g. bartowski, unsloth, and mradermacher including "quality" and "speed".

## Benchmarks
In first tests with `llama-sweep-bench` I'm getting up to 140 tok/sec PP and 10 tok/sec TG on my 3090TI FE 24GB VRAM + AMD 9950X 2x48GB DDR5-6400 96GB RAM with OC infinity fabric. It does slow down of course as it gets deeper into the full 32k context. Check the linked Benchmarks Discussion for updates as this is all pretty fresh right now. Pretty amazing performance for a high quality LLM on a high-end gaming rig though!

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/)
* [ik_llama.cpp Getting Started Guide](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
* [ik_llama.cpp Benchmarks Discussion](https://github.com/ikawrakow/ik_llama.cpp/discussions/357)
* [imatrix calibration_data_v5_rc.txt](https://gist.github.com/tristandruyen/9e207a95c7d75ddf37525d353e00659c#file-calibration_data_v5_rc-txt)

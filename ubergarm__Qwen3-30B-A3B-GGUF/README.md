---
quantized_by: ubergarm
pipeline_tag: text-generation
base_model: Qwen/Qwen3-30B-A3B
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3-30B-A3B/blob/main/LICENSE
base_model_relation: quantized
tags:
- imatrix
- qwen3_moe
- conversational
- ik_llama.cpp
---

## `ik_llama.cpp` imatrix Quantizations of Qwen/Qwen3-30B-A3B

This quant collection **REQUIRES** [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/) fork to support advanced non-linear SotA quants. Do **not** download these big files and expect them to run on mainline vanilla llama.cpp, ollama, LM Studio, KoboldCpp, etc!

These quants provide best in class quality for the given memory footprint.

## Big Thanks
Shout out to Wendell and the **Level1Techs** crew, the community [Forums](https://forum.level1techs.com/t/deepseek-deep-dive-r1-at-home/225826), [YouTube Channel](https://www.youtube.com/@Level1Techs)!  **BIG thanks** for providing **BIG hardware** expertise and access to run these experiments and make these great quants available to the community!!!

Also thanks to all the folks in the quanting and inferencing community here and on `r/LocalLLaMA` for tips and tricks helping each other run all the fun new models!

Excited to share and learn together. Thanks!

## Quant Collection
So far these are my best recipes offering the great quality in good memory footprint breakpoints.

#### ubergarm/Qwen3-30B-A3B-mix-IQ4_K
This quant is provides the best in class quality while providing good speed performance. This quant is designed to run with over 32k context using GPU performant f16 KV-Cache in under 24GB VRAM GPU.  You could also try offload to CPU using `-nkvo -ctk q8_0 -ctv q8_0` and use `-rtr` for RAM optimized tensor packing on startup (without `mmap()` support) taking ~18396MiB of VRAM or less by offloading repeating layers to CPU as well at decreased speed.

```
17.679 GiB (4.974 BPW)

  f32:  241 tensors
 q8_0:    6 tensors
iq4_k:   96 tensors
iq5_k:   48 tensors
iq6_k:  188 tensors

Final estimate: PPL = 9.1184 +/- 0.07278 (wiki-test.raw, compare to BF16 at 9.0703 +/- 0.07223)
*NOTE*: Benchmarks including PPL with `wiki.test.raw` and KLD with `ubergarm-kld-test-corpus.txt` are looking interesting! Will publish soon!
```

## Quick Start
#### `ik_llama.cpp` API server for GPU inferencing
```bash
# This example for ~21468MiB VRAM Usage
./build/bin/llama-server
  --model ubergarm/Qwen3-30B-A3B-GGUF/Qwen3-30B-A3B-mix-IQ4_K \
  --alias ubergarm/Qwen3-30B-A3B-mix-IQ4_K \
  -fa \
  -ctk f16 -ctv f16 \
  -c 32768 \
  -fmoe \
  -ngl 99 \
  --threads 1
  --host 127.0.0.1 \
  --port 8080
```

If you want more context and/or less VRAM usage, you can try:
* Smaller KV Cache quantization `-ctk q4_0 -ctv q4_0`

If you want more throughput you could try:
* Increase context to max limit for your VRAM
* use `--parallel N` to have (context / N) available per slot
* use an asyncio client and keep the queue full

## Quantization
<details>

<summary>👈Secret Recipe</summary>

```bash
#!/usr/bin/env bash

custom="
# Attention (give Layer 0 a little extra as it scores lowest on cosine-similarity score)
blk\.0\.attn_k.*=q8_0
blk\.0\.attn_q.*=q8_0
blk\.0\.attn_v.*=q8_0
blk\.0\.attn_output.*=q8_0

blk\..*\.attn_k.*=iq6_k
blk\..*\.attn_q.*=iq6_k
blk\..*\.attn_v.*=iq6_k
blk\..*\.attn_output.*=iq6_k

# Token Embedding (put these second so attn_output regex doesn catch too early)
token_embd\.weight=q8_0
output\.weight=q8_0

# Experts
blk\..*\.ffn_down_exps\.weight=iq5_k
blk\..*\.ffn_(gate|up)_exps\.weight=iq4_k
"

custom=$(
  echo "$custom" | grep -v '^#' | \
  sed -Ez 's:\n+:,:g;s:,$::;s:^,::'
)

./build/bin/llama-quantize \
    --custom-q "$custom" \
    --imatrix /mnt/raid/models/ubergarm/Qwen3-30B-A3B-GGUF/imatrix-Qwen3-30B-A3B.dat \
    /mnt/raid/models/Qwen/Qwen3-30B-A3B/Qwen3-30B-A3B-BF16-00001-of-00002.gguf \
    /mnt/raid/models/ubergarm/Qwen3-30B-A3B-GGUF/Qwen3-30B-A3B-mix-IQ4_K.gguf \
    IQ4_K \
    24
```

</details>

## Discussion
*TODO*: Discuss some about comparing quants e.g. bartowski, unsloth, and mradermacher including "quality" and "speed".

## Benchmarks
In first tests with `llama-sweep-bench` I'm getting over 1600 tok/sec PP and 105 tok/sec TG on my 3090TI FE 24GB VRAM. It does slow down of course as it gets deeper into the full 32k context. Check the linked Benchmarks Discussion for updates as this is all pretty fresh right now. Pretty amazing performance both in terms of generation quality and speed for a model this size!

![Benchmarks showing these peak 1600 tok/sec PP and 105 tok/sec TG fully offloaded on 3090TI FE 24GB VRAM](images/benchmarks-01.png "Benchmarks showing these peak 1600 tok/sec PP and 105 tok/sec TG fully offloaded on 3090TI FE 24GB VRAM")

![Benchmarks showing Token Probability Deviation Percentiles](images/qwen3-30b-fig-09.png "Benchmarks showing Token Probability Deviation Percentiles")

## References
* [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp/)
* [ik_llama.cpp Getting Started Guide](https://github.com/ikawrakow/ik_llama.cpp/discussions/258)
* [ik_llama.cpp Benchmarks Discussion](https://github.com/ikawrakow/ik_llama.cpp/discussions/357)
* [imatrix calibration_data_v5_rc.txt](https://gist.github.com/tristandruyen/9e207a95c7d75ddf37525d353e00659c#file-calibration_data_v5_rc-txt)

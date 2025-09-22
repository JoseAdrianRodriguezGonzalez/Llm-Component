---
base_model:
- google/gemma-3-12b-it
datasets:
- eaddario/imatrix-calibration
language:
- en
license:
- gemma
pipeline_tag: text-generation
tags:
- gguf
- quant
- pruned
- experimental
---

# Experimental layer-wise + pruned (layers 26 and 29) quantization of google/gemma-3-12b-it

Using [LLaMA C++][llm] release [b5540][llm-rel] for quantization.

Original model: [google/gemma-3-12b-it][mdl]

From the original model creators:

> Terms of Use: [Terms](https://ai.google.dev/gemma/terms)
>
> Authors: Google DeepMind
> 
> Model Information
> Summary description and brief definition of inputs and outputs.
>
> Description
> Gemma is a family of lightweight, state-of-the-art open models from Google, built from the same research and technology used to create the Gemini models. Gemma 3 models are multimodal, handling text and image input and generating text output, with open weights for both pre-trained variants and instruction-tuned variants. Gemma 3 has a large, 128K context window, multilingual support in over 140 languages, and is available in more sizes than previous versions. Gemma 3 models are well-suited for a variety of text generation and image understanding tasks, including question answering, summarization, and reasoning. Their relatively small size makes it possible to deploy them in environments with limited resources such as laptops, desktops or your own cloud infrastructure, democratizing access to state of the art AI models and helping foster innovation for everyone.
>
> Inputs and outputs
> Input:
>
> Text string, such as a question, a prompt, or a document to be summarized
> Images, normalized to 896 x 896 resolution and encoded to 256 tokens each
> Total input context of 128K tokens for the 4B, 12B, and 27B sizes, and 32K tokens for the 1B size
> Output:
>
> Generated text in response to the input, such as an answer to a question, analysis of image content, or a summary of a document
> Total output context of 8192 tokens
Usage

# PLEASE READ THIS BEFORE USING THESE EXPERIMENTAL VERSIONS!

An area of personal interest is finding ways to optimize the inference performance of LLMs when deployed in resource-constrained environments like commodity hardware, desktops, laptops, mobiles, edge devices, etc. There are many approaches to accomplish this, including architecture simplification and knowledge distillation, but my focus has been primarily on quantization and pruning.

The method used to produce these experimental versions is covered in [Squeezing Tensor Bits: the quest for smaller LLMs][mdm], but at a high level it involves using a custom version of `llama-imatrix` and `llama-quantize` to identify influential tensors, quantize the most important layers to higher bit precision and the less important to lower bits, and remove (prune) one or more layers. This process was partly inspired by Dumitru's et al [Layer-Wise Quantization: A Pragmatic and Effective Method for Quantizing LLMs Beyond Integer Bit-Levels][lwq-ppr], and Xin Men's et al [ShortGPT: Layers in Large Language Models are More Redundant Than You Expect][sgpt-ppr]

As of version [b5125][qtz-rel], [llama-quantize][qtz] can now perform **tensor-wide quantization (TWQ)**, whereby user-defined tensors are quantized at a specific level, or perform **layer-wise quantization (LWQ)** by selecting different quantization types per tensor/layer. For example, `--tensor-type attn_v=q6_k` will quantize all *Attention Value* tensors at *q6_k* (TWQ), and `--tensor-type "\.([0-9]|1[01257]|31)\.attn_k=q4_k"` will quantize *Attention Key* tensors on layers 0 to 9, 10, 11, 12, 15, 17 and 31 at *q4_k*, leaving the remaining layers at their default value (LWQ).

A custom version of `llama-quantize` is used to prune the model by providing a comma-separated list in the `--prune-layers` command line option. The pruning operation will renumber remaining layers to avoid gaps in the sequence, update the relevant model metadata and, if an imatrix is available, it will use the correct importance score vector. This option can be used alongside `--tensor-type` to perform tensor/layer-wise quantization on selected tensor types, whilst at the same time pruning others. For example:
```
llama-quantize --tensor-type attn=q6_k --prune-layers 3,7,11 --imatrix imatrix.dat model-f32.gguf model-q4_k_m.gguf q4_k_m
```

An enhanced version of [llama-imatrix][imx] generates useful statistics to guide the tensor and layer selection process. `--show-statistics` will display:

### Tensor statistics:
- **Σ(Bias):** the sum of all activations over the tensor (i.e. the Importance Scores)
- **Min & Max:** minimum and maximum activation values
- **μ & σ:** activations' mean and standard deviation
- **% Active:** proportion of elements whose average activation exceeds a very small threshold (1e-6). Helpful to determine how alive/dormant the tensor is during inference
- **N:** number of activations in the tensor
- **Entropy:** entropy of the activation distribution, in bits (standard Shannon entropy measurement)
- **E (norm):** Normalized entropy.
- **ZD Score:** z-score distribution as described in [*3.1 Layer Importance Scores*][lwq-lim] in the **Layer-Wise Quantization** paper
- **CosSim:** cosine similarity between same type tensors with respect to the previous layer (i.e. blk.7.attn_k and blk.6.attn_k)

### Layer statistics:
- **Σ(Bias):** weighted average of the sum of all activations over the tensor (i.e. the Importance Scores)
- **ZD Score:** weighted average of the z-score distribution as described in [*3.1 Layer Importance Scores*][lwq-lim] in the **Layer-Wise Quantization** paper
- **CosSim:** weighted average of the cosine similarity of whole layer with respect to the previous layer (i.e. Layer 3 and 2)

Please note that tensor statistics are calculated for each individual tensor and should be used to compare between tensors of the same type only. For example, assuming that *attn_k* in layer 10 has a higher influence during inference than *attn_k* in layer 7 because its **Σ(Bias)** is larger makes sense, whilst concluding the same between *attn_k* and *ffn_down* does not.

There are two Pull Request ([prune][prn-pr] and [imatrix][imtx-pr]) to merge these changes back into the core llama.cpp project. This may or may not ever happen so, until then, the modified version will be available on [GitHub][gh] ([prune][gh-prn] and [imatrix][gh-itx]).

For testing and comparison I use models produced by [Unsloth][ust] ([Daniel and Michael Han][ust-ai] do some really advanced level stuff!) and [Bartowski][btk] (see credits below) but when they don't provide versions of the required model, all tests and comparisons are done against naive quantizations obtained by simply running `llama-quantize` with no further optimization. In this case however, whilst both have versions of this model, Unsloth's uses a different vocabulary size on their quants (262144 vs 262208) which does not allow for a valid like-for-like comparison.

All experimental versions were generated using an appropriate imatrix created from calibration datasets available at [eaddario/imatrix-calibration][ical]. At its core, an Importance Matrix (imatrix) is a table or, more broadly, a structured representation that scores the relative importance of different features or parameters in a machine learning model. It essentially quantifies the "impact" each feature has on a specific outcome, prediction, or relationship being modelled, and it helps to counterbalance the negative effects of quantization and pruning.

The process to generate these models is roughly as follows:

1. Convert the original model's tensors to [GGUF][ggf] F16*
2. Estimate the Perplexity score for the F16 model (baseline) using the [wikitext-2-raw-v1][wki-dat] dataset, and save the [logits][lgt]
3. Generate an [imatrix][imx-dat] from selected calibration datasets
4. Determine tensor and layer Importance Score contribution using the modified version of `llama-imatrix`
5. Select an appropriate quant level for each tensor and quantize/prune the model using `llama-quantize`. In this model's case, layers **26** and **29** have been pruned
6. Calculate Perplexity, KL Divergence, ARC (Easy+Challenge), HellaSwag, MMLU, Truthful QA and WinoGrande scores for each quantized model
7. Keep versions with the best scores
8. Repeat until all desired quants are created. I find that quantizations below Q3/IQ3 are not fit for my purposes and therefore do not usually generate them, but happy to provide other quants on request.

*[BF16][bf16] would be preferred, but Apple's GPUs don't support it yet, and therefore any operations are executed in the CPU, making it unacceptably slow. This is expected to change in the near term but until then, if you are using Apple kit avoid using any models tagged BF16

# Models

### Sizes (in GB)
| Model                                                               | Bartowski |  Repo | Shrinkage |
| ------------------------------------------------------------------- | --------: | ----: | --------: |
| [gemma-3-12b-it-pruned-IQ3_M](./gemma-3-12b-it-pruned-IQ3_M.gguf)   |      5.66 |  5.21 |      8.0% |
| [gemma-3-12b-it-pruned-IQ3_S](./gemma-3-12b-it-pruned-IQ3_S.gguf)   |      5.21 |  5.04 |      3.3% |
| [gemma-3-12b-it-pruned-IQ4_NL](./gemma-3-12b-it-pruned-IQ4_NL.gguf) |      6.89 |  6.16 |     10.6% |
| [gemma-3-12b-it-pruned-Q3_K_L](./gemma-3-12b-it-pruned-Q3_K_L.gguf) |      6.48 |  5.33 |     17.7% |
| [gemma-3-12b-it-pruned-Q3_K_M](./gemma-3-12b-it-pruned-Q3_K_M.gguf) |      6.01 |  5.04 |     16.1% |
| [gemma-3-12b-it-pruned-Q3_K_S](./gemma-3-12b-it-pruned-Q3_K_S.gguf) |      5.46 |  4.81 |     11.9% |
| [gemma-3-12b-it-pruned-Q4_K_M](./gemma-3-12b-it-pruned-Q4_K_M.gguf) |      7.30 |  6.20 |     15.1% |
| [gemma-3-12b-it-pruned-Q4_K_S](./gemma-3-12b-it-pruned-Q4_K_S.gguf) |      6.94 |  6.17 |     11.1% |
| [gemma-3-12b-it-pruned-Q5_K_M](./gemma-3-12b-it-pruned-Q5_K_M.gguf) |      8.44 |  7.32 |     13.3% |
| [gemma-3-12b-it-pruned-Q5_K_S](./gemma-3-12b-it-pruned-Q5_K_S.gguf) |      8.23 |  7.26 |     11.8% |
| [gemma-3-12b-it-pruned-Q6_K](./gemma-3-12b-it-pruned-Q6_K.gguf)     |      9.66 |  9.01 |      6.7% |
| [gemma-3-12b-it-pruned-Q8_0](./gemma-3-12b-it-pruned-Q8_0.gguf)     |     12.50 | 10.98 |     12.2% |

### Perplexity and KL Divergence scores
| Model                                                               |                μPPL |   𝜌PPL |               μKLD |        RMS Δp |
| ------------------------------------------------------------------- | ------------------: | -----: | -----------------: | ------------: |
| [gemma-3-12b-it-pruned-IQ3_M](./gemma-3-12b-it-pruned-IQ3_M.gguf)   | 35.478449 ±0.411747 | 80.18% | 1.229937 ±0.004277 | 30.166 ±0.089 |
| [gemma-3-12b-it-pruned-IQ3_S](./gemma-3-12b-it-pruned-IQ3_S.gguf)   | 32.557804 ±0.369351 | 80.53% | 1.196823 ±0.004146 | 29.810 ±0.088 |
| [gemma-3-12b-it-pruned-IQ4_NL](./gemma-3-12b-it-pruned-IQ4_NL.gguf) | 36.879518 ±0.436763 | 80.79% | 1.190922 ±0.004215 | 29.578 ±0.088 |
| [gemma-3-12b-it-pruned-Q3_K_L](./gemma-3-12b-it-pruned-Q3_K_L.gguf) | 33.537202 ±0.371564 | 79.10% | 1.263077 ±0.004253 | 31.084 ±0.088 |
| [gemma-3-12b-it-pruned-Q3_K_M](./gemma-3-12b-it-pruned-Q3_K_M.gguf) | 34.029948 ±0.376082 | 78.62% | 1.300974 ±0.004321 | 31.537 ±0.088 |
| [gemma-3-12b-it-pruned-Q3_K_S](./gemma-3-12b-it-pruned-Q3_K_S.gguf) | 36.103787 ±0.402250 | 77.13% | 1.395578 ±0.004559 | 32.089 ±0.088 |
| [gemma-3-12b-it-pruned-Q4_K_M](./gemma-3-12b-it-pruned-Q4_K_M.gguf) | 31.219358 ±0.342580 | 80.83% | 1.106608 ±0.003932 | 29.739 ±0.088 |
| [gemma-3-12b-it-pruned-Q4_K_M-bartowski][b-q4km]                    |  9.197963 ±0.073909 | 98.63% | 0.045560 ±0.000416 |  6.400 ±0.054 |
| [gemma-3-12b-it-pruned-Q4_K_S](./gemma-3-12b-it-pruned-Q4_K_S.gguf) | 31.245217 ±0.343080 | 80.86% | 1.105266 ±0.003926 | 29.698 ±0.088 |
| [gemma-3-12b-it-pruned-Q5_K_M](./gemma-3-12b-it-pruned-Q5_K_M.gguf) | 30.668770 ±0.335889 | 81.60% | 1.039101 ±0.003848 | 29.177 ±0.088 |
| [gemma-3-12b-it-pruned-Q5_K_S](./gemma-3-12b-it-pruned-Q5_K_S.gguf) | 30.644285 ±0.335716 | 81.62% | 1.038541 ±0.003836 | 29.119 ±0.088 |
| [gemma-3-12b-it-pruned-Q6_K](./gemma-3-12b-it-pruned-Q6_K.gguf)     | 30.107026 ±0.329175 | 81.96% | 1.009233 ±0.003785 | 28.800 ±0.088 |
| [gemma-3-12b-it-pruned-Q8_0](./gemma-3-12b-it-pruned-Q8_0.gguf)     | 30.014168 ±0.327772 | 82.04% | 1.004325 ±0.003776 | 28.772 ±0.088 |
| [gemma-3-12b-it-pruned-F16](./gemma-3-12b-it-pruned-F16.gguf)       |  9.042786 ±0.071503 |   100% |                N/A |           N/A |

### ARC, HellaSwag, MMLU, Truthful QA and WinoGrande scores
Scores generated using [llama-perplexity][ppl] with 750 tasks per test, and a context size of 768 tokens.

For the test data used in the generation of these scores, follow the appropriate links: [HellaSwag][hsw-tst], [ARC, MMLU, Truthful QA][tst-dat] and [WinoGrande][wng-tst]

| Model                                                               |             ARC | HellaSwag |            MMLU |     Truthful QA |      WinoGrande | Avg Score |
| ------------------------------------------------------------------- | --------------: | --------: | --------------: | --------------: | --------------: | --------: |
| [gemma-3-12b-it-pruned-IQ3_M](./gemma-3-12b-it-pruned-IQ3_M.gguf)   | 66.9333 ±1.7190 |     74.67 | 42.0000 ±1.8034 | 39.4667 ±1.7860 | 67.4667 ±1.7119 |     58.11 |
| [gemma-3-12b-it-pruned-IQ3_S](./gemma-3-12b-it-pruned-IQ3_S.gguf)   | 65.0667 ±1.7420 |     74.80 | 42.8000 ±1.8079 | 40.4000 ±1.7930 | 66.1333 ±1.7292 |     57.84 |
| [gemma-3-12b-it-pruned-IQ4_NL](./gemma-3-12b-it-pruned-IQ4_NL.gguf) | 68.2667 ±1.7007 |     75.47 | 42.6667 ±1.8072 | 40.1333 ±1.7910 | 68.5333 ±1.6968 |     59.01 |
| [gemma-3-12b-it-pruned-Q3_K_L](./gemma-3-12b-it-pruned-Q3_K_L.gguf) | 67.8667 ±1.7063 |     75.73 | 42.5333 ±1.8065 | 40.2667 ±1.7920 | 67.0667 ±1.7172 |     58.69 |
| [gemma-3-12b-it-pruned-Q3_K_M](./gemma-3-12b-it-pruned-Q3_K_M.gguf) | 68.6667 ±1.6949 |     75.20 | 44.4000 ±1.8155 | 40.0000 ±1.7900 | 65.8667 ±1.7325 |     58.83 |
| [gemma-3-12b-it-pruned-Q3_K_S](./gemma-3-12b-it-pruned-Q3_K_S.gguf) | 67.6000 ±1.7100 |     75.20 | 43.7333 ±1.8126 | 39.8667 ±1.7890 | 66.5333 ±1.7242 |     58.59 |
| [gemma-3-12b-it-pruned-Q4_K_M](./gemma-3-12b-it-pruned-Q4_K_M.gguf) | 69.8667 ±1.6766 |     77.47 | 43.6000 ±1.8119 | 40.8000 ±1.7958 | 68.4000 ±1.6988 |     60.03 |
| [gemma-3-12b-it-pruned-Q4_K_M-bartowski][b-q4km]                    | 69.6000 ±1.6807 |     81.07 | 43.6000 ±1.8119 | 41.0667 ±1.7976 | 75.7333 ±1.5664 |     62.21 |
| [gemma-3-12b-it-pruned-Q4_K_S](./gemma-3-12b-it-pruned-Q4_K_S.gguf) | 69.8667 ±1.6766 |     77.33 | 43.4667 ±1.8113 | 40.8000 ±1.7958 | 69.6000 ±1.6807 |     60.21 |
| [gemma-3-12b-it-pruned-Q5_K_M](./gemma-3-12b-it-pruned-Q5_K_M.gguf) | 68.8000 ±1.6929 |     77.87 | 45.3333 ±1.8190 | 41.2000 ±1.7984 | 68.8000 ±1.6929 |     60.40 |
| [gemma-3-12b-it-pruned-Q5_K_S](./gemma-3-12b-it-pruned-Q5_K_S.gguf) | 68.9333 ±1.6909 |     77.73 | 45.0667 ±1.8180 | 41.3333 ±1.7993 | 68.6667 ±1.6949 |     60.35 |
| [gemma-3-12b-it-pruned-Q6_K](./gemma-3-12b-it-pruned-Q6_K.gguf)     | 68.9333 ±1.6909 |     78.66 | 45.4667 ±1.8194 | 40.8000 ±1.7958 | 68.6667 ±1.6949 |     60.51 |
| [gemma-3-12b-it-pruned-Q8_0](./gemma-3-12b-it-pruned-Q8_0.gguf)     | 68.8000 ±1.6929 |     78.40 | 45.4667 ±1.8194 | 41.7333 ±1.8018 | 68.8000 ±1.6929 |     60.64 |
| [gemma-3-12b-it-pruned-F16](./gemma-3-12b-it-pruned-F16.gguf)       | 69.2000 ±1.6869 |     81.20 | 45.3333 ±1.8190 | 41.4667 ±1.8002 | 74.8000 ±1.5864 |     62.40 |

### Tokens per Second - Benchmarks
Scores generated using [llama-bench][bch]. Naive (`llama-quantize` with no optimization) Q4_K_M quantization included for comparison.

| model                                                               |     size |  params | backend    | threads |          test |           t/s |
| ------------------------------------------------------------------- | -------: | ------: | ---------- | ------: | ------------: | ------------: |
| [gemma-3-12b-it-pruned-Q4_K_M](./gemma-3-12b-it-pruned-Q4_K_M.gguf) | 5.77 GiB | 11.32 B | Metal,BLAS |      12 |         pp512 |  523.27 ±3.74 |
| [gemma-3-12b-it-pruned-Q4_K_M](./gemma-3-12b-it-pruned-Q4_K_M.gguf) | 5.77 GiB | 11.32 B | Metal,BLAS |      12 |         tg128 |   46.92 ±0.60 |
| [gemma-3-12b-it-pruned-Q4_K_M](./gemma-3-12b-it-pruned-Q4_K_M.gguf) | 5.77 GiB | 11.32 B | Metal,BLAS |      12 | pp1024+tg1024 |   75.45 ±0.35 |
| [gemma-3-12b-it-pruned-Q4_K_M-bartowski][b-q4km]                    | 6.79 GiB | 11.77 B | Metal,BLAS |      12 |         pp512 | 482.36 ±23.04 |
| [gemma-3-12b-it-pruned-Q4_K_M-bartowski][b-q4km]                    | 6.79 GiB | 11.77 B | Metal,BLAS |      12 |         tg128 |   45.54 ±1.21 |
| [gemma-3-12b-it-pruned-Q4_K_M-bartowski][b-q4km]                    | 6.79 GiB | 11.77 B | Metal,BLAS |      12 | pp1024+tg1024 |   74.27 ±0.19 |

# Metrics used
**[Perplexity][ppx]:** one of the key metrics used in NLP evaluation. It measures the quality of a language model by evaluating how well it predicts the next token given a particular sequence of words. A PPL of **1** indicates an exact match between predicted and actual, whereas values greater than one indicate a degree of "surprise" the generated token differs from the expected.

**[Kullback–Leibler (KL) Divergence][kld]:** a statistical measure of how much a probability distribution differs from another. When quantizing models (or altering the original tensors in any way for that matter), the closest we can preserve the weights' probability distribution to the original model the better, thus the closest to **0** the better.

**[AI2 Reasoning Challenge (ARC)][arc]:** a benchmark to evaluate the ability of AI models to answer complex science questions that require logical reasoning beyond pattern matching.

**[HellaSwag][hsw]:** the Harder Endings, Longer contexts, and Low-shot Activities for Situations With Adversarial Generations (bit of a mouthful!) is a benchmark designed to test commonsense natural language inference. It requires the model to predict the most likely ending of a sentence.

**[MMLU][mmlu]:** the Massive Multitask Language Understanding evaluates LLMs’ general knowledge and problem-solving abilities across 57 subjects, including elementary mathematics, US history, computer science, and law.

**[Truthful QA][tqa]:** evaluates how well LLMs generate truthful responses to questions. It identifies whether AI models can avoid generating false or misleading information, particularly in areas where human knowledge is prone to misconceptions.

**[Winogrande][wng]:** based on the [Winograd Schema Challenge][wng-chl], is a natural language understanding task requiring models to resolve ambiguities in sentences involving pronoun references.

## Credits
A big **Thank You!** to [Colin Kealty][btk] for the many contributions and for being one of the best sources of high quality quantized models available on Hugging Face, and a really big ***Thank You!*** to [Georgi Gerganov][ggg] for his amazing work with **llama.cpp** and the **ggml/gguf** libraries.

[arc]:      https://leaderboard.allenai.org/arc/submissions/get-started
[btk]:      https://huggingface.co/bartowski
[bch]:      https://github.com/ggml-org/llama.cpp/tree/master/tools/llama-bench
[bf16]:     https://en.wikipedia.org/wiki/Bfloat16_floating-point_format
[b-q4km]:   https://huggingface.co/bartowski/google_gemma-3-12b-it-pruned-GGUF/blob/main/google_gemma-3-12b-it-pruned-Q4_K_M.gguf
[u-q4km]:   https://huggingface.co/unsloth
[ical]:     https://huggingface.co/datasets/eaddario/imatrix-calibration
[ggg]:      https://github.com/ggerganov
[ggf]:      https://huggingface.co/docs/hub/en/gguf
[gh]:       https://github.com/EAddario
[gh-itx]:   https://github.com/EAddario/llama.cpp/tree/imatrix
[gh-prn]:   https://github.com/EAddario/llama.cpp/tree/prune
[hsw]:      https://rowanzellers.com/hellaswag
[hsw-tst]:  https://github.com/klosax/hellaswag_text_data
[imx-dat]:  https://huggingface.co/eaddario/gemma-3-12b-it-pruned-GGUF/tree/main/imatrix
[imx]:      https://github.com/ggml-org/llama.cpp/tree/master/tools/imatrix
[imtx-pr]:  https://github.com/ggml-org/llama.cpp/pull/12718
[kld]:      https://en.wikipedia.org/wiki/Kullback–Leibler_divergence
[llm]:      https://github.com/ggerganov/llama.cpp
[llm-rel]:  https://github.com/ggml-org/llama.cpp/releases/tag/b5540
[lgt]:      https://huggingface.co/eaddario/gemma-3-12b-it-pruned-GGUF/tree/main/logits
[lwq-lim]:  https://arxiv.org/html/2403.03853v3#S3
[lwq-ppr]:  https://arxiv.org/abs/2406.17415
[mdm]:      https://medium.com/@eaddario/squeezing-tensor-bits-the-quest-for-smaller-llms-86b23bd052ca
[mmlu]:     https://github.com/hendrycks/test
[mdl]:      https://huggingface.co/google/gemma-3-12b-it
[ppl]:      https://github.com/ggml-org/llama.cpp/tree/master/tools/perplexity
[ppx]:      https://huggingface.co/docs/transformers/en/perplexity
[prn-pr]:   https://github.com/ggml-org/llama.cpp/pull/13037
[qtz]:      https://github.com/ggml-org/llama.cpp/tree/master/tools/quantize
[qtz-rel]:  https://github.com/ggerganov/llama.cpp/releases/tag/b5125
[sgpt-ppr]: https://arxiv.org/abs/2403.03853
[tst-dat]:  https://huggingface.co/datasets/ikawrakow/validation-datasets-for-llama.cpp/tree/main
[tqa]:      https://github.com/sylinrl/TruthfulQA
[ust]:      https://huggingface.co/unsloth
[ust-ai]:   https://unsloth.ai
[wng-chl]:  https://cdn.aaai.org/ocs/4492/4492-21843-1-PB.pdf
[wki-dat]:  https://huggingface.co/datasets/Salesforce/wikitext/tree/main/wikitext-2-raw-v1
[wng]:      https://winogrande.allenai.org
[wng-tst]:  https://huggingface.co/datasets/ikawrakow/winogrande-eval-for-llama.cpp/tree/main

---
license: llama2
tags:
- llama
- llama-2
- facebook
- meta
- text-generation-inference
- quantized
- gguf
- 32k-context
- togethercomputer
language:
- en
pipeline_tag: text-generation
---

# LLaMA-2-7B-32K-Instruct_GGUF #

[Together Computer, Inc.](https://together.ai/) has released
[Llama-2-7B-32K-Instruct](https://huggingface.co/togethercomputer/Llama-2-7B-32K-Instruct), a model based on
[Meta AI](https://ai.meta.com)'s [LLaMA-2-7B](https://huggingface.co/meta-llama/Llama-2-7b),
but fine-tuned for context lengths up to 32K using "Position Interpolation" and "Rotary Position Embeddings"
(RoPE).

While the current version of [llama.cpp](https://github.com/ggerganov/llama.cpp) already supports such large
context lengths, it requires quantized files in the new GGUF format - and that's where this repo comes in:
it contains the following quantizations of the original weights from Together's fined-tuned model

* [Q2_K](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q2_K.gguf)
* [Q3_K_S](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q3_K_S.gguf),
[Q3_K_M](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q3_K_M.gguf) (aka Q3_K) and
[Q3_K_L](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q3_K_L.gguf)
* [Q4_0](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q4_0.gguf),
[Q4_1](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q4_1.gguf),
[Q4_K_S](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q4_K_S.gguf) and
[Q4_K_M](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q4_K_M.gguf) (aka Q4_K)
* [Q5_0](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q5_0.gguf),
[Q5_1](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q5_1.gguf),
[Q5_K_S](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q5_K_S.gguf) and
[Q5_K_M](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q5_K_M.gguf) (aka Q5_K)
* [Q6_K](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q6_K.gguf),
* [Q8_0](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-Q8_0.gguf) and
* [F16](https://huggingface.co/rozek/LLaMA-2-7B-32K-Instruct_GGUF/blob/main/LLaMA-2-7B-32K-Instruct-f16.gguf) (unquantized)

> Nota bene: while RoPE makes inferences with large contexts possible, you still need an awful lot of RAM
> when doing so. And since "32K" does not mean that you always have to use a context size of 32768 (only that
> the model was fine-tuned for that size), it is recommended that you keep your context as small as possible

> If you need quantizations for Together Computer's
> [Llama-2-7B-32K](https://huggingface.co/togethercomputer/Llama-2-7B-32K)
> model, then look for
> [LLaMA-2-7B-32K_GGUF](https://huggingface.co/rozek/LLaMA-2-7B-32K_GGUF)

## How Quantization was done ##

Since the author does not want arbitrary Python stuff to loiter on his computer, the quantization was done
using [Docker](https://www.docker.com/).

Assuming that you have the [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on
your system and also have a basic knowledge of how to use it, you may just follow the instructions shown
below in order to generate your own quantizations:

> Nota bene: you will need 30+x GB of free disk space, at least - depending on your quantization

1. create a new folder called `llama.cpp_in_Docker`<br>this folder will later be mounted into the Docker
container and store the quantization results
2. download the weights for the fine-tuned LLaMA-2 model from
[Hugging Face](https://huggingface.co/togethercomputer/LLaMA-2-7B-32K-Instruct) into a subfolder of
`llama.cpp_in_Docker` (let's call the new folder `LLaMA-2-7B-32K-Instruct`)
4. within the <u>Docker Desktop</u>, search for and download a `basic-python` image - just use one of
the most popular ones
5. from a <u>terminal session on your host computer</u> (i.e., not a Docker container!), start a new container
for the downloaded image which mounts the folder we created before:<br>
```
docker run --rm \
  -v ./llama.cpp_in_Docker:/llama.cpp \
  -t basic-python /bin/bash
```

(you may have to adjust the path to your local folder)

5. back in the <u>Docker Desktop</u>, open the "Terminal" tab of the started container and enter the
following commands (one after the other - copying the complete list and pasting it into the terminal
as a whole does not always seems to work properly):<br>
```
apt update
apt-get install software-properties-common -y
apt-get update
apt-get install g++ git make -y
cd /llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
```
6. now open the "Files" tab and navigate to the file `/llama.cpp/llama.cpp/Makefile`, right-click on it and
choose "Edit file"
7. search for `aarch64`, and - in the line found (which looks like `ifneq ($(filter aarch64%,$(UNAME_M)),)`) - 
change `ifneq` to `ifeq`
8. save your change using the disk icon in the upper right corner of the editor pane and open the "Terminal"
tab again
9. now enter the following commands:<br>
```
make
python3 -m pip install -r requirements.txt
python3 convert.py ../LLaMA-2-7B-32K-Instruct
```
10. you are now ready to run the actual quantization, e.g., using<br>
```
./quantize ../LLaMA-2-7B-32K-Instruct/ggml-model-f16.gguf \
   ../LLaMA-2-7B-32K-Instruct/LLaMA-2-7B-32K-Instruct-Q4_0.gguf Q4_0
```
11. run any quantizations you need and stop the container when finished (the container will automatically
be deleted but the generated files will remain available on your host computer)
12. the `basic-python` image may also be deleted (manually) unless you plan to use it again in the near future

You are now free to move the quanitization results to where you need them and run inferences with context
lengths up to 32K (depending on the amount of memory you will have available - long contexts need a
lot of RAM)

## License ##

Concerning the license(s):

* the [original model](https://ai.meta.com/llama/) (from Meta AI) was released under a rather [permissive
license](https://ai.meta.com/llama/license/)
* the fine tuned model from Together Computer uses the
[same license](https://huggingface.co/togethercomputer/LLaMA-2-7B-32K-Instruct/blob/main/README.md)
* as a consequence, this repo does so as well
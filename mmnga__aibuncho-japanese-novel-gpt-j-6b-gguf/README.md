---
license: openrail
language:
- ja
pipeline_tag: text-generation
tags:
- gpt-j
---

# AIBunCho/japanese-novel-gpt-j-6b
[AI BunChoさんが公開しているjapanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b)のgguf変換版です。
  
*注意:こちらはブランチで試用になります。llama.cpp本家にgptneox, gpt2が実装された時に、このggufファイルが使用できない可能性があります。*

***[GitHubリポジトリの readme はこちら](https://github.com/mmnga/llama.cpp/tree/mmnga-dev)***

## Usage (試用)

```
git clone --branch mmnga-dev https://github.com/mmnga/llama.cpp.git
cd llama.cpp
make -j
./main -m 'aibuncho-japanese-novel-gpt-j-6b-q4_0.gguf' -n 128 -p '犬「吾輩は猫である。」猫「'  --top_p 0.9 --temp 0.7 --repeat-penalty 1.1
```

**CUBLAS**
```
LLAMA_CUBLAS=1 make -j
./main -m 'aibuncho-japanese-novel-gpt-j-6b-q4_0.gguf' -n 128 -p '犬「吾輩は猫である。」猫「' -ngl 24
```

**従来のCPU実行**
~~~~bash
git clone --branch mmnga-dev https://github.com/mmnga/llama.cpp.git
cd llama.cpp
make -j gptj
./gptj -m 'aibuncho-japanese-novel-gpt-j-6b-q4_0.gguf' -n 128 -p '犬「吾輩は猫なのか」' --top_p 0.9 --temp 0.7 --repeat-penalty 1.2  -eos '</s>' -sep '[SEP]'
~~~~
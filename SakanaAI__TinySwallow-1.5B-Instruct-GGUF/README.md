---
license: apache-2.0
language:
- ja
pipeline_tag: text-generation
library_name: transformers
base_model:
- Qwen/Qwen2.5-1.5B-Instruct
datasets:
- tokyotech-llm/lmsys-chat-1m-synth
- tokyotech-llm/swallow-magpie-ultra-v0.1
- tokyotech-llm/swallow-swallow-gemma-magpie-v0.1
---
# TinySwallow-1.5B-Instruct-GGUF

🤗 [Models](https://huggingface.co/SakanaAI) | 📚 [Paper](http://arxiv.org/abs/2501.16937) | 📝 [Blog](https://sakana.ai/taid-jp/) | 🐦 [Twitter](https://twitter.com/SakanaAILabs)

This is the [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) model in GGUF format. 

[TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) is an instruction-tuned version of [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B), created through *TAID (Temporally Adaptive Interpolated Distillation)*, our new knowledge distillation method. 
We used [Qwen2.5-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-32B-Instruct) as the teacher model and [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) as the student model. 
The model has been further instruction-tuned to enhance its ability to follow instructions and engage in conversations in Japanese.


## Usage
Check out [our GitHub repository](https://github.com/SakanaAI/TinySwallow-ChatUI/blob/main/docs/iphone.md) to quickly run it on your iPhone.

## Model Details

- **Model type:** Autoregressive Language Model
- **Language(s):** Japanese
- **Paper:** http://arxiv.org/abs/2501.16937
- **Blog:** https://sakana.ai/taid-jp/
- **Training Datasets:**
  - [Gemma-2-LMSYS-Chat-1M-Synth](https://huggingface.co/datasets/tokyotech-llm/lmsys-chat-1m-synth/blob/main/README_gemma.md)
  - [tokyotech-llm/swallow-magpie-ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1)
  - [tokyotech-llm/swallow-gemma-magpie-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-gemma-magpie-v0.1)

## Uses
This model is provided for research and development purposes only and should be considered as an experimental prototype. 
It is not intended for commercial use or deployment in mission-critical environments. 
Use of this model is at the user's own risk, and its performance and outcomes are not guaranteed. 
Sakana AI shall not be liable for any direct, indirect, special, incidental, or consequential damages, or any loss arising from the use of this model, regardless of the results obtained. 
Users must fully understand the risks associated with the use of this model and use it at their own discretion.


## Acknowledgement

We would like to thank the developers of the source models for their contributions and for making their work available. 

## Authors

* [Sakana AI](https://sakana.ai/)
  * [Makoto Shing](https://huggingface.co/mkshing)
  * [Taishi Nakamura](https://x.com/Setuna7777_2)
  * [Kou Misaki](https://huggingface.co/takkyu2)
  * [Takuya Akiba](https://huggingface.co/iwiwi)
* [Swallow Team](https://swallow-llm.github.io/index.en.html)
  * [Naoki Okazaki](https://www.chokkan.org/index.ja.html)
  * [Youmi Ma](https://www.nlp.c.titech.ac.jp/member/youmi.en.html)
  * [Kakeru Hattori](https://aya-se.vercel.app/)
  * [Kazuki Fujii](https://x.com/okoge_kaz)
  * [Sakae Mizuki](https://s-mizuki-nlp.github.io/)

## License 
This model is derived from Qwen ([Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)) and trained on Gemma data ([Gemma Terms](https://ai.google.dev/gemma/terms), [Prohibited Use](https://ai.google.dev/gemma/prohibited_use_policy)). Use (including commercial) is permitted if you comply with both licenses/policies above.


## Citation

```bibtex
@misc{sakana2025taid,
      title         = {TAID: Temporally Adaptive Interpolated Distillation for Efficient Knowledge Transfer in Language Models}, 
      author.       = {Makoto Shing and Kou Misaki and Han Bao and Sho Yokoi and Takuya Akiba},
      year          = {2025},
      eprint        = {2501.16937},
      archivePrefix = {arXiv},
      primaryClass  = {cs.LG},
      url           = {http://arxiv.org/abs/2501.16937}
}
```
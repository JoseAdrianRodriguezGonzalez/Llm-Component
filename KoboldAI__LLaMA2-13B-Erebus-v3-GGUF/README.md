---
license: llama2
license_name: llama-2
license_link: LICENSE
language:
- en
pipeline_tag: text-generation
inference: false
tags:
- pytorch
- llama
- llama-2
- finetuned
- not-for-all-audiences
---
# LLaMA2-13B-Erebus
This is the GGUF version of this model designed to be used with [Koboldcpp](https://koboldai.org/cpp), the easy and versitile program for AI co-writing and more.
Because this is a co-writing model, you are expected to use the Story Mode inside the KoboldAI Lite interface.

## Model description
This is the third generation of the original Shinen made by Mr. Seeker. The full dataset consists of 8 different sources, all surrounding the "Adult" theme. The name "Erebus" comes from the greek mythology, also named "darkness". This is in line with Shin'en, or "deep abyss". For inquiries, please contact the KoboldAI community. **Warning: THIS model is NOT suitable for use by minors. The model will output X-rated content.**

## Training procedure
LLaMA2-13B-Erebus was trained on 8x A6000 Ada GPU's for a single epoch. No special frameworks have been used.

## Training data
The data can be divided in 8 different datasets:
- Literotica (everything with 3.0/5 or higher)
- Sexstories (everything with 70 or higher)
- Dataset-G (private dataset of X-rated stories)
- Doc's Lab (all stories)
- Lushstories (Editor's pick)
- Swinglifestyle (all stories)
- Pike-v2 Dataset (novels with "adult" rating)
- SoFurry (collection of various animals)

The dataset uses `[Genre: <comma-separated list of genres>]` for tagging.

The full dataset is 2.3B tokens in size. 

## Limitations and biases
Based on known problems with NLP technology, potential relevant factors include bias (gender, profession, race and religion). **Warning: This model has a very strong NSFW bias!**
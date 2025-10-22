"""
Here I´m going to do manually the detection of language impures on prompts genereated by several models, as also, I´m going to generate a report of it
"""
import nltk
from nltk.corpus import stopwords
import re
import pandas as pd
df = pd.read_csv("../../prompts/deepseek+hf_mradermacher_DeepSeek-R1-Distill-Llama-8B.Q8_0.csv")

nltk.download('words')
english_vocab = set(w.lower() for w in nltk.corpus.words.words())
with open("spanish.txt", "r", encoding="utf-8") as f:
    spanish_vocab = set(line.strip().lower() for line in f)
def clean_words(prompt):
    prompt=prompt.replace(",","").replace(":","").replace(";","").replace(".","").lower().strip()
    return prompt.split(" ")
def count_words(language_expected,tokens):
    en_count = sum(1 for t in tokens if t not in spanish_vocab)
    es_count = sum(1 for t in tokens if t in spanish_vocab and t not in english_vocab)
    total = len(tokens)
    if total == 0:
        return {"en": 0, "es": 0, "contamination": 0}

    if language_expected == "es":
        contamination = en_count / total
        en_words=[t for t in tokens if t not in spanish_vocab]
    else:
        contamination = es_count / total
        es_words=[t for t in tokens if t in spanish_vocab and t not in english_vocab]

    return {
        "en": en_count,
        "es": es_count,
        "total": total,
        "contamination": contamination,
        "words": en_words if language_expected=="es" else es_words
    }

for idx,row in df.iterrows():
    prompt = row["Prompt"]
    original_lang = row["Language"]
    print("="*50)
    lista=clean_words(prompt)
    diccio=count_words(original_lang,lista)
    print(diccio)

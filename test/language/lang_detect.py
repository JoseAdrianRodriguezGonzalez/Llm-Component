"""
Here I´m going to do manually the detection of language impures on prompts genereated by several models, as also, I´m going to generate a report of it
"""
import nltk

import re
import pandas as pd
from nltk.stem.snowball import SpanishStemmer,EnglishStemmer
df = pd.read_csv("../../prompts/deepseek+hf_mradermacher_DeepSeek-R1-Distill-Llama-8B.Q8_0.csv")
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('words')
stop_es = set(stopwords.words('spanish'))
stop_en = set(stopwords.words('english'))
english_vocab = set(w.lower() for w in nltk.corpus.words.words())
with open("spanish.txt", "r", encoding="utf-8") as f:
    spanish_vocab = set(line.strip().lower() for line in f)
stem_es=SpanishStemmer()
stems_es = {stem_es.stem(t) for t in spanish_vocab}
def clean_words(prompt):
    tokens = re.findall(r"[a-záéíóúüñ]+", prompt.lower())
    return tokens
stems_es = {stem_es.stem(w) for w in spanish_vocab}
def count_words(language_expected, tokens):
    en_words = []
    es_words = []
    unknown = []


    for t in tokens:
        
        if t in spanish_vocab or stem_es.stem(t) in stems_es or stem_es.stem(t) in spanish_vocab:
            if t not in stop_es:
                es_words.append(t)
        elif t in english_vocab or t not in stop_en:
            en_words.append(t)
        else:
            unknown.append(t)

    total = len(tokens)
    if total == 0:
        return {"en":0, "es":0, "unknown":0, "total":0, "contamination":0, "words":[], "unknown_words":[]}

    if language_expected == "es":
        contamination = len(en_words)/total
        contam_words = en_words
    else:
        contamination = len(es_words)/total
        contam_words = es_words

    return {
        "en": len(en_words),
        "es": len(es_words),
        "unknown": len(unknown),
        "total": total,
        "contamination": round(contamination,3),
        "words": contam_words,
        "unknown_words": unknown
    }

import spacy
nlp_es = spacy.load("es_core_news_sm")
nlp_en = spacy.load("en_core_web_sm")

def count_words_spacy(language_expected, tokens):
    en_words, es_words, unknown = [], [], []

    for t in tokens:
        doc_es = nlp_es(t)
        doc_en = nlp_en(t)

        lemma_es = doc_es[0].lemma_.lower()
        lemma_en = doc_en[0].lemma_.lower()

        if lemma_es in spanish_vocab or t in spanish_vocab:
            es_words.append(t)
        elif lemma_en in english_vocab or t in english_vocab:
            en_words.append(t)
        else:
            unknown.append(t)

    total = len(tokens)
    if total == 0:
        return {"en":0, "es":0, "unknown":0, "total":0, "contamination":0, "words":[], "unknown_words":[]}

    if language_expected == "es":
        contamination = len(en_words)/total
        contam_words = en_words
    else:
        contamination = len(es_words)/total
        contam_words = es_words

    return {
        "en": len(en_words),
        "es": len(es_words),
        "unknown": len(unknown),
        "total": total,
        "contamination": round(contamination,3),
        "words": contam_words,
        "unknown_words": unknown
    }

for idx,row in df.iterrows():
    prompt = row["Prompt"]
    original_lang = row["Language"]
    print("="*50)
    lista=clean_words(prompt)
    diccio=count_words(original_lang,lista)
    print(diccio)
    sp=count_words_spacy(original_lang,lista)
    print(sp)

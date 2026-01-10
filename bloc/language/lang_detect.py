import nltk
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import SpanishStemmer,EnglishStemmer
import os
nltk.download('stopwords')
nltk.download('words')
stop_es = set(stopwords.words('spanish'))
stop_en = set(stopwords.words('english'))
english_vocab = set(w.lower() for w in nltk.corpus.words.words())
with open("spanish.txt", "r", encoding="utf-8") as f:
    spanish_vocab = set(line.strip().lower() for line in f)
stem_es = SpanishStemmer()
stem_en=EnglishStemmer()
stems_es = {stem_es.stem(w) for w in spanish_vocab}
stems_en={stem_en.stem(w) for w in english_vocab}
def clean_words(prompt):
    if not isinstance(prompt, str):
        return []
    tokens = re.findall(r"[a-záéíóúüñA-Z']+", prompt)
    return [t.lower() for t in tokens if len(t) > 2]  # ignorar palabras cortas
def classify_words(tokens):
    en_words, es_words, unknown = [], [], []
    for t in tokens:
        if t in spanish_vocab or stem_es.stem(t) in stems_es:
            es_words.append(t)
        elif t in english_vocab or stem_en.stem(t) in stems_en:
            en_words.append(t)
        else:
            unknown.append(t)

    return en_words, es_words, unknown

def count_words(language_expected, tokens):
    en_words, es_words, unknown = classify_words(tokens)
    total = len(tokens)
    if total == 0:
        return {"en":0, "es":0, "unknown":0, "total":0, "contamination":0, "words":[], "unknown_words":[]}

    if language_expected == "es":
        contam_words = en_words
    else:
        contam_words = es_words

    contamination = round(len(contam_words) / total, 3)

    return {
        "en": len(en_words),
        "es": len(es_words),
        "unknown": len(unknown),
        "total": total,
        "contamination": contamination,
        "words": contam_words,
        "unknown_words": unknown
    }
output_dir = "../../prompts/out"
os.makedirs(output_dir, exist_ok=True)

def save():
    for csv_file in os.listdir("../../prompts"):
        if not csv_file.endswith(".csv"):
            continue
        df = pd.read_csv(os.path.join("../../prompts", csv_file))
        report_rows = []

        for idx, row in df.iterrows():
            prompt = row["Prompt"]
            original_lang = row["Language"]
            tokens = clean_words(prompt)
            stats = count_words(original_lang, tokens)
            report_rows.append({
                "Fila": idx,
                "Prompt": prompt,
                "Idioma original": original_lang,
                **stats
            })

        out_path = os.path.join(output_dir, f"report_{csv_file}")
        pd.DataFrame(report_rows).to_csv(out_path, index=False)
        print(f"Reporte guardado en: {out_path}")
save()

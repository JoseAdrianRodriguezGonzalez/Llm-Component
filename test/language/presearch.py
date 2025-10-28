import fasttext
import pandas as pd
import re
df = pd.read_csv("../../prompts/deepseek+hf_mradermacher_DeepSeek-R1-Distill-Llama-8B.Q8_0.csv")

model = fasttext.load_model("lid.176.bin")
def clean_words(prompt):
    tokens = re.findall(r"[a-záéíóúüñ]+", prompt.lower())
    return tokens
def count_words_fasttext(language_expected, tokens):
    en_words, es_words, unknown = [], [], []

    for t in tokens:
        # fastText necesita texto completo, no solo una palabra pequeña, 
        # pero funciona bien con palabras también
        pred_label, prob = model.predict(t)  # devuelve ('__label__en', 0.95)
        lang = pred_label[0].replace("__label__", "")

        if lang == "es":
            es_words.append(t)
        elif lang == "en":
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
    lista = clean_words(prompt)
    diccio = count_words_fasttext(original_lang, lista)
    print(diccio)

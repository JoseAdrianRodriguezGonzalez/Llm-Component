from lingua import Language, LanguageDetectorBuilder
import pandas as pd
df = pd.read_csv("../prompts/deepseek+hf_mradermacher_DeepSeek-R1-Distill-Llama-8B.Q8_0.csv")
languages = [Language.ENGLISH, Language.SPANISH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
for idx, row in df.iterrows():
    prompt = row["Prompt"]
    original_lang = row["Language"]
    detected_lang = detector.detect_language_of(prompt)
    fragments = detector.detect_multiple_languages_of(prompt)
    print(f"Fila {idx} | original: {original_lang} | dominante detectado: {detected_lang.name}")
    for frag in fragments:
        lang = frag.language.name
        fragment_text = prompt[frag.start_index:frag.end_index]
        snippet = fragment_text.replace("\n", " ")[:50]
        print(f"  {lang}: '{snippet}...'")
#This model is useless
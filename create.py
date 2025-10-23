import pandas as pd
import os

base_path = "Accepted"

models = [m for m in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, m))]

for model in models:
    quantizations = sorted([
        q for q in os.listdir(os.path.join(base_path, model))
        if os.path.isdir(os.path.join(base_path, model, q))
    ])

    for quant in quantizations:
        rows = []
        quant_path = os.path.join(base_path, model, quant)

        for language in sorted(os.listdir(quant_path)):
            lang_path = os.path.join(quant_path, language)

            for file_name in os.listdir(lang_path):
                file_path = os.path.join(lang_path, file_name)
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read().strip()

                rows.append({
                    "Quantization": quant,
                    "Language": language,
                    "Prompt": text
                })

        # Crear DataFrame con una fila por prompt
        df = pd.DataFrame(rows)
        df.to_csv(f"{model}+{quant}.csv", index=False)

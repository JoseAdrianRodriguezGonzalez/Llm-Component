"""
Create csv files for each models
Quantization name | language | prompt
"""
import pandas as pd
import os
models=[model for model in os.listdir("Accepted") if os.path.isdir(os.path.join("Accepted", model))]
#print((models))
quantizations=sorted([(model,quant) for model in models for quant in os.listdir("Accepted/"+model)  if os.path.isdir(os.path.join("Accepted",model,quant))])
for model,quantization in quantizations:
    Quantization=[]
    Language=[]
    Prompt=[]
    rows=[]
    for language in sorted(os.listdir(os.path.join("Accepted",model,quantization))):
        for files in os.listdir(os.path.join("Accepted",model,quantization,language)):
            with open((os.path.join("Accepted",model,quantization,language,files)),"r") as file:
                Quantization.append(quantization)
                Language.append(language)
                Prompt.append(file.read())
    rows.append({"Quantization":Quantization,"Language":Language,"Prompt":Prompt})
    element=pd.DataFrame(rows)
    element.to_csv(f"{model}+{quantization}.csv")
    

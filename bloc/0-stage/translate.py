import json
from transformers import MarianTokenizer,MarianMTModel
import torch 
from tqdm import tqdm
class translator:
    def __init__(self,name="Helsinki-NLP/opus-mt-en-es"):
        self.model_name=name
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(self.device)
        self.tokenizer=MarianTokenizer.from_pretrained(self.model_name,use_safetensors=True)
        self.model=MarianMTModel.from_pretrained(self.model_name,use_safetensors=True).to(self.device)
    def translate(self,text):
        inputs=self.tokenizer(text=text,return_tensors="pt",truncation=True,padding=True).to(self.device)
        outputs=self.tokenizer(**inputs)
        return self.tokenizer.decode(outputs[0],skip_special_tokens=True)
    def translate_batch(self, texts):
        inputs = self.tokenizer(
            texts,
            return_tensors="pt",
            truncation=True,
            padding=True
        ).to(self.device)

        outputs = self.model.generate(**inputs)
        return [self.tokenizer.decode(t, skip_special_tokens=True) for t in outputs]
    def from_jsonl(self,src_file,output_file,batch_size=4):
        results=[]
        batch=[]
        with open(src_file,"r",encoding="utf-8") as file:
            data_list=json.load(file)
            for item in tqdm(data_list,desc="Elementos"):
                batch.append(item)
                if len(batch)==batch_size:
                    results.extend(self._process_batch(batch))
                    batch=[]
            if batch:
                results.extend(self.translate_batch(batch))
        with open(output_file,"w",encoding="utf-8") as f_out:
            json.dump(results,f_out,ensure_ascii=False,indent=False)
    def _process_batch(self, batch):
        texts = []
        structure = []
        for item in batch:
            texts.extend([
                item["card"],
                item["element"],
                item["description"]
            ])
            structure.append(item)
        translations = self.translate_batch(texts)
        results = []
        idx = 0
        for item in structure:
            new_item = item.copy()
            new_item["card"] = translations[idx]; idx += 1
            new_item["element"] = translations[idx]; idx += 1
            new_item["description"] = translations[idx]; idx += 1
            results.append(new_item)
        return results
def run_pipeline():
    tr=translator()
    tr.from_jsonl("data/sample.json","data/sample_es.json")


run_pipeline()
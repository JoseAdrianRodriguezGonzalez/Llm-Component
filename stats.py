from huggingface_hub import HfApi,hf_hub_download
import os
import shutil
"""
This section is for the API's hugging face call.

"""
api = HfApi()



def modelRetrieve():
    """
    Reads a file called models.txt, that contains the name of the models which are text generator
    """
    with open("models.txt","r") as file:
        model_ids=[linea.strip() for linea in file]
        return model_ids
def downloadingReadmes(model_ids):
    """
    Therefore, it reads the name models, will make folders with its name and author or LLm's creator. Will
    download the README.md with a process of reading-writing.
    Therefore, the apu contains the possible tags from eeach model and will be written on a file called tags.txt

    """
    for model_id in model_ids:
        try:
            model_folder=model_id.replace("/","__")
            os.makedirs(model_folder,exist_ok=True)
            readme_path=hf_hub_download(repo_id=model_id,filename="README.md")
            dest_path=os.path.join(model_folder,"README.md")
            with open(readme_path,"r",encoding="utf-8") as src,open(dest_path,"w",encoding="utf-8") as dst:
                dst.write(src.read())
            model_info=api.model_info(model_id)
            tags=model_info.tags
            with open(os.path.join(model_folder,"tags.txt"),"w",encoding="utf-8") as tag:
                tag.write("\n".join(tags))
        except Exception as e:
            print(f"[ERROR] No se pudo acceder a '{model_id}': {e}")
def readTags():
    """
    It will be read the tags from each model and extracted each feature
    """
    modelos_tags={}
    for carpeta in os.listdir("."):
        carpeta_path=os.path.join(".",carpeta)
        tags_path=os.path.join(carpeta_path,"tags.txt")
        if os.path.isdir(carpeta_path) and os.path.isfile(tags_path):
            with open(tags_path,"r",encoding="utf-8") as f:
                tags=[line.strip() for line in f]
                modelos_tags[carpeta]=tags
    return modelos_tags

def moveLang(model_tags):
    """
    Will count the quantity of models who are on english or sapnish, and will make folder to those modelos that contains
    on its tags englsih and spanish
    """
    suma = 0
    for lang in ["en", "es"]:
        os.makedirs(lang, exist_ok=True)

    for modelo, tags in model_tags.items():
        src = os.path.join(".", modelo)
        if "en" in tags:
            dst = os.path.join("en", modelo)
            shutil.move(src, dst)
            suma += 1
        elif "es" in tags:
            dst = os.path.join("es", modelo)
            shutil.move(src, dst)
            suma += 1
    print(f"{sum}/{len(model_tags)}")
if __name__=="__main__":
    with open("models_accepted.txt","w") as file:
        for folders in os.listdir('Accepted'):
            file.write(f"{folders}\n")
        file.write(f"${len(os.listdir('Accepted'))}")
    
    
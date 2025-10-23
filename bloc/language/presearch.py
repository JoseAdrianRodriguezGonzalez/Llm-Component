import os
for files in sorted(os.listdir("../../prompts/")):
    with open("list_actualizada.txt","a+",encoding="utf-8") as file:
        file.write(f"{files} \n")
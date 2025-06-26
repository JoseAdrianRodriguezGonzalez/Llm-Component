---
base_model:
- lianghsun/Llama-3.2-Taiwan-3B-Instruct
language:
- zh
- en
- ja
- ko
- fr
- it
- de
license: llama3.2
tags:
- ROC
- Taiwan
- zh-tw
- llama-factory
new_version: lianghsun/Llama-3.2-Taiwan-3B-Instruct
pipeline_tag: text-generation
library_name: llama.cpp
---

# Model Card for lianghsun/Llama-3.2-Taiwan-3B-Instruct-GGUF

<!-- Provide a quick summary of what the model is/does. -->
<a href="https://discord.gg/EAWvwDdwpP" target="_blank">[👋 歡迎加入 Discord 討論 🎉]</a>

![image/png](https://cdn-uploads.huggingface.co/production/uploads/618dc56cbc345ca7bf95f3cd/sgphjAJEkoBgFAk-e2g5T.png)
<div align="center">圖像後製來自 <a href="https://online.visual-paradigm.com/">VisuaParadigm</a>：站在玉山上的量化 🦙 。
</div>


透過 [llama.cpp](https://github.com/ggerganov/llama.cpp) 將 [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct) 版本轉成 `.gguf` 和各種量化版本模型。

<details>
  <summary><b>Model Change Log</b></summary>
  
  | Update Date  | Model Version         | Key Changes                         |
  |--------------|-----------------------|-------------------------------------|
  | 2025-01-01   | v2025.01.01          | This version corresponds to the `v2025.01.01` release of [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct).  |
  | 2024-12-11   | v2024.12.11           | This version corresponds to the `v2024.11.27` release of [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct). |
  
</details>

## More Information

請參考不同 tag 選擇對照的原始非量化的版本，最新的 main 分支對映的是 `v2025.01.01` 版本，有關原始非量化版本請參考原始模型 [lianghsun/Llama-3.2-Taiwan-3B-Instruct](https://huggingface.co/lianghsun/Llama-3.2-Taiwan-3B-Instruct) 介紹。

**已知問題：** 量化後的模型會有機率輸出全部簡體中文的情況，此問題目前尚未深入研究原因。

### Issuses 
#### How to use in Ollama
根據 [Issue：ollama 直接run gguf會跑出文不對題](https://discord.com/channels/1310544431983759450/1327811803085799534) 討論串， [@k1dave6412](https://huggingface.co/k1dave6412) 查出原因是要調整預設的對話模板（chat template），故我們在 repo 內有放置一個 `template` 的檔案來修正這個問題，但如果你要客制你的對話模板，請照著 Ollama 的 [Template](https://github.com/ollama/ollama/blob/main/docs/modelfile.md) 設定。 

## Model Card Authors

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang)


## Model Card Contact

[Huang Liang Hsun](https://www.linkedin.com/in/lianghsunhuang)

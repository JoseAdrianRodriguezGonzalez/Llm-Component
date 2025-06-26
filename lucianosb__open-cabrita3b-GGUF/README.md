---
inference: false
language:
- pt
license: apache-2.0
model_creator: 22H
model_link: https://huggingface.co/22h/open-cabrita3b
model_name: Open Cabrita 3B
model_type: llama
quantized_by: lucianosb
pipeline_tag: text-generation
---

# Open Cabrita 3B - GGUF
- Criador do Modelo: [22h](https://huggingface.co/22h)
- Modelo Original: [Open Cabrita 3B](https://huggingface.co/22h/open-cabrita3b)
- Artigo: [CABRITA: CLOSING THE GAP FOR FOREIGN LANGUAGES](https://arxiv.org/pdf/2308.11878.pdf)

## Arquivos Incluídos

| Nome | Método Quant | Bits | Tamanho  | Desc |
| ---- | ---- | ---- | ---- | ----- |
| [opencabrita3b-q4_0.gguf](https://huggingface.co/lucianosb/open-cabrita3b-GGUF/blob/main/opencabrita3b-q4_0.gguf) | q4_0 | 4 | 1.94 GB | Quantização em 4-bit. |
| [opencabrita3b-q4_1.gguf](https://huggingface.co/lucianosb/open-cabrita3b-GGUF/blob/main/opencabrita3b-q4_1.gguf) | q4_1 | 4 | 2.14 GB | Quantização em 4-bit. Acurácia maior que q4_0 mas não tão boa quanto q5_0. Inferência mais rápida que os modelos q5. |
| [opencabrita3b-q5_0.gguf](https://huggingface.co/lucianosb/open-cabrita3b-GGUF/blob/main/opencabrita3b-q5_0.gguf) | q5_0 | 5 | 2.34 GB | Quantização em 5-bit. Melhor acurácia, maior uso de recursos, inferência mais lenta. |
| [opencabrita3b-q5_1.gguf](https://huggingface.co/lucianosb/open-cabrita3b-GGUF/blob/main/opencabrita3b-q5_1.gguf) | q5_1 | 5 | 2.53 GB | Quantização em 5-bit. Ainda Melhor acurácia, maior uso de recursos, inferência mais lenta. |
| [opencabrita3b-q8_0.gguf](https://huggingface.co/lucianosb/open-cabrita3b-GGUF/blob/main/opencabrita3b-q8_0.gguf) | q8_0 | 8 | 3.52 GB | Quantização em 8-bit. Quase indistinguível do float16. Usa muitos recursos e é mais lento. |

**Observação**: os valores de RAM acima não pressupõem descarregamento de GPU. Se as camadas forem descarregadas para a GPU, isso reduzirá o uso de RAM e usará VRAM.

## Como executar com `llama.cpp`

Usei o seguinte comando. Ajuste para suas necessidades:

```
./main -m ./models/open-cabrita3b/opencabrita3b-q5_1.gguf --color --temp 0.5 -n 256 -p "### Instrução: {comando} ### Resposta: "
```

Para compreender os parâmetros, veja [a documentação do llama.cpp](https://github.com/ggerganov/llama.cpp/blob/master/examples/main/README.md)

Experimente gratuitamente no Google Colab: [Open_Cabrita_llamacpp_5_1.ipynb](https://colab.research.google.com/github/lucianosb/cabrita-notebooks/blob/main/Open_Cabrita_llamacpp_5_1.ipynb)

## Sobre o formato GGUF

GGUF é um novo formato introduzido pela equipe llama.cpp em 21 de agosto de 2023. É um substituto para o GGML, que não é mais suportado pelo llama.cpp.

O principal benefício do GGUF é que ele é um formato extensível e à prova de futuro que armazena mais informações sobre o modelo como metadados. Ele também inclui código de tokenização significativamente melhorado, incluindo pela primeira vez suporte total para tokens especiais. Isso deve melhorar o desempenho, especialmente com modelos que usam novos tokens especiais e implementam modelos de prompt personalizados.

Aqui está uma lista de clientes e bibliotecas que são conhecidos por suportar GGUF:

- [llama.cpp](https://github.com/ggerganov/llama.cpp).
- [text-generation-webui](https://github.com/oobabooga/text-generation-webui), a interface web mais amplamente utilizada. Suporta GGUF com aceleração GPU via backend ctransformers - backend llama-cpp-python deve funcionar em breve também.
- [KoboldCpp](https://github.com/LostRuins/koboldcpp), agora suporta GGUF a partir da versão 1.41! Uma poderosa interface web GGML, com aceleração total da GPU. Especialmente bom para contar histórias.
- [LM Studio](https://lmstudio.ai), versão 0.2.2 e posteriores suportam GGUF. Uma GUI local totalmente equipada com aceleração GPU em ambos Windows (NVidia e AMD) e macOS.
- [LoLLMS Web UI](https://github.com/ParisNeo/lollms-webui), agora deve funcionar, escolha o backend c_transformers. Uma ótima interface web com muitos recursos interessantes. Suporta aceleração GPU CUDA.
- [ctransformers](https://github.com/marella/ctransformers), agora suporta GGUF a partir da versão 0.2.24! Uma biblioteca Python com aceleração GPU, suporte LangChain e servidor AI compatível com OpenAI.
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python), suporta GGUF a partir da versão 0.1.79. Uma biblioteca Python com aceleração GPU, suporte LangChain e servidor API compatível com OpenAI.
- [candle](https://github.com/huggingface/candle), adicionou suporte GGUF em 22 de agosto. Candle é um framework ML Rust com foco em desempenho, incluindo suporte GPU e facilidade de uso.
- [LocalAI](https://github.com/go-skynet/LocalAI), adicionou suporte GGUF em 23 de agosto. LocalAI provê uma API Rest para modelos LLM e de geração de imagens.

## Template

````
### Instrução:
{prompt}

### Resposta:
````
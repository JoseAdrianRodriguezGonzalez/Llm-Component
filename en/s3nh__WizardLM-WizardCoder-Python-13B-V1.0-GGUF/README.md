
---
license: openrail
pipeline_tag: text-generation
library_name: transformers
language:
- zh
- en
---


## Original model card 

Buy me a coffee if you like this project ;)
<a href="https://www.buymeacoffee.com/s3nh"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg" alt=""></a>

#### Description 

GGUF Format model files for [This project](https://huggingface.co/WizardLM/WizardCoder-Python-13B-V1.0).

### GGUF Specs 

GGUF is a format based on the existing GGJT, but makes a few changes to the format to make it more extensible and easier to use. The following features are desired:

Single-file deployment: they can be easily distributed and loaded, and do not require any external files for additional information.
Extensible: new features can be added to GGML-based executors/new information can be added to GGUF models without breaking compatibility with existing models.
mmap compatibility: models can be loaded using mmap for fast loading and saving.
Easy to use: models can be easily loaded and saved using a small amount of code, with no need for external libraries, regardless of the language used.
Full information: all information needed to load a model is contained in the model file, and no additional information needs to be provided by the user.
The key difference between GGJT and GGUF is the use of a key-value structure for the hyperparameters (now referred to as metadata), rather than a list of untyped values. 
This allows for new metadata to be added without breaking compatibility with existing models, and to annotate the model with additional information that may be useful for
inference or for identifying the model.

### Perplexity params

Model	Measure	Q2_K	Q3_K_S	Q3_K_M	Q3_K_L	Q4_0	Q4_1	Q4_K_S	Q4_K_M	Q5_0	Q5_1	Q5_K_S	Q5_K_M	Q6_K	Q8_0	F16
7B	perplexity	6.7764	6.4571	6.1503	6.0869	6.1565	6.0912	6.0215	5.9601	5.9862	5.9481	5.9419	5.9208	5.9110	5.9070	5.9066
13B	perplexity	5.8545	5.6033	5.4498	5.4063	5.3860	5.3608	5.3404	5.3002	5.2856	5.2706	5.2785	5.2638	5.2568	5.2548	5.2543



### inference 


TODO

# Original model card

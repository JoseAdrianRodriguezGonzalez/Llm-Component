---
datasets:
- msaad02/formatted-ss-cleaned-brockport-qa
language:
- en
pipeline_tag: text-generation
---

**VERIFIED 8/25/23**
# BrockportGPT GGUF LLaMA2 Finetune

> This is a quantized version of the original model, found at "msaad02/llama2_7b_brockportgpt"

This model is part of my thesis to make a question-answering bot for SUNY Brockport. The data used for finetuning is a subset of the question database I generated, and is also available on my huggingface account.

For more information, see my [github repo](https://github.com/msaad02/honors-thesis) for the project.

## Examples

>Are SAT scores required?
>>SAT scores are not required for admission, but test scores are used as part of Brockport's holistic review process to make admissions decisions.

>Who can I contact for help with financial aid?
>>You can contact the financial aid office at SUNY Brockport for assistance with financial aid. They are available to answer any questions and help you navigate the financial aid process.


## Prompting

This prompting style is what was used for finetuning:

>Below is an inquiry related to SUNY Brockport - from academics, admissions, and faculty support to student life. Prioritize accuracy and brevity.
>
>\### Instruction:\
>{question}
>
>\### Response:\
>{response}

## Usage

GGUF is the current state of the art model, started being supported for llama.cpp on August 23rd, 2023. Today is August 25th, so pretty recent, you could say! GGML is its predacessor and has since been depricated.

To use, I recommend using ctransformers, but you can also use the llama.cpp library directly as well. Be sure that you have the most updated versions, ctransformers required version >=0.2.24 for gguf support, and llama.cpp python bindings does not yet support it -- you need to be careful

```python
from ctransformers import AutoModelForCausalLM
import textwrap

llm = AutoModelForCausalLM.from_pretrained(
    model_path_or_repo_id="msaad02/llama2_7b_brockportgpt_gguf",
    model_file="brockportgpt-7b-q4_1.gguf",
    model_type="llama"
)

def qa(text: str, full = False):
    # textwrap.dedent gets rid of indenting at the start of each newline
    text = textwrap.dedent(f"""\
        Below is an inquiry related to SUNY Brockport - from academics, admissions, and faculty support to student life. Prioritize accuracy and brevity.

        ### Instruction:
        {text}

        ### Response:
        """)
    
    response = llm(text, max_new_tokens=256)
    response = (text + response) if full else response

    return response

qa("How do I apply?")
> You can apply for admission to the University by completing an application online or by mailing a paper copy of the application to SUNY Brockport (available only through PDF upload).

print(qa("How do I apply?", full=True))
> Below is an inquiry related to SUNY Brockport - from academics, admissions, and faculty support to student life. Prioritize accuracy and brevity.
> 
> ### Instruction:
> How do I apply?
> 
> ### Response:
> You can apply for admission to the English department at SUNY Brockport by following the application process outlined on their website.
```
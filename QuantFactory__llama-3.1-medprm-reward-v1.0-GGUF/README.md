
---

library_name: transformers
license: mit
tags:
- medical
- biomedical
- process-reward-model
- medical-ai
- retrieval-augmented-generation
pipeline_tag: text-generation

---

[![QuantFactory Banner](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiuCm7c8lEwEJuRey9kiVZsRn2W-b4pWlu3-X534V3YmVuVc2ZL-NXg2RkzSOOS2JXGHutDuyyNAUtdJI65jGTo8jT9Y99tMi4H4MqL44Uc5QKG77B0d6-JfIkZHFaUA71-RtjyYZWVIhqsNZcx8-OMaA?key=xt3VSDoCbmTY7o-cwwOFwQ)](https://hf.co/QuantFactory)


# QuantFactory/llama-3.1-medprm-reward-v1.0-GGUF
This is quantized version of [dmis-lab/llama-3.1-medprm-reward-v1.0](https://huggingface.co/dmis-lab/llama-3.1-medprm-reward-v1.0) created using llama.cpp

# Original Model Card


# Med-PRM-Reward (Version 1.0)
🚀 Med-PRM-Reward is among the first Process Reward Models (PRMs) specifically designed for the medical domain. Unlike conventional PRMs, it enhances its verification capabilities by integrating clinical knowledge through retrieval-augmented generation (RAG). Med-PRM-Reward demonstrates exceptional performance in scaling-test-time computation, particularly outperforming majority‐voting ensembles on complex medical reasoning tasks. Moreover, its scalability is not limited to Llama-3.1-8B-Instruct: it delivers similarly outstanding results in scaling-test-time computation across multiple other medical‐specialized models. Notably, when combined with llama-3-meerkat-8b-v1.0, it became the first 8B model framework to surpass a score of 80 on the MedQA (4-option) benchmark.

📄 Paper: [Med-PRM-Reward: Medical Reasoning Models with Stepwise, Guideline‑verified Process Rewards](https://huggingface.co/papers/2506.11474)

## Quick Start
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "dmis-lab/llama-3.1-medprm-reward-v1.0"
device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"
).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_id)


plus_id = tokenizer(" +", add_special_tokens=False)["input_ids"][0]
minus_id = tokenizer(" -", add_special_tokens=False)["input_ids"][0]

def get_prob(text: str, special_char: str = " ки"):
    encoded = tokenizer(text, return_tensors="pt", add_special_tokens=True)
    input_ids = encoded["input_ids"].to(device)
    attention_mask = encoded["attention_mask"].to(device)
    with torch.no_grad():
        logits = model(input_ids, attention_mask=attention_mask).logits[0]
    offsets = tokenizer(text, return_offsets_mapping=True)["offset_mapping"]
    positions = [
        i for i, (s, e) in enumerate(offsets[0])
        if text[s:e] == special_char
    ]
    plus_probs = []
    for pos in positions:
        if pos < logits.size(0):
            pair = torch.stack([logits[pos][plus_id], logits[pos][minus_id]])
            probs = torch.softmax(pair, dim=0)
            plus_probs.append(probs[0].item())
    min_plus = min(plus_probs) if plus_probs else None
    final_plus = plus_probs[-1] if plus_probs else None
    return {
        "plus_probs": plus_probs,
        "min_plus_prob": min_plus,
        "final_plus_prob": final_plus
    }


docs = ["Document 1: Causes of Posterior Urethral Valves.  The valves can block the outflow of urine through the urethra, leading to damage in the bladder, ureters and kidneys. However, it is important to note that PUV occurs randomly by chance and is not caused by anything a mother did or did not do during pregnancy.In the womb, if the baby is unable to urinate due to PUV, there might be a deficiency in amniotic fluid, known as oligohydramnios. A major concern for oligohydramnios is the lack of proper lung development, called lung hypoplasia",
"Document 2: Amniotic Fluid Index -- Pathophysiology -- Polyhydramnios. Polyhydramnios, or increased amniotic fluid volume, also has a number of potential causes, with two primary common mechanisms: decreased fetal swallowing of amniotic fluid, or increased fetal production of amniotic fluid"]
question = ("A 29-year-old G1P0 female presents at 22 weeks gestation for her first prenatal care appointment. Physical exam demonstrates a uterine size greater than expected for her gestational age and taut, shiny skin with scattered striae on her abdomen. Ultrasound examination of the fetus reveals 2.5 L of amniotic fluid (normal 1.5-2.0 L) with an amniotic fluid index (AFI) of 34 (normal AFI 20-25). Which of the following fetal abnormalities or dysfunctions could have contributed to these abnormal ultrasound findings? 

(A) Renal agenesis
(B) Pulmonary hypoplasia
(C) Duodenal atresia
(D) Posterior urethral valve
(E) Polycystic kidney disease")
explanation = ("Step 1:  The patient's uterine size is greater than expected for her gestational age, which could indicate an issue with fetal growth, such as macrosomia or polyhydramnios. ки Step 2:  The physical examination of the patient reveals taut, shiny skin with scattered striae on her abdomen, which is indicative of rapid weight gain, often associated with polyhydramnios. ки Step 3:  The ultrasound findings show an increased volume of amniotic fluid of 2.5 L, which is above the normal range of 1.5-2.0 L, and an amniotic fluid index (AFI) of 34, also higher than the normal range of 20-25. ки Step 4:  Polyhydramnios is characterized by an excessive accumulation of amniotic fluid, and it is often associated with fetal or maternal conditions that limit fetal swallowing or increase fetal urine production. ки Step 5:  Among the available options, posterior urethral valve (D) is a condition where the urethra is partially blocked, leading to an obstruction in the urinary tract, which can result in increased fetal urine production and subsequent polyhydramnios. ки Step 6:  Considering the options provided, posterior urethral valve is a condition that could have contributed to the abnormal ultrasound findings due to its association with increased fetal urine production and polyhydramnios. The answer is D. ки")

doc_block = "

".join(docs) + "

"
user_content = f"{doc_block}Question: {question}

Explanation: {explanation}"
system_prompt = (
        "You are an evaluator assessing the logicality and validity of the reasoning in each step of the given explanation. "
        "In order to support the evaluation, the relevant documents, the question, and the explanation are provided sequentially. "
        "If the reasoning contains errors, output - after that step. If the reasoning in a step is logical and valid, output + after that step. "
)
raw = tokenizer.apply_chat_template(
    [{"role": "system", "content": system_prompt},
     {"role": "user",   "content": user_content}],
    tokenize=False,
    add_generation_prompt=True
)

scores = get_prob(raw)
print("Plus probabilities per step:", scores["plus_probs"])
print("Min plus probability :", scores["min_plus_prob"])
print("Final plus probability :", scores["final_plus_prob"])
```

## Evaluation
Across seven medical benchmarks, we conducted scaling‐test‐time computation using solutions generated by the Med-PRM-policy model, evaluating 64 solutions per question.

### Reference

## Acknowledgement

## Contact
Feel free to email jhyun0414@hanyang.ac.kr if you have any questions.


---

base_model:
- meta-llama/Llama-3.1-8B
language:
- en
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
- security

---

[![QuantFactory Banner](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeiuCm7c8lEwEJuRey9kiVZsRn2W-b4pWlu3-X534V3YmVuVc2ZL-NXg2RkzSOOS2JXGHutDuyyNAUtdJI65jGTo8jT9Y99tMi4H4MqL44Uc5QKG77B0d6-JfIkZHFaUA71-RtjyYZWVIhqsNZcx8-OMaA?key=xt3VSDoCbmTY7o-cwwOFwQ)](https://hf.co/QuantFactory)


# QuantFactory/Foundation-Sec-8B-GGUF
This is quantized version of [fdtn-ai/Foundation-Sec-8B](https://huggingface.co/fdtn-ai/Foundation-Sec-8B) created using llama.cpp

# Original Model Card


# Foundation-Sec-8B - Model Card

## Model Information

Foundation-Sec-8B (Llama-3.1-FoundationAI-SecurityLLM-base-8B) is an open-weight, 8-billion parameter base language model specialized for cybersecurity applications. It extends Llama-3.1-8B model through continued pretraining on a curated corpus of cybersecurity-specific text, including threat intelligence reports, vulnerability databases, incident response documentation, and security standards. It has been trained to understand security concepts, terminology, and practices across multiple security domains. The model is designed to serve as a domain-adapted base model for use in applications such as threat detection, vulnerability assessment, security automation, and attack simulation. Foundation-Sec-8B enables organizations to build AI-driven security tools that can be deployed locally, reducing dependency on cloud-based AI services while maintaining high performance on security-related tasks.

- **Model Name:** Foundation-Sec-8B (Llama-3.1-FoundationAI-SecurityLLM-base-8B)
- **Model Developer:** Amin Karbasi and team at Foundation AI — Cisco
- **Technical Report:** [`https://arxiv.org/abs/2504.21039`](https://arxiv.org/abs/2504.21039)
- **Model Card Contact:** For questions about the team, model usage, and future directions, contact [`karbasi@cisco.com`](mailto:karbasi@cisco.com). For technical questions about the model, please contact [`paulkass@cisco.com`](mailto:paulkass@cisco.com).
- **Model Release Date:** April 28, 2025
- **Supported Language(s):** English
- **Model Architecture:** Auto-regressive language model that uses an optimized transformer architecture (Meta Llama-3.1-8B backbone)
- **Training Objective:** Continued pre-training on cybersecurity-specific corpus
- **Training Data Status:** This is a static model trained on an offline dataset. Future versions of the tuned models will be released on updated data.
- **License:** Apache 2.0
    
    

## Intended Use

### Intended Use Cases

Foundation-Sec-8B is designed for security practitioners, researchers, and developers building AI-powered security workflows and applications. Foundation-Sec-8B is optimized for three core use case categories:

- **SOC Acceleration**: Automating triage, summarization, case note generation, and evidence collection.
- **Proactive Threat Defense**: Simulating attacks, prioritizing vulnerabilities, mapping TTPs, and modeling attacker behavior.
- **Engineering Enablement**: Providing security assistance, validating configurations, assessing compliance evidence, and improving security posture.

The model is intended for local deployment in environments prioritizing data security, regulatory compliance, and operational control.

### Downstream Use

Foundation-Sec-8B can be used directly for security-related language tasks and serves as a strong starting point for fine-tuning across a variety of cybersecurity workflows. Example downstream applications include:

- Summarization
    - Summarizing detection playbooks and incident reports
    - Consolidating fragmented analyst notes into structured case summaries
- Classification
    - Mapping threats to MITRE ATT&CK techniques
    - Prioritizing vulnerabilities based on contextual risk
    - Classifying security-relevant emails and leaked file contents
- Named Entity Recognition
    - Extracting compliance evidence from documents
    - Building network behavior profiles from technical manuals
- Question & Answer
    - Assisting SOC analysts with alert triage and investigation
    - Responding to cloud security and software compliance queries
- Reasoning and Text Generation
    - Generating red-team attack plans and threat models
    - Predicting attacker next steps in active investigations
    - Enriching vulnerability scan results with contextual insights

For questions or assistance with fine-tuning Foundation-Sec-8B, please contact **Paul Kassianik** (paulkass@cisco.com) or **Dhruv Kedia** (dkedia@cisco.com).

### Out-of-Scope Use

The following uses are out-of-scope and are neither recommended nor intended use cases:

1. **Generating harmful content** - The model should not be used to:
    - Generate malware or other malicious code
    - Create phishing content or social engineering scripts
    - Develop attack plans targeting specific organizations
    - Design exploitation techniques for vulnerabilities without legitimate security research purposes
2. **Critical security decisions without human oversight** - The model should not be used for:
    - Autonomous security decision-making without human review
    - Critical infrastructure protection without expert supervision
    - Final determination of security compliance without human verification
    - Autonomous vulnerability remediation without testing
3. **Legal or medical advice** - The model is not qualified to provide:
    - Legal advice regarding security regulations, compliance requirements, or intellectual property disputes
    - Legal advice regarding security issues that would reference legal statutes, precedents, or case law necessary to provide legal advice
    - Medical advice regarding health impacts of security incidents
4. **Non-security use cases** - The model is specifically optimized for cybersecurity and may not perform as well on general tasks as models trained for broader applications.
5. **Violation of Laws or Regulations** - Any use that violates applicable laws or regulations.

## How to Get Started with the Model

Use the code below to get started with the model.

```python
# Import the required libraries
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("fdtn-ai/Foundation-Sec-8B")
model = AutoModelForCausalLM.from_pretrained("fdtn-ai/Foundation-Sec-8B")

# Example: Matching CWE to CVE IDs
prompt="""CVE-2021-44228 is a remote code execution flaw in Apache Log4j2 via unsafe JNDI lookups (“Log4Shell”). The CWE is CWE-502.

CVE-2017-0144 is a remote code execution vulnerability in Microsoft’s SMBv1 server (“EternalBlue”) due to a buffer overflow. The CWE is CWE-119.

CVE-2014-0160 is an information-disclosure bug in OpenSSL’s heartbeat extension (“Heartbleed”) causing out-of-bounds reads. The CWE is CWE-125.

CVE-2017-5638 is a remote code execution issue in Apache Struts 2’s Jakarta Multipart parser stemming from improper input validation of the Content-Type header. The CWE is CWE-20.

CVE-2019-0708 is a remote code execution vulnerability in Microsoft’s Remote Desktop Services (“BlueKeep”) triggered by a use-after-free. The CWE is CWE-416.

CVE-2015-10011 is a vulnerability about OpenDNS OpenResolve improper log output neutralization. The CWE is"""

# Tokenize the input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate the response
outputs = model.generate(
    inputs["input_ids"],
    max_new_tokens=3,
    do_sample=True,
    temperature=0.1,
    top_p=0.9,
)

# Decode and print the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
response = response.replace(prompt, "").strip()
print(response)
```

## Training and Evaluation

### Training Data

Foundation-sec-8B was pretrained on approximately **5.1 billion tokens** of cybersecurity-specific data curated in-house by Cisco’s Foundation AI team. The dataset was meticulously collected from public sources on the web. 

The pre-training corpus was built through a multi-stage pipeline that included large-scale web crawling, relevancy filtering, deduplication, and quality filtering.

**Data cutoff:** April 10th, 2025.

More detailed methodology is available in the technical report. 

### Training Setup

Foundation-sec-8B is based on the **Llama 3.1 8B** architecture. Pre-training was performed on Cisco Foundation AI’s internal compute cluster.

Key training details:

- **Continued pretraining** for cybersecurity specialization
- **4096-token** sequence length
- **Optimizer:** AdamW

More detailed methodology is available in the technical report. 

### Evaluation

Foundation-sec-8B was benchmarked on cybersecurity and general reasoning tasks, using a standardized 5-shot prompting setup (temperature = 0.3).

| **Benchmark** | **Foundation-sec-8B** | **Llama 3.1 8B** | **Llama 3.1 70B** |
| --- | --- | --- | --- |
| CTI-MCQA | 67.39 | 64.14 | 68.23 |
| CTI-RCM | 75.26 | 66.43 | 72.66 |

**Benchmark Overview:**

- **CTI-MCQA:** 2,500 multiple-choice questions testing cybersecurity knowledge across frameworks like MITRE ATT&CK, NIST, GDPR, and threat intelligence best practices.
- **CTI-RCM:** 900+ vulnerability root cause mapping examples linking CVEs to CWE categories, assessing deep understanding of security weaknesses.

**Key highlights:**

- **+3 to +9 point gains** over Llama-3.1-8B across security-specific benchmarks.
- **Comparable or better** performance than Llama-3.1-70B on cyber threat intelligence tasks.
- **Minimal drop (~2%)** in general language reasoning (MMLU) despite cybersecurity specialization.

For full benchmark details and evaluation methodology, please refer to the technical report. 

## Limitations

Foundation-Sec-8B has several limitations that users should be aware of:

1. **Domain-specific knowledge limitations**:
    - Foundation-Sec-8B may not be familiar with recent vulnerabilities, exploits, or novel attack vectors or security technologies released after its training cutoff date
    - Knowledge of specialized or proprietary security systems or tools may be limited
2. **Potential biases**:
    - The model may reflect biases present in security literature and documentation
    - The model may be trained on known attack patterns and have difficulty recognizing novel attack vectors
    - Security practices and recommendations may be biased toward certain technological ecosystems
    - Geographic and cultural biases in security approaches may be present
3. **Security risks**:
    - The model cannot verify the identity or intentions of users
    - Adversarial prompting techniques might potentially bypass safety mechanisms
    - The model may unintentionally provide information that could be misused if proper prompting guardrails are not implemented
4. **Contextual blindness:**
    - The model may struggle to understand the complex interrelationships between systems, users, and data in order to provide accurate context.
5. **Technical limitations**:
    - Performance varies based on how security concepts are described in prompts
    - May not fully understand complex, multi-step security scenarios without clear explanation
    - Cannot access external systems or actively scan environments
    - Cannot independently verify factual accuracy of its outputs
6. **Ethical considerations**:
    - Dual-use nature of security knowledge requires careful consideration of appropriate use cases
    

### Recommendations

To address the limitations of Foundation-Sec-8B, we recommend:

1. **Human oversight**:
    - Always have qualified security professionals review model outputs before implementation
    - Use the model as an assistive tool rather than a replacement for expert human judgment
    - Implement a human-in-the-loop approach for security-critical applications
2. **System design safeguards**:
    - Implement additional validation layers for applications built with this model
    - Consider architectural constraints that limit the model's ability to perform potentially harmful actions (excessive agency)
    - Deploy the model in environments with appropriate access controls
3. **Prompt engineering**:
    - Use carefully designed prompts that encourage ethical security practices
    - Include explicit instructions regarding responsible disclosure and ethical hacking principles
    - Structure interactions to minimize the risk of inadvertently harmful outputs
4. **Knowledge supplementation**:
    - Supplement the model with up-to-date security feeds and databases
    - Implement retrieval-augmented generation for current threat intelligence sources
5. **Usage policies**:
    - Develop and enforce clear acceptable use policies for applications using this model
    - Implement monitoring and auditing for high-risk applications
    - Create documentation for end users about the model's limitations

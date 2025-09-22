---
base_model: meta-llama/Llama-3.2-1B-Instruct
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
pipeline_tag: text-generation
tags:
- facebook
- meta
- pytorch
- llama
- llama-3
- llama-cpp
- gguf-my-repo
extra_gated_prompt: "### LLAMA 3.2 COMMUNITY LICENSE AGREEMENT\n\nLlama 3.2 Version\
  \ Release Date: September 25, 2024\n\n“Agreement” means the terms and conditions\
  \ for use, reproduction, distribution  and modification of the Llama Materials set\
  \ forth herein.\n\n“Documentation” means the specifications, manuals and documentation\
  \ accompanying Llama 3.2 distributed by Meta at https://llama.meta.com/doc/overview.\n\
  \n“Licensee” or “you” means you, or your employer or any other person or entity\
  \ (if you are  entering into this Agreement on such person or entity’s behalf),\
  \ of the age required under applicable laws, rules or regulations to provide legal\
  \ consent and that has legal authority to bind your employer or such other person\
  \ or entity if you are entering in this Agreement on their behalf.\n\n“Llama 3.2”\
  \ means the foundational large language models and software and algorithms, including\
  \ machine-learning model code, trained model weights, inference-enabling code, training-enabling\
  \ code, fine-tuning enabling code and other elements of the foregoing distributed\
  \ by Meta at  https://www.llama.com/llama-downloads.\n\n“Llama Materials” means,\
  \ collectively, Meta’s proprietary Llama 3.2 and Documentation (and  any portion\
  \ thereof) made available under this Agreement.\n\n“Meta” or “we” means Meta Platforms\
  \ Ireland Limited (if you are located in or,  if you are an entity, your principal\
  \ place of business is in the EEA or Switzerland)  and Meta Platforms, Inc. (if\
  \ you are located outside of the EEA or Switzerland). \n\nBy clicking “I Accept”\
  \ below or by using or distributing any portion or element of the Llama Materials,\
  \ you agree to be bound by this Agreement.\n\n1. License Rights and Redistribution.\n\
  a. Grant of Rights. You are granted a non-exclusive, worldwide,  non-transferable\
  \ and royalty-free limited license under Meta’s intellectual property or other rights\
  \  owned by Meta embodied in the Llama Materials to use, reproduce, distribute,\
  \ copy, create derivative works  of, and make modifications to the Llama Materials.\
  \  \nb. Redistribution and Use.  \ni. If you distribute or make available the Llama\
  \ Materials (or any derivative works thereof),  or a product or service (including\
  \ another AI model) that contains any of them, you shall (A) provide a copy of this\
  \ Agreement with any such Llama Materials; and (B) prominently display “Built with\
  \ Llama” on a related website, user interface, blogpost, about page, or product\
  \ documentation. If you use the Llama Materials or any outputs or results of the\
  \ Llama Materials to create, train, fine tune, or otherwise improve an AI model,\
  \ which is distributed or made available, you shall also include “Llama” at the\
  \ beginning of any such AI model name.\nii. If you receive Llama Materials, or any\
  \ derivative works thereof, from a Licensee as part of an integrated end user product,\
  \ then Section 2 of this Agreement will not apply to you. \niii. You must retain\
  \ in all copies of the Llama Materials that you distribute the  following attribution\
  \ notice within a “Notice” text file distributed as a part of such copies:  “Llama\
  \ 3.2 is licensed under the Llama 3.2 Community License, Copyright © Meta Platforms,\
  \ Inc. All Rights Reserved.”\niv. Your use of the Llama Materials must comply with\
  \ applicable laws and regulations (including trade compliance laws and regulations)\
  \ and adhere to the Acceptable Use Policy for the Llama Materials (available at\
  \ https://www.llama.com/llama3_2/use-policy), which is hereby  incorporated by reference\
  \ into this Agreement.\n  \n2. Additional Commercial Terms. If, on the Llama 3.2\
  \ version release date, the monthly active users of the products or services made\
  \ available by or for Licensee, or Licensee’s affiliates,  is greater than 700 million\
  \ monthly active users in the preceding calendar month, you must request  a license\
  \ from Meta, which Meta may grant to you in its sole discretion, and you are not\
  \ authorized to exercise any of the rights under this Agreement unless or until\
  \ Meta otherwise expressly grants you such rights.\n3. Disclaimer of Warranty. UNLESS\
  \ REQUIRED BY APPLICABLE LAW, THE LLAMA MATERIALS AND ANY OUTPUT AND  RESULTS THEREFROM\
  \ ARE PROVIDED ON AN “AS IS” BASIS, WITHOUT WARRANTIES OF ANY KIND, AND META DISCLAIMS\
  \ ALL WARRANTIES OF ANY KIND, BOTH EXPRESS AND IMPLIED, INCLUDING, WITHOUT LIMITATION,\
  \ ANY WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR A PARTICULAR\
  \ PURPOSE. YOU ARE SOLELY RESPONSIBLE FOR DETERMINING THE APPROPRIATENESS OF USING\
  \ OR REDISTRIBUTING THE LLAMA MATERIALS AND ASSUME ANY RISKS ASSOCIATED WITH YOUR\
  \ USE OF THE LLAMA MATERIALS AND ANY OUTPUT AND RESULTS.\n4. Limitation of Liability.\
  \ IN NO EVENT WILL META OR ITS AFFILIATES BE LIABLE UNDER ANY THEORY OF LIABILITY,\
  \  WHETHER IN CONTRACT, TORT, NEGLIGENCE, PRODUCTS LIABILITY, OR OTHERWISE, ARISING\
  \ OUT OF THIS AGREEMENT,  FOR ANY LOST PROFITS OR ANY INDIRECT, SPECIAL, CONSEQUENTIAL,\
  \ INCIDENTAL, EXEMPLARY OR PUNITIVE DAMAGES, EVEN  IF META OR ITS AFFILIATES HAVE\
  \ BEEN ADVISED OF THE POSSIBILITY OF ANY OF THE FOREGOING.\n5. Intellectual Property.\n\
  a. No trademark licenses are granted under this Agreement, and in connection with\
  \ the Llama Materials,  neither Meta nor Licensee may use any name or mark owned\
  \ by or associated with the other or any of its affiliates,  except as required\
  \ for reasonable and customary use in describing and redistributing the Llama Materials\
  \ or as  set forth in this Section 5(a). Meta hereby grants you a license to use\
  \ “Llama” (the “Mark”) solely as required  to comply with the last sentence of Section\
  \ 1.b.i. You will comply with Meta’s brand guidelines (currently accessible  at\
  \ https://about.meta.com/brand/resources/meta/company-brand/). All goodwill arising\
  \ out of your use of the Mark  will inure to the benefit of Meta.\nb. Subject to\
  \ Meta’s ownership of Llama Materials and derivatives made by or for Meta, with\
  \ respect to any derivative works and modifications of the Llama Materials that\
  \ are made by you, as between you and Meta, you are and will be the owner of such\
  \ derivative works and modifications.\nc. If you institute litigation or other proceedings\
  \ against Meta or any entity (including a cross-claim or counterclaim in a lawsuit)\
  \ alleging that the Llama Materials or Llama 3.2 outputs or results, or any portion\
  \ of any of the foregoing, constitutes infringement of intellectual property or\
  \ other rights owned or licensable by you, then any licenses granted to you under\
  \ this Agreement shall terminate as of the date such litigation or claim is filed\
  \ or instituted. You will indemnify and hold harmless Meta from and against any\
  \ claim by any third party arising out of or related to your use or distribution\
  \ of the Llama Materials.\n6. Term and Termination. The term of this Agreement will\
  \ commence upon your acceptance of this Agreement or access to the Llama Materials\
  \ and will continue in full force and effect until terminated in accordance with\
  \ the terms and conditions herein. Meta may terminate this Agreement if you are\
  \ in breach of any term or condition of this Agreement. Upon termination of this\
  \ Agreement, you shall delete and cease use of the Llama Materials. Sections 3,\
  \ 4 and 7 shall survive the termination of this Agreement. \n7. Governing Law and\
  \ Jurisdiction. This Agreement will be governed and construed under the laws of\
  \ the State of  California without regard to choice of law principles, and the UN\
  \ Convention on Contracts for the International Sale of Goods does not apply to\
  \ this Agreement. The courts of California shall have exclusive jurisdiction of\
  \ any dispute arising out of this Agreement. \n### Llama 3.2 Acceptable Use Policy\n\
  Meta is committed to promoting safe and fair use of its tools and features, including\
  \ Llama 3.2.  If you access or use Llama 3.2, you agree to this Acceptable Use Policy\
  \ (“**Policy**”).  The most recent copy of this policy can be found at [https://www.llama.com/llama3_2/use-policy](https://www.llama.com/llama3_2/use-policy).\n\
  #### Prohibited Uses\nWe want everyone to use Llama 3.2 safely and responsibly.\
  \ You agree you will not use, or allow others to use, Llama 3.2 to:\n1. Violate\
  \ the law or others’ rights, including to:\n    1. Engage in, promote, generate,\
  \ contribute to, encourage, plan, incite, or further illegal or unlawful activity\
  \ or content, such as:\n        1. Violence or terrorism\n        2. Exploitation\
  \ or harm to children, including the solicitation, creation, acquisition, or dissemination\
  \ of child exploitative content or failure to report Child Sexual Abuse Material\n\
  \        3. Human trafficking, exploitation, and sexual violence\n        4. The\
  \ illegal distribution of information or materials to minors, including obscene\
  \ materials, or failure to employ legally required age-gating in connection with\
  \ such information or materials.\n        5. Sexual solicitation\n        6. Any\
  \ other criminal activity\n    1. Engage in, promote, incite, or facilitate the\
  \ harassment, abuse, threatening, or bullying of individuals or groups of individuals\n\
  \    2. Engage in, promote, incite, or facilitate discrimination or other unlawful\
  \ or harmful conduct in the provision of employment, employment benefits, credit,\
  \ housing, other economic benefits, or other essential goods and services\n    3.\
  \ Engage in the unauthorized or unlicensed practice of any profession including,\
  \ but not limited to, financial, legal, medical/health, or related professional\
  \ practices\n    4. Collect, process, disclose, generate, or infer private or sensitive\
  \ information about individuals, including information about individuals’ identity,\
  \ health, or demographic information, unless you have obtained the right to do so\
  \ in accordance with applicable law\n    5. Engage in or facilitate any action or\
  \ generate any content that infringes, misappropriates, or otherwise violates any\
  \ third-party rights, including the outputs or results of any products or services\
  \ using the Llama Materials\n    6. Create, generate, or facilitate the creation\
  \ of malicious code, malware, computer viruses or do anything else that could disable,\
  \ overburden, interfere with or impair the proper working, integrity, operation\
  \ or appearance of a website or computer system\n    7. Engage in any action, or\
  \ facilitate any action, to intentionally circumvent or remove usage restrictions\
  \ or other safety measures, or to enable functionality disabled by Meta \n2. Engage\
  \ in, promote, incite, facilitate, or assist in the planning or development of activities\
  \ that present a risk of death or bodily harm to individuals, including use of Llama\
  \ 3.2 related to the following:\n    8. Military, warfare, nuclear industries or\
  \ applications, espionage, use for materials or activities that are subject to the\
  \ International Traffic Arms Regulations (ITAR) maintained by the United States\
  \ Department of State or to the U.S. Biological Weapons Anti-Terrorism Act of 1989\
  \ or the Chemical Weapons Convention Implementation Act of 1997\n    9. Guns and\
  \ illegal weapons (including weapon development)\n    10. Illegal drugs and regulated/controlled\
  \ substances\n    11. Operation of critical infrastructure, transportation technologies,\
  \ or heavy machinery\n    12. Self-harm or harm to others, including suicide, cutting,\
  \ and eating disorders\n    13. Any content intended to incite or promote violence,\
  \ abuse, or any infliction of bodily harm to an individual\n3. Intentionally deceive\
  \ or mislead others, including use of Llama 3.2 related to the following:\n    14.\
  \ Generating, promoting, or furthering fraud or the creation or promotion of disinformation\n\
  \    15. Generating, promoting, or furthering defamatory content, including the\
  \ creation of defamatory statements, images, or other content\n    16. Generating,\
  \ promoting, or further distributing spam\n    17. Impersonating another individual\
  \ without consent, authorization, or legal right\n    18. Representing that the\
  \ use of Llama 3.2 or outputs are human-generated\n    19. Generating or facilitating\
  \ false online engagement, including fake reviews and other means of fake online\
  \ engagement \n4. Fail to appropriately disclose to end users any known dangers\
  \ of your AI system 5. Interact with third party tools, models, or software designed\
  \ to generate unlawful content or engage in unlawful or harmful conduct and/or represent\
  \ that the outputs of such tools, models, or software are associated with Meta or\
  \ Llama 3.2\n\nWith respect to any multimodal models included in Llama 3.2, the\
  \ rights granted under Section 1(a) of the Llama 3.2 Community License Agreement\
  \ are not being granted to you if you are an individual domiciled in, or a company\
  \ with a principal place of business in, the European Union. This restriction does\
  \ not apply to end users of a product or service that incorporates any such multimodal\
  \ models.\n\nPlease report any violation of this Policy, software “bug,” or other\
  \ problems that could lead to a violation of this Policy through one of the following\
  \ means:\n\n* Reporting issues with the model: [https://github.com/meta-llama/llama-models/issues](https://l.workplace.com/l.php?u=https%3A%2F%2Fgithub.com%2Fmeta-llama%2Fllama-models%2Fissues&h=AT0qV8W9BFT6NwihiOHRuKYQM_UnkzN_NmHMy91OT55gkLpgi4kQupHUl0ssR4dQsIQ8n3tfd0vtkobvsEvt1l4Ic6GXI2EeuHV8N08OG2WnbAmm0FL4ObkazC6G_256vN0lN9DsykCvCqGZ)\n\
  * Reporting risky content generated by the model: [developers.facebook.com/llama_output_feedback](http://developers.facebook.com/llama_output_feedback)\n\
  * Reporting bugs and security concerns: [facebook.com/whitehat/info](http://facebook.com/whitehat/info)\n\
  * Reporting violations of the Acceptable Use Policy or unlicensed uses of Llama\
  \ 3.2: LlamaUseReport@meta.com"
extra_gated_fields:
  First Name: text
  Last Name: text
  Date of birth: date_picker
  Country: country
  Affiliation: text
  Job title:
    type: select
    options:
    - Student
    - Research Graduate
    - AI researcher
    - AI developer/engineer
    - Reporter
    - Other
  geo: ip_location
  ? By clicking Submit below I accept the terms of the license and acknowledge that
    the information I provide will be collected stored processed and shared in accordance
    with the Meta Privacy Policy
  : checkbox
extra_gated_description: The information you provide will be collected, stored, processed
  and shared in accordance with the [Meta Privacy Policy](https://www.facebook.com/privacy/policy/).
extra_gated_button_content: Submit
---

# hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF
This model was converted to GGUF format from [`meta-llama/Llama-3.2-1B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF --hf-file llama-3.2-1b-instruct-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF --hf-file llama-3.2-1b-instruct-q4_k_m.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF --hf-file llama-3.2-1b-instruct-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo hugging-quants/Llama-3.2-1B-Instruct-Q4_K_M-GGUF --hf-file llama-3.2-1b-instruct-q4_k_m.gguf -c 2048
```

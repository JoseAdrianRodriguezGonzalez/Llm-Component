---
base_model: mistralai/Ministral-8B-Instruct-2410
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
pipeline_tag: text-generation
quantized_by: bartowski
inference: false
extra_gated_prompt: '# Mistral AI Research License

  If You want to use a Mistral Model, a Derivative or an Output for any purpose that
  is not expressly authorized under this Agreement, You must request a license from
  Mistral AI, which Mistral AI may grant to You in Mistral AI''s sole discretion.
  To discuss such a license, please contact Mistral AI via the website contact form:
  https://mistral.ai/contact/

  ## 1. Scope and acceptance

  **1.1. Scope of the Agreement.** This Agreement applies to any use, modification,
  or Distribution of any Mistral Model by You, regardless of the source You obtained
  a copy of such Mistral Model.

  **1.2. Acceptance.** By accessing, using, modifying, Distributing a Mistral Model,
  or by creating, using or distributing a Derivative of the Mistral Model, You agree
  to be bound by this Agreement.

  **1.3. Acceptance on behalf of a third-party.** If You accept this Agreement on
  behalf of Your employer or another person or entity, You warrant and represent that
  You have the authority to act and accept this Agreement on their behalf. In such
  a case, the word "You" in this Agreement will refer to Your employer or such other
  person or entity.

  ## 2. License

  **2.1. Grant of rights**.  Subject to Section 3 below, Mistral AI hereby grants
  You a non-exclusive, royalty-free, worldwide, non-sublicensable, non-transferable,
  limited license to use, copy, modify, and Distribute under the conditions provided
  in Section 2.2 below, the Mistral Model and any Derivatives made by or for Mistral
  AI and to create Derivatives of the Mistral Model.

  **2.2. Distribution of Mistral Model and Derivatives made by or for Mistral AI.**
  Subject to Section 3 below, You may Distribute copies of the Mistral Model and/or
  Derivatives made by or for Mistral AI, under the following conditions: You must
  make available a copy of this Agreement to third-party recipients of the Mistral
  Models and/or Derivatives made by or for Mistral AI you Distribute, it being specified
  that any rights to use the Mistral Models and/or Derivatives made by or for Mistral
  AI shall be directly granted by Mistral AI to said third-party recipients pursuant
  to the Mistral AI Research License agreement executed between these parties; You
  must retain in all copies of the Mistral Models the following attribution notice
  within a "Notice" text file distributed as part of such copies: "Licensed by Mistral
  AI under the Mistral AI Research License".

  **2.3. Distribution of Derivatives made by or for You.** Subject to Section 3 below,
  You may Distribute any Derivatives made by or for You under additional or different
  terms and conditions, provided that: In any event, the use and modification of Mistral
  Model and/or Derivatives made by or for Mistral AI shall remain governed by the
  terms and conditions of this Agreement; You include in any such Derivatives made
  by or for You prominent notices stating that You modified the concerned Mistral
  Model; and Any terms and conditions You impose on any third-party recipients relating
  to Derivatives made by or for You shall neither limit such third-party recipients''
  use of the Mistral Model or any Derivatives made by or for Mistral AI in accordance
  with the Mistral AI Research License nor conflict with any of its terms and conditions.

  ## 3. Limitations

  **3.1. Misrepresentation.** You must not misrepresent or imply, through any means,
  that the Derivatives made by or for You and/or any modified version of the Mistral
  Model You Distribute under your name and responsibility is an official product of
  Mistral AI or has been endorsed, approved or validated by Mistral AI, unless You
  are authorized by Us to do so in writing.

  **3.2. Usage Limitation.** You shall only use the Mistral Models, Derivatives (whether
  or not created by Mistral AI) and Outputs for Research Purposes.

  ## 4. Intellectual Property

  **4.1. Trademarks.** No trademark licenses are granted under this Agreement, and
  in connection with the Mistral Models, You may not use any name or mark owned by
  or associated with Mistral AI or any of its affiliates, except (i) as required for
  reasonable and customary use in describing and Distributing the Mistral Models and
  Derivatives made by or for Mistral AI and (ii) for attribution purposes as required
  by this Agreement.

  **4.2. Outputs.** We claim no ownership rights in and to the Outputs. You are solely
  responsible for the Outputs You generate and their subsequent uses in accordance
  with this Agreement. Any Outputs shall be subject to the restrictions set out in
  Section 3 of this Agreement.

  **4.3. Derivatives.** By entering into this Agreement, You accept that any Derivatives
  that You may create or that may be created for You shall be subject to the restrictions
  set out in Section 3 of this Agreement.

  ## 5. Liability

  **5.1. Limitation of liability.** In no event, unless required by applicable law
  (such as deliberate and grossly negligent acts) or agreed to in writing, shall Mistral
  AI be liable to You for damages, including any direct, indirect, special, incidental,
  or consequential damages of any character arising as a result of this Agreement
  or out of the use or inability to use the Mistral Models and Derivatives (including
  but not limited to damages for loss of data, loss of goodwill, loss of expected
  profit or savings, work stoppage, computer failure or malfunction, or any damage
  caused by malware or security breaches), even if  Mistral AI has been advised of
  the possibility of such damages.

  **5.2. Indemnification.** You agree to indemnify and hold harmless Mistral AI from
  and against any claims, damages, or losses arising out of or related to Your use
  or Distribution of the Mistral Models and Derivatives.

  ## 6. Warranty

  **6.1. Disclaimer.** Unless required by applicable law or prior agreed to by Mistral
  AI in writing, Mistral AI provides the Mistral Models and Derivatives on an "AS
  IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied,
  including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT,
  MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. Mistral AI does not represent
  nor warrant that the Mistral Models and Derivatives will be error-free, meet Your
  or any third party''s requirements, be secure or will allow You or any third party
  to achieve any kind of result or generate any kind of content. You are solely responsible
  for determining the appropriateness of using or Distributing the Mistral Models
  and Derivatives and assume any risks associated with Your exercise of rights under
  this Agreement.

  ## 7. Termination

  **7.1. Term.** This Agreement is effective as of the date of your acceptance of
  this Agreement or access to the concerned Mistral Models or Derivatives and will
  continue until terminated in accordance with the following terms.

  **7.2. Termination.** Mistral AI may terminate this Agreement at any time if You
  are in breach of this Agreement. Upon termination of this Agreement, You must cease
  to use all Mistral Models and Derivatives and shall permanently delete any copy
  thereof. The following provisions, in their relevant parts, will survive any termination
  or expiration of this Agreement, each for the duration necessary to achieve its
  own intended purpose (e.g. the liability provision will survive until the end of
  the applicable limitation period):Sections 5 (Liability), 6(Warranty), 7 (Termination)
  and 8 (General Provisions).

  **7.3. Litigation.** If You initiate any legal action or proceedings against Us
  or any other entity (including a cross-claim or counterclaim in a lawsuit), alleging
  that the Model or a Derivative, or any part thereof, infringe upon intellectual
  property or other rights owned or licensable by You, then any licenses granted to
  You under this Agreement will immediately terminate as of the date such legal action
  or claim is filed or initiated.

  ## 8. General provisions

  **8.1. Governing laws.** This Agreement will be governed by the laws of France,
  without regard to choice of law principles, and the UN Convention on Contracts for
  the International Sale of Goods does not apply to this Agreement.

  **8.2. Competent jurisdiction.** The courts of Paris shall have exclusive jurisdiction
  of any dispute arising out of this Agreement.

  **8.3. Severability.** If any provision of this Agreement is held to be invalid,
  illegal or unenforceable, the remaining provisions shall be unaffected thereby and
  remain valid as if such provision had not been set forth herein.

  ## 9. Definitions

  "Agreement": means this Mistral AI Research License agreement governing the access,
  use, and Distribution of the Mistral Models, Derivatives and Outputs.

  "Derivative": means any (i) modified version of the Mistral Model (including but
  not limited to any customized or fine-tuned version thereof), (ii) work based on
  the Mistral Model, or (iii) any other derivative work thereof.

  "Distribution", "Distributing", "Distribute" or "Distributed": means supplying,
  providing or making available, by any means, a copy of the Mistral Models and/or
  the Derivatives as the case may be, subject to Section 3 of this Agreement.

  "Mistral AI", "We" or "Us": means Mistral AI, a French société par actions simplifiée
  registered in the Paris commercial registry under the number 952 418 325, and having
  its registered seat at 15, rue des Halles, 75001 Paris.

  "Mistral Model": means the foundational large language model(s), and its elements
  which include algorithms, software, instructed checkpoints, parameters, source code
  (inference code, evaluation code and, if applicable, fine-tuning code) and any other
  elements associated thereto made available by Mistral AI under this Agreement, including,
  if any, the technical documentation, manuals and instructions for the use and operation
  thereof.

  "Research Purposes": means any use of a Mistral Model,  Derivative, or Output that
  is solely for (a) personal, scientific or academic research, and (b) for non-profit
  and non-commercial purposes, and not directly or indirectly connected to any commercial
  activities or business operations. For illustration purposes, Research Purposes
  does not include (1) any usage of the Mistral Model, Derivative or Output by individuals
  or contractors employed in or engaged by companies in the context of (a) their daily
  tasks, or (b) any activity (including but not limited to any testing or proof-of-concept)
  that is intended to generate revenue, nor (2) any Distribution by a commercial entity
  of the Mistral Model, Derivative or Output whether in return for payment or free
  of charge, in any medium or form, including but not limited to through a hosted
  or managed service (e.g. SaaS, cloud instances, etc.), or behind a software layer.

  "Outputs": means any content generated by the operation of the Mistral Models or
  the Derivatives from  a prompt (i.e., text instructions) provided by users. For
  the avoidance of doubt, Outputs do not include any components of a Mistral Models,
  such as any fine-tuned versions of the Mistral Models, the weights, or parameters.

  "You": means the individual or entity entering into this Agreement with Mistral
  AI.


  *Mistral AI processes your personal data below to provide the model and enforce
  its license. If you are affiliated with a commercial entity, we may also send you
  communications about our models. For more information on your rights and data handling,
  please see our <a href="https://mistral.ai/terms/">privacy policy</a>.*'
extra_gated_fields:
  First Name: text
  Last Name: text
  Country: country
  Affiliation: text
  Job title: text
  I understand that I can only use the model, any derivative versions and their outputs for non-commercial research purposes: checkbox
  ? I understand that if I am a commercial entity, I am not permitted to use or distribute
    the model internally or externally, or expose it in my own offerings without a
    commercial license
  : checkbox
  ? I understand that if I upload the model, or any derivative version, on any platform,
    I must include the Mistral Research License
  : checkbox
  ? I understand that for commercial use of the model, I can contact Mistral or use
    the Mistral AI API on la Plateforme or any of our cloud provider partners
  : checkbox
  ? By clicking Submit below I accept the terms of the license and acknowledge that
    the information I provide will be collected stored processed and shared in accordance
    with the Mistral Privacy Policy
  : checkbox
  geo: ip_location
extra_gated_description: Mistral AI processes your personal data below to provide
  the model and enforce its license. If you are affiliated with a commercial entity,
  we may also send you communications about our models. For more information on your
  rights and data handling, please see our <a href="https://mistral.ai/terms/">privacy
  policy</a>.
extra_gated_button_content: Submit
---

## Llamacpp imatrix Quantizations of Ministral-8B-Instruct-2410

# This is based on the officially merged safetensors for Ministral, however there may still be changes required to llama.cpp for full performance

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b3930">b3930</a> for quantization.

Original model: https://huggingface.co/mistralai/Ministral-8B-Instruct-2410

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

## Prompt format

```
<s>[INST]{prompt}[/INST]
```

## What's new:

Update to official repo

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [Ministral-8B-Instruct-2410-f16.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-f16.gguf) | f16 | 16.05GB | false | Full F16 weights. |
| [Ministral-8B-Instruct-2410-Q8_0.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q8_0.gguf) | Q8_0 | 8.53GB | false | Extremely high quality, generally unneeded but max available quant. |
| [Ministral-8B-Instruct-2410-Q6_K_L.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q6_K_L.gguf) | Q6_K_L | 6.85GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [Ministral-8B-Instruct-2410-Q6_K.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q6_K.gguf) | Q6_K | 6.59GB | false | Very high quality, near perfect, *recommended*. |
| [Ministral-8B-Instruct-2410-Q5_K_L.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q5_K_L.gguf) | Q5_K_L | 6.06GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [Ministral-8B-Instruct-2410-Q5_K_M.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q5_K_M.gguf) | Q5_K_M | 5.72GB | false | High quality, *recommended*. |
| [Ministral-8B-Instruct-2410-Q5_K_S.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q5_K_S.gguf) | Q5_K_S | 5.59GB | false | High quality, *recommended*. |
| [Ministral-8B-Instruct-2410-Q4_K_L.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q4_K_L.gguf) | Q4_K_L | 5.31GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [Ministral-8B-Instruct-2410-Q4_K_M.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q4_K_M.gguf) | Q4_K_M | 4.91GB | false | Good quality, default size for must use cases, *recommended*. |
| [Ministral-8B-Instruct-2410-Q3_K_XL.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q3_K_XL.gguf) | Q3_K_XL | 4.80GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [Ministral-8B-Instruct-2410-Q4_K_S.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q4_K_S.gguf) | Q4_K_S | 4.69GB | false | Slightly lower quality with more space savings, *recommended*. |
| [Ministral-8B-Instruct-2410-Q4_0.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q4_0.gguf) | Q4_0 | 4.67GB | false | Legacy format, generally not worth using over similarly sized formats |
| [Ministral-8B-Instruct-2410-Q4_0_8_8.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q4_0_8_8.gguf) | Q4_0_8_8 | 4.66GB | false | Optimized for ARM inference. Requires 'sve' support (see link below). *Don't use on Mac or Windows*. |
| [Ministral-8B-Instruct-2410-Q4_0_4_8.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q4_0_4_8.gguf) | Q4_0_4_8 | 4.66GB | false | Optimized for ARM inference. Requires 'i8mm' support (see link below). *Don't use on Mac or Windows*. |
| [Ministral-8B-Instruct-2410-Q4_0_4_4.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q4_0_4_4.gguf) | Q4_0_4_4 | 4.66GB | false | Optimized for ARM inference. Should work well on all ARM chips, pick this if you're unsure. *Don't use on Mac or Windows*. |
| [Ministral-8B-Instruct-2410-IQ4_XS.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-IQ4_XS.gguf) | IQ4_XS | 4.45GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Ministral-8B-Instruct-2410-Q3_K_L.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q3_K_L.gguf) | Q3_K_L | 4.33GB | false | Lower quality but usable, good for low RAM availability. |
| [Ministral-8B-Instruct-2410-Q3_K_M.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q3_K_M.gguf) | Q3_K_M | 4.02GB | false | Low quality. |
| [Ministral-8B-Instruct-2410-IQ3_M.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-IQ3_M.gguf) | IQ3_M | 3.79GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Ministral-8B-Instruct-2410-Q2_K_L.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q2_K_L.gguf) | Q2_K_L | 3.71GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [Ministral-8B-Instruct-2410-Q3_K_S.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q3_K_S.gguf) | Q3_K_S | 3.66GB | false | Low quality, not recommended. |
| [Ministral-8B-Instruct-2410-IQ3_XS.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-IQ3_XS.gguf) | IQ3_XS | 3.52GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [Ministral-8B-Instruct-2410-Q2_K.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-Q2_K.gguf) | Q2_K | 3.19GB | false | Very low quality but surprisingly usable. |
| [Ministral-8B-Instruct-2410-IQ2_M.gguf](https://huggingface.co/bartowski/Ministral-8B-Instruct-2410-GGUF/blob/main/Ministral-8B-Instruct-2410-IQ2_M.gguf) | IQ2_M | 2.96GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

Some say that this improves the quality, others don't notice any difference. If you use these models PLEASE COMMENT with your findings. I would like feedback that these are actually used and useful so I don't keep uploading quants no one is using.

Thanks!

## Downloading using huggingface-cli

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/Ministral-8B-Instruct-2410-GGUF --include "Ministral-8B-Instruct-2410-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/Ministral-8B-Instruct-2410-GGUF --include "Ministral-8B-Instruct-2410-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (Ministral-8B-Instruct-2410-Q8_0) or download them all in place (./)

## Q4_0_X_X

These are *NOT* for Metal (Apple) offloading, only ARM chips.

If you're using an ARM chip, the Q4_0_X_X quants will have a substantial speedup. Check out Q4_0_4_4 speed comparisons [on the original pull request](https://github.com/ggerganov/llama.cpp/pull/5780#pullrequestreview-21657544660)

To check which one would work best for your ARM chip, you can check [AArch64 SoC features](https://gpages.juszkiewicz.com.pl/arm-socs-table/arm-socs.html) (thanks EloyOn!).

## Which file should I choose?

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU and Apple Metal, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset

Thank you ZeroWw for the inspiration to experiment with embed/output

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski

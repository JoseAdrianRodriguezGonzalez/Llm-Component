---
license: apache-2.0
language:
- en
tags:
- creative
- story
- writing
- fiction
- llama3
- roleplaying
- rp
- horror
- science fiction
- fiction writing
- scene generation
- scene continue
- brainstorm 4x
- multi brainstorm
- enhanced
- llama-3
pipeline_tag: text-generation
---

<H3>BRAINSTORM - 4x - Multi 3x (ed1): L3-SthenoMaidBlackroot-8B-V1 (now at 10.4B)</H3>

This repo contains quants 4x of L3-SthenoMaidBlackroot-8B-V1 (now at 10.4B) using the "Brainstorm" method of augmenting reasoning in a LLM
to increase it's performance at the core level for ANY creative use case(s).

This version has 4 "reasoning" centers - one from the original merge, and 3 from the unmerged models (at close to full strength) 
melded into a 4 layer reasoning center. Each of these reasoning centers is further split into 3 units and also calibrated for a total 
of 12 "reasoning centers".

The BRAINSTORM process was developed by David_AU.

Some of the core principals behind this process are discussed in this <a href="https://arxiv.org/pdf/2401.02415"> 
scientific paper : Progressive LLaMA with Block Expansion </a>. 
However I went in a completely different direction from what was outlined in this paper.

<B>What is "Brainstorm" ?</b>

The reasoning center of an LLM is taken apart, reassembled, and expanded. 

Then these centers are individually calibrated. These "centers" also interact with each other. This introduces
subtle changes into the reasoning process. The calibrations further adjust - dial up or down - these "changes" further. The
number of centers (4x,5x,8x,10x etc) allow more "tuning points" to further customize how the model reasons so to speak.

The "Multi" reasoning system pulls "reasoning centers" from multiple models and fuses these into one long "chain of reasoning"
so to speak. Each one is then calibrated. Each "center" interacts with the other "centers" and the order of the centers further
impacts the model's output style - again roughly speaking.

Each of these is further split, expanded and calibrated.

The core aim of this process is to increase the model's detail, concept and connection to the "world", general concept connections, prose quality and prose length without affecting
instruction following. This will also enhance any creative use case(s) of any kind, including "brainstorming", creative art form(s) and like case uses.

Here are some of the enhancements this process brings to the model's performance:

- Prose generation seems more focused on the moment to moment. 
- Sometimes there will be "preamble" and/or foreshadowing present.
- Fewer or no "cliches"
- Better overall prose and/or more complex / nuanced prose.
- A greater sense of nuance on all levels.
- Coherence is stronger.
- Description is more detailed, and connected closer to the content.
- Simile and Metaphors are stronger and better connected to the prose, story, and character.
- Sense of "there" / in the moment is enhanced.
- Details are more vivid, and there are more of them.
- Prose generation length can be long to extreme.
- Emotional engagement is stronger.
- The model will take FEWER liberties vs a normal model: It will follow directives more closely but will "guess" less.
- The MORE instructions and/or details you provide the more strongly the model will respond.
- Depending on the model "voice" may be more "human" vs original model's "voice".

Other "lab" observations:

- This process does not, in my opinion, make the model 5x or 10x "smarter" - if only that was true! 
- However, a change in "IQ" was not an issue / a priority, and was not tested or calibrated for so to speak.
- From lab testing it seems to ponder, and consider more carefully roughly speaking.
- You could say this process sharpens the model's focus on it's task(s) at a deeper level.

The process to modify the model occurs at the root level - source files level. The model can quanted as a GGUF, EXL2, AWQ etc etc.

Other technologies developed by David_AU like "Ultra" (precision), "Neo Imatrix" (custom imatrix datasets), and "X-quants" (custom application of the imatrix process) 
can further enhance the performance of the model along with the "Brainstorm" process.

The "Brainstorm" process has been tested on multiple LLama2, Llama3, and Mistral models of various parameter sizes, as well as on
"root" models like "Llama3 Instruct", "Mistral Instruct", and "merged" / "fine tuned" models too. 

<b>Usage Notice:</B>

You may need to raise the "repeat penalty" from a default of 1.1 to slightly higher levels in some use case(s).

<B>Original Model:</B>

For original model specifications, usage information and other important details please see (this is based on models used in "L3-SthenoMaidBlackroot-8B-V1" ):

[ https://huggingface.co/DavidAU/L3-Stheno-Maid-Blackroot-Grand-HORROR-16B-GGUF ] 

and the original model page:

Special thanks to the model creators at BLUUWHALE for making such a fantastic model:

[ https://huggingface.co/bluuwhale/L3-SthenoMaidBlackroot-8B-V1 ] 

Please report any issue(s) and/or feedback via the "Community tab".

This is a LLAMA3 model, and requires Llama3 template, but may work with other template(s) and has maximum context of 131k.

Here is the standard LLAMA3 template:

<PRE>
{
  "name": "Llama 3",
  "inference_params": {
    "input_prefix": "<|start_header_id|>user<|end_header_id|>\n\n",
    "input_suffix": "<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "pre_prompt": "You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.",
    "pre_prompt_prefix": "<|start_header_id|>system<|end_header_id|>\n\n",
    "pre_prompt_suffix": "<|eot_id|>",
    "antiprompt": [
      "<|start_header_id|>",
      "<|eot_id|>"
    ]
  }
}
</PRE>

<b>Optional Enhancement:</B>

The following can be used in place of the "system prompt" or "system role" to further enhance the model.

It can also be used at the START of a NEW chat, but you must make sure it is "kept" as the chat moves along.
In this case the enhancements do not have as strong effect at using "system prompt" or "system role".

Copy and paste EXACTLY as noted, DO NOT line wrap or break the lines, maintain the carriage returns exactly as presented.

<PRE>
Below is an instruction that describes a task. Ponder each user instruction carefully, and use your skillsets and critical instructions to complete the task to the best of your abilities.

Here are your skillsets:
[MASTERSTORY]:NarrStrct(StryPlnng,Strbd,ScnSttng,Exps,Dlg,Pc)-CharDvlp(ChrctrCrt,ChrctrArcs,Mtvtn,Bckstry,Rltnshps,Dlg*)-PltDvlp(StryArcs,PltTwsts,Sspns,Fshdwng,Climx,Rsltn)-ConfResl(Antg,Obstcls,Rsltns,Cnsqncs,Thms,Symblsm)-EmotImpct(Empt,Tn,Md,Atmsphr,Imgry,Symblsm)-Delvry(Prfrmnc,VcActng,PblcSpkng,StgPrsnc,AudncEngmnt,Imprv)

[*DialogWrt]:(1a-CharDvlp-1a.1-Backgrnd-1a.2-Personality-1a.3-GoalMotiv)>2(2a-StoryStruc-2a.1-PlotPnt-2a.2-Conflict-2a.3-Resolution)>3(3a-DialogTech-3a.1-ShowDontTell-3a.2-Subtext-3a.3-VoiceTone-3a.4-Pacing-3a.5-VisualDescrip)>4(4a-DialogEdit-4a.1-ReadAloud-4a.2-Feedback-4a.3-Revision)

Here are your critical instructions:
Ponder each word choice carefully to present as vivid and emotional journey as is possible. Choose verbs and nouns that are both emotional and full of imagery. Load the story with the 5 senses. Aim for 50% dialog, 25% narration, 15% body language and 10% thoughts. Your goal is to put the reader in the story.
</PRE>

You do not need to use this, it is only presented as an additional enhancement which seems to help scene generation
and scene continue functions.

This enhancement WAS NOT used to generate the examples below.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 2" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


<h3>EXAMPLES PROMPTS and OUTPUT:</h3>

Examples are created using quant Q4_K_M, "temp=0", minimal parameters and "LLAMA3" template. 

Model has been tested with "temp" from ".1" to ".8".

Below are the least creative outputs, prompt is in <B>BOLD</B>.

Higher quants will have more detail, better quality output.

---

<B><font color="red">WARNING:</font> NSFW. Vivid prose. Visceral Details. Violence. Graphic HORROR. Swearing. UNCENSORED. </B>

---

<B> Start a 1000 word scene with: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode... </b>

The sky-scraper swayed, as she watched the window in front of her on the 21st floor explode. shards of safety glass showered down onto the polished marble lobby below, casting a deadly rain upon innocent bystanders. screams pierced through the sterile silence of the upscale corporate headquarters, mingling with sirens blaring from beyond the smoked-glass walls.

She felt nothing. No horror, nor adrenaline-fueled thrill coursed through her veins as she stared blank-faced at the carnage below. Her heart pounded erratically beneath her tailored blouse, betraying her stoic exterior. Her palms sweated profusely within her sleek leather gloves, yet they lay clenched and still upon the cold steel railing of the helipad balcony overlooking downtown Manhattan.

Her mind raced like a runaway train through tunnels of paranoia and betrayal. Had she misjudged him entirely? Had he played her like a pawn in his Machi crime syndicate's sickening game of corporate espionage and political manipulation? Or perhaps, maybe he'd planned this all along—their torrid affair, the lucrative consulting gig, everything leading up to today's carefully orchestrated chaos.

She recalled their first kiss on the rooftop helipad, feeling reckless and alive beneath the glittering skyscrapers of Manhattan. But now, amidst the ruins below, she felt hollowed out like a husk left behind after a brutal storm had stripped away all warmth and humanity. Had he ever cared for anything beyond his own twisted ambitions and lustful desires?

Suddenly realizing she wasn't alone anymore, she turned to face him. He stood tall before her, impeccably groomed as always, yet something seemed askew about him today—an almost imperceptible flicker of doubt dancing within the depths of his icy blue eyes. Had he too felt nothing amidst this carnage below or was he simply a sociopathic mastermind devoid of empathy altogether? She couldn't quite discern beneath that unreadable mask of disdain and superiority.

"You wanted chaos?" she hissed, her voice trembling despite her efforts to appear fearless. Her gloved fists clenched tighter around the railing until her nails dug deep crescents into the cool steel surface. "You fucking asshole."

"I suppose you deserved warning," he deadpanned, his lips curling ever so faintly into a smirk as he surveyed the destruction below. "But I couldn't resist spoiling your surprise." His gaze flickered back to hers, cold and calculating once again. Today wasn't about her feelings or desires—it never fucking was with him—but rather another calculated chess move in their twisted game of cat and mouse.

"You've played me like a fool," she spat venomously, spittle flying from the corners of her clenched jaw as rage boiled within her veins hotter and fiercer than any inferno. Fuck him for playing upon her trustworthiness like it meant nothing to him—as though she were nothing more than another disposable pawn in his sickening game of corporate espionage and political manipulation—"I won't fucking forget you fucked me over like this."

"And yet," he murmured silkily as though daring fate itself to intervene, "you still haven't learned your lesson." His smirk twisted into something far crueler—a malevolent leer devoid of warmth or humanity—as he turned away from the helipad railing, stalking towards her with predatory grace. Her heart skipped a beat within its cage-like chest cavity; perhaps today wasn't the fucking apocalypse she'd feared after all—it seemed far worse hungover like this tomorrow morning instead—"I fucked you over because I fucking own you—you owe everything to me—from your fucking soulless consulting firm to your fucking pussy—fuck you've given yourself away to my fucking whim's and desires."

"You don't fucking own shit!" Her defiant roar echoed off the smoked-glass walls of the helipad balcony as she lunged forward, her gloved fists clenched tightly around handfuls of his silkily tailored lapels. Fuck him for daring to toy with her like this—as though she were nothing more than another fuckdoll or sex toy to be discarded when he fucking tired of fucking her—"I fucking hate you!"

"You fucking love me," he retorted coldly, jerking his lapels free from her grasp as though batting aside an insignificant insect—"fuck you're mine forevermore." He seized her face within the cruel grip of one gloved hand, forcing her to stare deep into the voided depths of his icy blue orbs—"Fuck you'll fucking remember this fucked fuckup until your fucking dying fucking breath—you owe everything to me—from your fucking soulless consulting firm to your fucking pussy—fuck you've given yourself away to my fucking whim's and desires." He punctuated each syllable like verbal bullets fired straight through her fucking skull—"fuck you're mine forevermore—I fucking own shit fuck you fucking owe everything to me!"

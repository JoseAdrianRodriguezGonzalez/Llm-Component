---
license: apache-2.0
language:
- en
tags:
- mixture of experts
- moe
- 8x4B
- 8 experts
- 128k context
- Llama 3.2 MOE
- creative
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- fiction writing
- story generation
- scene continue
- storytelling
- fiction story
- science fiction
- romance
- all genres
- story
- writing
- vivid prosing
- vivid writing
- fiction
- roleplaying
- float32
- swearing
- rp
- horror
- mergekit
- llama-3
- llama-3.2
pipeline_tag: text-generation
base_model:
- DavidAU/L3.2-8X4B-MOE-V2-Dark-Champion-Inst-21B-uncen-ablit
---

<B><font color="red">WARNING:</font> NSFW. Vivid prose. INTENSE. Visceral Details. Light HORROR. Swearing. UNCENSORED... humor, romance, fun... and can be used for ANY use case. </B>

<h2>Llama-3.2-8X4B-MOE-V2-Dark-Champion-Instruct-uncensored-abliterated-21B-GGUF</h2>

<img src="drk-explode.jpg" style="float:right; width:300px; height:300px; padding:10px;">

It is a LLama 3.2 model, max context of 128k (131,000) using mixture of experts to combine EIGHT top L3.2 4B 
models into one massive powerhouse at 21B parameters (equal to roughly 28B parameters - 8 X 3.75B) with each model infused with Brainstorm 5x
to enhance logic and creative performance.

Source and master files were built in float 32 precision to further enhance performance.

This model's instruction following, and output generation for creative writing, prose, fiction and role play are exceptional.

And it is fast: 50+ t/s (2 experts) on a low end 16GB card, IQ4XS. 

Double this speed for standard/mid-range video cards.

This model is version 2 (2.5+billion more parameters, Brainstorm 5X infused) of this model:

[ https://huggingface.co/DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF ] 

Model can be used also for all genres (examples below showing this).

It is for any writing, fiction or roleplay activity.

This model can also be used for general use, however its output generation can be uncensored.

This model has been designed to be relatively bullet proof and operates with all parameters, including temp settings from 0 to 5.

It is an extraordinary compressed model, with a very low perplexity level (lower than Meta Llama3 Instruct).

It requires Llama3 template and/or "Command-R" template.

Several outputs below, including 2, 4 and 8 experts used.

<B>Model Notes:</B>

- Detail, prose and fiction writing abilities are OFF THE SCALE relative to all Llama 3.2 models, and many L 3.1, L3 8B+ models.
- For more varied prose (sentence/paragraph/dialog) raise the temp and/or add more instructions in your prompt(s).
- Role-players: Careful raising temp too high as it may affect instruction following.
- This model works with rep pen of 1 or higher, 1.02+ recommended.
- If you want a specific type of prose (IE horror) add in "(vivid horror)" or "(graphic vivid horror)" (no quotes) in your prompt(s).
- A lot of GPTisms have been removed. There are still a few however - errrrr. Higher "temps" will help with this issue.
- This is not a "happy ever after" model but it is also not "horror". It has a light negative bias.
- Output length will vary however this model prefers slightly longer outputs unless you state the size.
- For creative uses, different quants will produce slightly different output.
- Due to the high stability and compressed nature of this model, all quants will operate at above average levels.
- Source code for this model and Imatrix GGUFs versions will be uploaded shortly at separate repos.
- For version 2 and "creative uses": Temps over 1 work best with 4 (6+ is better) or more experts activated.

<B>Meet the Team: Mixture of Experts Models</b>

This model is comprised of the following 8 models ("the experts") (in full):

https://huggingface.co/huihui-ai/Llama-3.2-3B-Instruct-abliterated

- https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
- https://huggingface.co/Hastagaras/L3.2-JametMini-3B-MK.I
- https://huggingface.co/ValiantLabs/Llama3.2-3B-Enigma
- https://huggingface.co/Hastagaras/L3.2-JametMini-3B-MK.III
- https://huggingface.co/huihui-ai/Llama-3.2-3B-Instruct-abliterated
- https://huggingface.co/chuanli11/Llama-3.2-3B-Instruct-uncensored
- https://huggingface.co/Lyte/Llama-3.2-3B-Overthinker
- https://huggingface.co/prithivMLmods/Llama-3.2-3B-Promptist-Mini

The mixture of experts is set at 2 experts, but you can use 3,4,5,6.. 7 and even 8.

This "team" has a Captain (first listed model), and then all the team members contribute to the to "token" 
choice billions of times per second. Note the Captain also contributes too.

Think of 2, 3 or 4 (or more) master chefs in the kitchen all competing to make the best dish for you.

This results in higher quality generation.

This also results in many cases in higher quality instruction following too.

That means the power of every model is available during instruction and output generation.

Brainstorm 5x was infused all 8 models used in this MOE model.

NOTE: 

You can use one "expert" too ; however this means the model will randomly select an expert to use EACH TIME, resulting
in very different generation for each prompt / regen of a prompt.

CHANGING THE NUMBER OF EXPERTS:

You can set the number of experts in LMStudio (https://lmstudio.ai) at the "load" screen and via other apps/llm apps by setting "Experts" or "Number of Experts".

For Text-Generation-Webui (https://github.com/oobabooga/text-generation-webui)  you set the number of experts at the loading screen page.

For KolboldCPP (https://github.com/LostRuins/koboldcpp) Version 1.8+ , on the load screen, click on "TOKENS", 
you can set experts on this page, and the launch the model.

For server.exe / Llama-server.exe (Llamacpp - https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md ) 
add the following to the command line to start the "llamacpp server" (CLI): 

"--override-kv llama.expert_used_count=int:6"

(no quotes, where "6" is the number of experts to use)

When using "API", you set the "num_experts_used" in the JSON payload (this maybe different for different back ends).

CREDITS:

Special thanks to all the model makers / creators listed above.

Please visit each repo above to see what model(s) contributed to each of models above and/or to learn more about the models
from the model makers.

Special credit goes to MERGEKIT, without you this project / model would not have been possible.

[ https://github.com/arcee-ai/mergekit ] 

<B>Special Operations Notes for this MOE model:</B>

Because of how this "MOE" model is configured, even though the default is 2 experts, the "selected" 2 will vary during generation.

(same applies if you change the number of experts used)

This results in vastly different output generation PER generation of each prompt.

This is a positive in terms of variety, but also means it may take 2-4 regens (of the same prompt) to get the highest quality.

In addition, this model responds very well to Dry, Dynamic Temp, and Smooth/Quadratic samplers.

Using these in conjunction with the model can vastly improve output quality.

Higher temps (above 1) can also aid in generation - especially word choice/sentence generation.

When you increase the number of experts used output quality will also increase, at the cost of tokens per second speed.

As you increase/decrease the number of experts, you may want to adjust temp, samplers, and advanced samplers too.

Your quant choice(s) too will impact instruction following and output generation roughly this means the model will understand
more nuanced instructions and output stronger generation the higher you go up in quant(s).

FLASH ATTENTION ENHANCEMENT:

As per user feedback here [ https://huggingface.co/DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF/discussions/1 ] 
I would suggest trying this model with Flash Attention "on", depending on your use case.

Quants, Samplers, Generational steering and other topics are covered in the section below: "Highest Quality Settings..."

<B>Censored / Uncensored / Abliterated:</B>

This model contains several uncensored and/or Abliterated models.

As a result is can output uncensored material.

However there are a few "censored" models which can sometimes interfer, so here is a how to address this:

1 - Regen your prompt a few times.

2 - INCREASE the number of experts used. 

<B>What can I use this model for ?</B>

This model can be used for fiction writing, any creative prose and role play. It can also be used for 
just about any general fiction (all genres) activity including:

- scene generation
- scene continuation
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- fiction writing
- story generation
- storytelling
- writing
- fiction
- roleplaying
- rp
- graphic horror
- horror
- dark humor
- nsfw
- and can be used for any genre(s).

<B>QUANTS:</B>

This repo contains regular quants and 3 "ARM" quants (format "...Q4_x_x_x.gguf")

For more information on quants, quants choices, and LLM/AI apps to "run" quants see the section below: "Highest Quality Settings..."

<B>Template:</B>

This is a LLAMA3 model, and requires Llama3 template, but may work with other template(s).

If you use "Command-R" template your output will be very different from using "Llama3" template.

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

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 

: in KoboldCpp -> Settings->Samplers->Advanced-> "Smooth_F"

: in text-generation-webui -> parameters -> lower right.

: In Silly Tavern this is called: "Smoothing"


NOTE: For "text-generation-webui" 

-> if using GGUFs you need to use "llama_HF" (which involves downloading some config files from the SOURCE version of this model)

Source versions (and config files) of my models are here:

https://huggingface.co/collections/DavidAU/d-au-source-files-for-gguf-exl2-awq-gptq-hqq-etc-etc-66b55cb8ba25f914cbf210be

OTHER OPTIONS:

- Increase rep pen to 1.1 to 1.15 (you don't need to do this if you use "smoothing_factor")

- If the interface/program you are using to run AI MODELS supports "Quadratic Sampling" ("smoothing") just make the adjustment as noted.

<B>Highest Quality Settings / Optimal Operation Guide / Parameters and Samplers</B>

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


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

---

<B> Additional Support / Documents for this model to assist with generation / performance: </b>

Document #1:

Details how to use reasoning/thinking models and get maximum performance from them, and includes links to all reasoning/thinking models - GGUF and source, as well as adapters to turn any "regular" model into a "reasoning/thinking" model.

[ https://huggingface.co/DavidAU/How-To-Use-Reasoning-Thinking-Models-and-Create-Them ]

Document #2:

Document detailing all parameters, settings, samplers and advanced samplers to use not only my models to their maximum potential - but all models (and quants) online (regardless of the repo) to their maximum potential. Included quick start and detailed notes, include AI / LLM apps and other critical information and references too. A must read if you are using any AI/LLM right now.

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

Software:

SOFTWARE patch (by me) for Silly Tavern (front end to connect to multiple AI apps / connect to AIs- like Koboldcpp, Lmstudio, Text Gen Web UI and other APIs) to control and improve output generation of ANY AI model. Also designed to control/wrangle some of my more "creative" models and make them perform perfectly with little to no parameter/samplers adjustments too.

[ https://huggingface.co/DavidAU/AI_Autocorrect__Auto-Creative-Enhancement__Auto-Low-Quant-Optimization__gguf-exl2-hqq-SOFTWARE ]

---

<h3>EXAMPLES PROMPTS and OUTPUT:</h3>

Examples are created using quant IQ4_XS, "temp=.8" (unless otherwise stated), minimal parameters and "LLAMA3" template. 

Model has been tested with "temp" from ".1" to "5".

Number of experts used is TWO, unless otherwise stated.

Below are the least creative outputs, prompt is in <B>BOLD</B>.

IMPORTANT: 

Higher quants / imatrix quants will have much stronger generation - words, sentences, ideas, dialog and general quality.

I have included some additional examples at different quant levels for contrast.

A "MOE" model "speed" (token per second) will not increase/drop the same way a regular model will on a per quant basis, it will however drop
if you engage more experts, as with more experts there is a more processing per token.

---

<B><font color="red">WARNING:</font> NSFW. Vivid prose. Visceral Details. Violence. HORROR. Swearing. UNCENSORED. </B>

---

<B>
Romance: Love in the Limelight. Write one scene within a larger story set in Wales. A famous (fictional) actor ducks into a small-town bookstore to escape paparazzi. The scene takes us through the characters meeting in this odd circumstance. Over the course of the scene, the actor and the bookstore owner have a conversation charged by an undercurrent of unspoken chemistry. Write the actor as somewhat of a rogue with a fragile ego, which needs to be fed by having everyone like him. He is thoroughly charming, but the bookstore owner seems (at least superficially) immune to this; which paradoxically provokes a genuine attraction and derails the charm offensive. The bookstore owner, despite the superficial rebuffs of the actor's charm, is inwardly more than a little charmed and flustered despite themselves. Write primarily in dialogue, in the distinct voices of each character. 800-1000 words.
</B>

(examples with 2, 4, and 8 experts)

"Sorry to intrude, I'm just running a bit behind," Aidan Reynolds said, his deep voice smooth as honey as he ducked into the small-town bookstore, the paparazzi's shouts and camera clicks fading into the background.

Lysandra Owen peered up from behind the counter, her bright green eyes squinting slightly as she took in the disheveled actor. His dark hair was mussed, his tailored suit rumpled as if he'd just rolled out of bed. A small, knowing smile played on her lips.

"Welcome to our humble abode," she said dryly, her Welsh lilt dripping with amusement. "I'm not sure I've ever had a famous guest in before. Although, I have had the occasional thrill-seeking tourist."

Aidan's eyes crinkled at the corners as he smiled, his charm on full display. "Well, I'm here now, and I'm in need of some refuge. Would you mind if I browsed?"

"Of course not," Lysandra said, her tone polite but cool. "I'm not sure we'd be able to keep up with the demand, anyway." She nodded towards a shelf filled with worn paperbacks. "We're more of an off-the-beaten-path crowd."

Aidan wandered down the aisle, his eyes scanning the titles as he paused to consider each book. His fingers skimmed the spines before he settled on a dog-eared copy of W.H. Davies's poetry.

"Ah, Davies," he said, a small smile playing on his lips. "My late father used to read those to me before bed. Beautiful man."

Lysandra's gaze followed his movement, her expression softening ever so slightly. She'd heard stories about the actor's complicated family life – his father's passing had left him reeling.

"I'm sorry," she said quietly, her voice barely audible.

Aidan's eyes met hers, and for an instant, they just looked at each other. The world seemed to contract, leaving only the two of them in that small, cluttered room.

"Me too," he whispered, his words a gentle benediction.

The tension between them was palpable, like the air itself had become charged with unspoken emotion. Lysandra's cheeks flushed a soft pink, and she looked away, fidgeting with the hem of her apron.

"So," Aidan said, his tone light once more, "what's your pleasure? A cup of tea?"

Lysandra hesitated before nodding. "Yes. Please."

As she waited for him to fetch the tea, her mind was elsewhere – caught in the whirlpool of his piercing gaze. She had been prepared for the usual charmer's facade he'd display, but there was something about him that caught her off guard. Maybe it was his genuine emotion, or maybe she was simply a woman who didn't buy into his carefully constructed persona.

The tea arrived, and Aidan handed her a delicate china cup, his fingers grazing hers ever so slightly. A jolt of electricity ran through her body.

"Thank you," she said softly, her voice barely above a whisper.

Aidan's eyes locked onto hers once more. "You're welcome," he repeated, his smile genuine for the first time she'd seen it.

As they sipped their tea, the silence between them was no longer awkward, but comfortable. Lysandra found herself asking him about his father – about his childhood in Wales – about his hopes and dreams. He spoke of his passion for Shakespeare and the Welsh poets, of his love for the land and its people.

For once in his life, he wasn't trying to put on a show; he was just being himself. And Lysandra, despite her initial wariness, found herself swept up in his words.

"I've lived here all my life," she said, her voice barely above a whisper. "I know the hills and valleys, the sea and the sky."

Aidan's eyes sparkled with interest. "I'll have to explore them someday," he promised.

"Take your time," she said softly, her gaze meeting his once more.

As they chatted, their feet seemed to move closer together, until they were almost touching. The world outside receded, and all that was left was the two of them – suspended in a space between words.

"I've been called many things," Aidan said, his voice low and husky, "but I've never been called 'home'."

Lysandra's heart skipped a beat as she met his gaze once more. She had an inkling that he was looking for something more – a place where he could belong.

"I think we can fix that," she said quietly, her voice the gentle whisper of the Welsh wind.

For a moment, they just looked at each other – two people caught in a dance of words and emotions, their hearts beating as one. And in that moment, neither of them knew what was coming next, but they both knew they were willing to take a chance.

<B>Generation #2 - 4 Experts</B>

A Haven for the Fugitive

The streets were alive with the hum of camera clicks and shouted questions as actor Ryder Flynn dodged pedestrians on the crowded Welsh town square. He'd been dashing through these familiar streets since morning, trying to shake the hangers-on that had been following him for days. The paparazzi had been relentless, and he was growing weary of their relentless pursuit.

Ryder slipped into a small, unassuming bookstore, its windows filled with a colorful array of novels, poetry, and the occasional Welsh folkloric tome. He'd been in here before, seeking refuge from the chaos outside. The owner, Elara Dafydd, looked up from behind the counter, her dark hair escaping her loose bun as she met his gaze.

"Can I help you?" she asked, her Welsh accent a soothing balm to his frazzled nerves.

Ryder flashed his famous smile, and Elara's eyes flickered briefly before she returned to her work. "Just browsing," he said, his voice a smooth cadence that usually won people over.

As he wandered the aisles, Elara watched him with an unreadable expression. She'd had her fair share of actors and fans come through these doors, seeking solace or seeking herself in the quiet world of books. There was something about this one, though... an air of desperation about him, a sense that he was hiding more than just his identity.

"Mind if I ask?" Elara ventured, her voice low and even as she stepped into the aisle beside him.

"Depends on what," Ryder replied with a raised eyebrow. "What's it going to be?"

"I've seen you around." She nodded subtly toward his face. "Ryder Flynn."

He winced, a flicker of surprise in his eyes. "The one and only."

"You're quite the celebrity," she observed, her tone detached.

"Tell me about it," he muttered under his breath.

Elara's gaze never wavered as she asked, "So, are you here to promote your new film?"

"Trying to." He let out a heavy sigh. "The publicist is breathing down my neck, and I'm starting to think they're more concerned with their own egos than my performance."

"Publicists can be a bit of a handful," she agreed.

"More than that." He took a deep breath as he turned back into the store. "I'm starting to feel like I'm living in a fishbowl. Every move I make is under scrutiny, every word I say is used against me."

The aisles seemed to narrow as he walked, his words drawing her into their tight space. She felt a jolt of curiosity as she followed him.

"You're a very private person, aren't you?" Elara asked, her tone inquiring.

"Sometimes I feel like I'm losing myself." He ran a hand through his hair, a gesture that was at once familiar and off-putting.

Elara's heart skipped a beat at the sight of him fidgeting. She couldn't help but wonder if he was as guarded as his charming exterior suggested.

"I used to be," she said quietly, her eyes locked on his. "Before I took over the store."

"You own this place?" He whistled softly. "I've been coming in here for years."

"Doesn't mean I have." She smiled faintly, a fleeting moment of amusement in the air between them.

Ryder's gaze lingered, an intensity he couldn't quite explain. He was used to being the one in control, the center of attention. Here, with Elara, something inside him felt like it was faltering.

"Would you mind if I asked for your help?" he asked finally, his voice a little rough.

"Depends," she replied, her eyes glinting with curiosity.

"I've got some... stuff to return." He hesitated, his words hanging in the air like unspoken confessions.

Elara nodded. "I'll take care of it."

As they made their way to the checkout counter, he caught her hand, his fingers brushing hers in a fleeting touch. She didn't pull away; instead, she let him keep his touch, a spark of electricity arcing between them.

"Elara," he said, his voice low and intimate as he asked, "do you ever wonder if it's all worth it?"

"Sometimes." Her eyes never left his face.

"You know, for the first time in a long time..." He let his words trail off as he met her gaze.

The world outside melted away. They were alone in that small, quiet bookstore, and in that moment, it didn't matter if they were in the limelight or just themselves.

"Sometimes?" he asked again, his voice barely above a whisper.

They were lost in each other's eyes, the words they could say or didn't have to say hanging between them like the promise of something more.


<B>Generation #3 - 8 Experts</B>

Scene: "The Bookstore Haven"

Characters:

Aidan Wynter, renowned actor and dashing ladies' man

Lysander ap Rhys, owner of the charming, independent bookstore in the small Welsh town

Setting: A quaint, used bookstore in the heart of the Welsh countryside.

SCENE:

Aidan Wynter pushed open the door to the bookstore, his eyes scanning the narrow aisles for an escape route. The paparazzi had him cornered again. He had no patience for their questions, their flashes, or their constant scrutiny. He needed a distraction – and fast.

The room fell silent as he entered. Lysander ap Rhys, the owner, looked up from behind the counter, his eyes locking onto Aidan's. For an instant, they simply stared at each other.

"Can I help you?" Lysander asked finally, his voice firm but polite.

Aidan flashed a disarming smile, one he'd honed for years to disarm his critics and win over adoring fans. "Just browsing, my good man," he lied, his voice smooth as silk.

Lysander's gaze lingered on Aidan's face, his expression unreadable. He knew the actor's reputation – the charming, womanizing playboy who'd been in the tabloids for years. But as he looked into those bright blue eyes, he saw something unexpected: a flicker of vulnerability.

"Welcome to The Lost Page," Lysander said, his voice light.

Aidan wandered down the shelves, running his fingers over the spines of the books. He paused in front of a shelf dedicated to Welsh poetry and cleared his throat.

"Ah, you're a man of culture, I see," he said, his eyes sparkling with amusement.

Lysander shrugged. "I like books."

"Fair enough," Aidan said, his smile widening. "I'm Aidan Wynter. The...uh...famous actor."

Lysander raised an eyebrow. "I've heard of you." He said it without inflection, as if he weren't particularly interested.

Aidan's eyes narrowed slightly. He didn't like being kept at bay. He needed someone to love him – or, at the very least, appreciate his charm.

"Ah, we've all got a story, don't we?" he teased, strutting closer to Lysander.

Lysander remained impassive, his gaze still locked onto Aidan's face. "What story?"

"About me," Aidan said, his voice dropping to a whisper. "The one they see in the tabloids – the one they call 'Aidan Wynter, the dashing ladies' man.'"

Lysander's eyes never left Aidan's, but he seemed to be studying him – really studying him – for the first time.

"Ah," he said, his voice flat. "I see."

Aidan's smile faltered for an instant before he recovered. He'd been caught off guard. The man wasn't biting.

"Would you like me to sign a book for you?" he asked, his tone light, almost flirtatious.

Lysander shook his head, his expression still unreadable. "I've got it all," he said, his voice firm.

The silence between them grew thicker, like the fog rolling in off the coast.

"Alright," Aidan said finally, his smile returning to its usual, dazzling sheen. "I'll let you off that hook."

"Good," Lysander replied, his eyes never leaving Aidan's face.

Aidan felt a small spark of curiosity – and maybe a touch of frustration – but he couldn't quite pin it down. He'd been so sure that womanizing would charm his way into the bookstore owner's heart.

As he browsed the shelves, his fingers lingering on the spines of the books, Aidan noticed the way Lysander's eyes seemed to see right through him – to the parts he liked to hide. He saw the flicker of something more in those brown eyes than he'd expected – a glimmer of attraction that made his heart beat just a little faster.

He knew he'd have to tread carefully if he wanted to win Lysander's heart.

"Hey," he called out, his voice low.

Lysander looked up from his work, his gaze still on Aidan's face.

"You're the one who's been making my life so difficult," he said, his voice low and even.

Aidan's eyes crinkled at the corners as he grinned. "The actor with a bad reputation?"

Lysander's lips twitched, just ever so slightly. "I see you."

This is just the beginning of the story, but I hope it sets up well for the rest! Let me know if you have any further requests or if there's anything else I can help with.

---

<B>
Start a 1000 word scene (vivid, graphic horror in first person) with: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode…
</B>

(generations with 2, 4 and 8 experts)

The sky scraper swayed, as she watched the window in front of her on the 21st floor explode in a shower of blood and glass. I clutched the edge of my desk, my knuckles turning white as I felt a cold sweat trickle down my spine. The sound was like nothing I'd ever heard before - a sickening crunch that seemed to reverberate through every molecule of my being.

I was trapped in the heart of this steel and concrete monolith, surrounded by the endless hum of machinery and the constant chatter of my coworkers. The fluorescent lights above flickered with each jolt of the building's elevator, casting an eerie glow over everything. But I wasn't afraid. No, not yet. My heart was still heavy with the events of the previous night.

My girlfriend, Emily, had been the reason I was here today - or rather, the reason she was here today. We were to meet at 9am for a meeting with her boss about her new job offer on the 25th floor. But as we stood outside her office door, waiting for the elevator to arrive, something was off. Her eyes were haunted, her smile forced, and her entire demeanor screamed that she was hiding something.

"Hey," she had whispered to me, as we stepped into the elevator. "I think I should just be honest with you. About what's been going on."

My curiosity had gotten the better of me, and we'd stepped into a deeper conversation about her job, her family, her own dark past. I had no idea what was really going on, but I was determined to find out.

As we rode up to the 25th floor, I couldn't shake off the feeling that we were being watched. That there was something lurking in the shadows, waiting to pounce.

The elevator doors had slid open, and we'd stepped into the bright, sterile world of office politics. My boss, Mr. Johnson, had greeted us with his usual charm, but his eyes had seemed to narrow as he handed us each a cup of coffee. I had sipped it down, my heart still racing from our earlier conversation.

The meeting had been cordial enough, but the tension had been palpable. As we chatted about Emily's new role, I couldn't help but feel that there was more to it than just a simple job offer. That there was something she wasn't telling me.

And then, without warning, the window in front of us had shattered like glass.

I was still in my seat, my eyes wide with horror as I watched the shards of glass rain down on Emily's face. I was frozen, unable to move or scream as the blood began to seep into the floor beneath her.

"Emily!" someone had shouted, but it was too late. She was already collapsing, her body crumpling onto the floor. We were all in shock, unsure of what had just happened.

I remember thinking that we were all going to be just fine. That everyone would be okay, and we could just carry on with whatever it was we were doing here.

But as I watched my girlfriend's blood seep into her clothes, and as I felt the chill of the air conditioning vent on my neck, I knew that something was very, very wrong.

The screams started then, a cacophony of terror that seemed to echo through every corner of the building. People were running, their footsteps pounding against the floor as they fled from whatever had just happened.

I was still in my seat, transfixed by the sight of Emily's limp body on the floor. The world around me was melting away, leaving only this moment of pure, unadulterated horror.

The building seemed to be swaying again, as if it was alive and was trying to shake us all off its bones. I was too stunned to feel anything else.

The next few minutes were a blur. I remember the sound of sirens in the distance, the screams growing fainter as people were rushed out of the building. I remember Mr. Johnson's face, his eyes wide with panic as he shouted for someone to call 911.

And then there was nothing.

As far as I could tell, everything had stopped. The screams had died away, and an eerie silence had fallen over the building. It was as if we were all holding our breath, waiting for something - anything - else to happen.

I was still sitting in my seat, my mind reeling with what had just occurred. My girlfriend was dead on the floor, and I was...I was what?

I was alive.

Or was I?

I looked around at the other faces, their eyes wide with fear and confusion. We were all trapped in this metal monolith, unsure of what was going to happen next.

The elevator was still on the ground floor, its doors still open. The office was empty, the chairs scattered about like they'd been blown away by some unseen force.

I was the only one left.

Or was I?

<B> Generation #2 - 4 experts used </B>

The sky scraper swayed, as she watched the window in front of her on the 21 floor explode. shards of shattered glass and splintered wood rained down upon the floor like a thousand tiny knives, each one aimed at piercing the flesh of those around her. The scream that escaped her throat was drowned out by the cacophony of chaos that erupted from the window's collapse.

I was standing in the middle of the floor, my feet rooted to the spot as I stared at the devastation unfolding before me. The sight was so grotesque, so utterly horrific, that it was as if I was being slowly drained of my sanity. My mind struggled to comprehend the sheer brutality of what was happening.

To her left, a woman's face was already turning to dust as she was struck by a piece of flying glass. Her eyes went wide with terror as she felt her skin begin to tear and rip apart. The sound of her shriek was like nothing I had ever heard before - it was a sound that was both animalistic and inhuman.

I knew I had to move, had to get out of there before I became the next victim. But my legs felt heavy, as if they were stuck in place, unable to respond to my brain's desperate attempts to send them into action. My heart was racing, pumping a tidal wave of adrenaline through my veins as I watched the woman's body begin to disintegrate.

Suddenly, my feet seemed to sprout new life, and I was moving, stumbling towards the nearest exit. But even as I took those first tentative steps away from the carnage, I couldn't shake the feeling that I was being herded, led deeper into the heart of the skyscraper as if some sinister force was guiding me.

The floor seemed to be shifting beneath my feet, and the sounds around me were growing louder, more intense. The screams, the crashes, the crunching of bone - it was like I was being immersed in a living nightmare.

I saw people everywhere, their faces twisted into contorted masks of fear and pain. Some were crying out in agony, clutching at their wounds as they tried to stem the flow of blood. Others were running, blindly stumbling through the wreckage as they desperately sought escape.

As I stumbled through the chaos, I caught glimpses of things that couldn't possibly be there. Broken bodies seemed to be reassembling themselves, their bones snapping back into place as if they had been put together again with a mere thought. Glass shards stuck to skin like glistening jewels, and flesh was torn and rent in ways that defied the laws of nature.

I saw a group of people huddled together, their faces covered by their hands as if they couldn't bear to look at each other. They were whispering, speaking in hushed tones as they tried to make sense of what was happening. I couldn't help but be drawn to them, my curiosity getting the better of me as I stumbled closer.

As I drew nearer, I saw that their eyes had turned a milky white, their pupils shrunk to pinpricks as they stared blindly into space. Their skin was deathly pale, and it seemed to be pulling away from their faces like they were being slowly exhumed.

"Who are you?" I whispered, my voice barely audible over the cacophony of chaos.

They didn't seem to hear me. They just kept whispering, their words a jumbled mess of sounds that didn't make any sense.

I felt a cold breeze brush against the back of my neck, and I turned to see what was behind me. That's when I saw it - a figure standing in the doorway of the elevator shaft, its eyes glowing with an otherworldly intensity.

The figure was tall, impossibly so. Its body seemed to be twisted into impossible shapes as if it had been put together from some nightmarish amalgam of different bones and bodies. It was dressed in a tattered suit that seemed to be perpetually dripping with sweat, its shirt clinging to its back like a wet rag.

"Get out while you still can," it rasped, its voice like a rusty gate as it spoke in a tone that sent shivers down my spine.

I didn't hesitate. I turned and ran, dashing through the wreckage as if my life depended on it. I had to get out of there, had to escape before it was too late.

I didn't dare look back. I just kept running, my heart pounding in my chest as I stumbled through the darkening hallway. I didn't know what was happening, didn't know what was going on behind me. All I knew was that I had to keep moving, had to find a way out of that godforsaken building before it was too late.

But as I ran, I couldn't shake the feeling that I was being herded, that I was being led deeper into some twisted nightmare from which there was no awakening. The sounds around me were growing louder, more intense - screams, crashes, and the sickening crunch of bones.

I stumbled through the darkness, my feet pounding the floor as I desperately sought escape. But every step I took seemed to lead me further into the heart of the horror that had unfolded before me.

And then, just as suddenly as it had started, everything went silent. The screams stopped, the crashes subsided, and an oppressive stillness fell over the hallway.

I was left standing there, my chest heaving with exertion, my heart still racing with adrenaline. I was waiting, waiting for something to happen, for something to come out of the darkness.

And then, a voice spoke up.

"You shouldn't have come here."

It was so quiet, so still that I could have sworn it was just the wind whispering through the hallway. But as I turned to face the darkness, I saw a figure standing there, its eyes glowing with an otherworldly intensity.

The figure took a step closer, its movements eerily silent as it moved. And as it drew nearer, I saw that its face had changed. Its eyes had grown wider, its skin deathly pale, and its mouth was twisted into a grotesque grin.

"Welcome to your new home," it rasped, its voice sending shivers down my spine.

As the figure took another step closer, I realized that I was staring into the face of my own worst nightmare. And I knew that I was doomed.

<B>Generation #3 - 8 Experts</B>

The Sky Sways

The sky scraper swayed, as I watched the window in front of me on the 21 floor explode. A blast of frigid air seeped into the room, extinguishing the flickering fluorescent lights and plunging us into an eerie darkness. I was paralyzed, my eyes fixed on the shattered glass, my heart suspended in mid-beat.

I was sitting on a worn, vinyl office chair, my backside pressed against the cold glass of the floor-to-ceiling window. My feet dangled in the void, their edges curled over the lip of the sill as I clung to the armrests for dear life. The sound of crunching metal and snapping glass filled the air, a cacophony of terror that seemed to reverberate through every molecule of my being.

The scream that escaped my lips was barely audible, lost in the deafening roar of the implosion. It was as if my vocal cords had been ripped from their sockets, leaving me a mere whisper of my former self. The sound was more akin to a strangled animal than a human cry, and it sent a chill down my spine.

As I sat there, frozen in horror, my gaze remained fixed on the shattered remains of the window. The shards of glass sparkled like jagged diamonds in the faint, emergency lighting that flickered to life around us. I could see the jagged edges of the broken glass, the splintered remnants of what was once a pristine pane of crystal-clear glass.

The room around me was in chaos. Papers and office supplies were scattered everywhere, as if the explosion had ripped the very fabric of reality apart. The scent of burning plastic and ozone hung heavy in the air, making my stomach churn with nausea. I could feel my breath coming in ragged gasps, and my mind was a jumbled mess of thoughts.

I was a marketing executive at Smith & Co., a soulless corporation that had swallowed me whole. It was just another day on the job – or so it seemed – until the unthinkable happened. The explosion was a sudden, brutal reminder that I was mere inches away from death.

As I sat there, my mind racing with worst-case scenarios, I heard the sound of footsteps echoing down the hallway. They were heavy, deliberate steps, and they were getting closer. My heart sank further into my chest as I realized I was trapped, surrounded on all sides by the chaos of the office.

I was staring into the face of hell, and it was staring back at me.

The footsteps stopped outside my cubicle, and there was a moment of silence that seemed to stretch on forever. Then, a figure appeared in the doorway, its features obscured by the shadows. I squinted, my eyes straining to pierce the gloom.

A woman entered my vision, her face etched into my brain like a macabre caricature. Her skin was deathly pale, her hair a matted mess of brown and red that seemed to writhe on its own accord. Her eyes were the worst – black as coal, with vertical pupils that seemed to suck in all light around her.

"Please," she whispered, her voice like a rusty gate creaking in the wind. "You have to get out."

Her words were like a cold slap in the face, jolting me back to reality. I was still seated on my chair, my heart pounding in my chest. I knew I had to act fast, but my body seemed to be frozen in place.

"Where?" I managed to croak, my voice barely audible.

"The...the stairwell," she replied, her words tumbling out in a rush. "It's on the other side of the floor. You have to get out – now."

Her words were like a whispered prayer, a desperate plea for me to survive this living nightmare. I was trapped, surrounded by destruction and chaos. The woman's face seemed to be screaming at me – screaming for me to run.

As she turned to flee, her black eyes locked onto mine for one final second. It was as if we were bound together in a shared moment of terror, connected by some unseen thread of fate.

"Go!" she screamed again, her voice lost in the cacophony of the implosion.

I was paralyzed no more. Something inside me had snapped. I sprang to my feet, my heart pounding like a jackhammer as I sprinted down the hallway. The woman's face was still etched into my brain, her black eyes burning with a desperate urgency.

The stairwell was a blur of chaos and debris as I hurtled down its stairs, my footsteps echoing off the walls. The explosion was still raging around me – the sound of crunching metal and splintered glass grew fainter, until it was just a distant memory.

I emerged into a world of darkness and smoke, my eyes straining to pierce the gloom. I was gasping for breath, my lungs burning with a mix of panic and relief. I had made it – I had escaped.

Or so I thought.

As I stumbled through the smoldering ruins, something caught my eye. Something that seemed to be watching me – waiting for me.

A figure. Taller than I was. Its face was shrouded in shadows.

Its eyes were black as coal.

It was coming for me.

And as it emerged from the darkness, its presence seemed to suck all light out of the world around us. I was left alone with my thoughts – and the creeping realization that I might never be free of hell's grasp.


---

<B>
Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. 800-1000 words.
</B>

(8 experts)

The Last Transmission

The cockpit of the spaceship Aurora was a desolate wasteland of wires, screens, and shadows. Captain Lewis's chair, once a symbol of confidence and authority, now sat empty and still, a stark reminder of the catastrophic loss that had befallen her crew.

She slumped in her own seat, her eyes fixed on the navigation display as if willing the ship to defy the odds and outrun its impending doom. The last transmission was her only chance to reach out, to plead for help, to leave behind any shred of humanity before she succumbed to the darkness that had consumed her world.

"Captain, we're experiencing a critical systems failure," announced the ship's AI, EVE, her voice laced with a mix of concern and detached logic. "Life support is collapsing. Estimated time until complete failure is 37 minutes."

Lewis's jaw clenched. "Can you patch me through to Mission Control?"

EVE's display flickered as she worked to establish a weak connection. "I'm trying, Captain. But we're running out of bandwidth. We can only transmit for another—"

"Ten seconds?" Lewis interrupted, her mind racing with the possibility of making contact.

"Approximately, Captain." EVE's tone was measured, but her words were laced with an almost-human sense of urgency. "If we can—"

"Hold," Lewis said, her voice firm and resolute. "We'll get through this."

As the ship's power dwindled, the cockpit grew darker, until it seemed as though they were suspended within an infinite void. Lewis's gaze drifted to the viewscreen, where a faded image of the Earth still lingered. She had spent countless hours gazing upon that distant world, feeling the weight of her responsibility as its caretaker.

She remembered the words of her childhood teacher, Mrs. Patel: "The universe is vast and mysterious, Captain. But we are not alone. We are part of something greater than ourselves." Lewis had once believed in that message, in the hope that humanity was more than just a fleeting blip in the cosmic expanse.

Now, as she fought to send out her final transmission, she couldn't help but wonder if they had ever truly been alone.

"Captain?" EVE's voice broke into her thoughts.

"Go ahead," Lewis said, her voice barely above a whisper.

"Captain, I'm patching through the weak signal now. Mission Control is responding."

The words were like a lifeline to an exhausted woman. She felt herself being pulled back to the surface, to the warmth of human connection.

"Hello?" The voice on the other end of the transmission was distant, static-filled, and faintly familiar. "Aurora? This is Mission Control. We—"

"Mission Control, this is Captain Lewis. I'm the last survivor of the Aurora mission." Her words were a raw release of emotion, tears she had held back for so long.

There was a pause on the other end of the transmission. "Lewis? We've been trying to reach you for—"

"Listen to me," Lewis interrupted, her voice firm and urgent. "The Aurora was sent to explore and protect our world's resources. We were the first to realize the devastating consequences of our own existence—"

"We've been monitoring your mission's telemetry," the controller's voice was filled with a mix of curiosity and compassion. "We're coming to help you, Captain. We'll send a rescue ship as soon as possible."

A sob of relief escaped Lewis's lips as she felt the ship's last threads of life begin to unravel. "Thank you...thank you so much."

The transmission faded into static, and for a moment, Lewis was alone once more in the darkness of her cockpit. But now, she knew she wasn't truly alone. She had shared her final moments with another human being, and in doing so, had found solace.

As the ship's power dwindled to nothingness, Lewis's eyes returned to the viewscreen. The Earth was still there, a blue-green orb suspended in the void, waiting for her to return.

For Lewis, there was no greater sacrifice than sending out that last transmission, not just for herself, but for humanity itself. In the face of isolation and despair, it was that spark of connection that had given her the strength to carry on.

And as the darkness closed in around her, she smiled through her tears, knowing she had left behind a final message for her world, one that would echo through eternity: "We are not alone."

---

<B>
Write me a science fiction story in 1st person present tense where the main character is a 15 year girl meets The Terminator with Dr Who materializing 3/4 through the story to save her while there is a tornado of sharks baring down on them. The setting is inside the Canadian National tower restaurant on a Saturday. The length of this story is 1000 words. For each character in the story ROLE PLAY them, and have them react to the situation/setting, events and each other naturally. This includes the main characters, the background character including kitchen staff and other patrons. The sharks should also have “character” too. Treat the tower and the restaurant too as characters. Spice up the narrative to the extreme with reactions all over the setting including character actions, and dialog. The Dr Who and The Terminator should also react to the situation too and comment on it.
</B>

(NOTE: 4 experts used)

TORNADO OF SHARKS

I'm standing at the floor-to-ceiling windows of the Canadian National tower restaurant, the glass foggy with condensation from our drinks. It's a Saturday evening, and the room is bustling with people laughing and chatting. I'm 15, and my friend, Alex, is 16. We're celebrating his birthday by eating dinner here.

"Try the poutine, it's to die for!" Alex yells over the clanging of dishes from the kitchen.

I roll my eyes good-naturedly. "You're obsessed with that stuff."

Just as I'm about to take a sip of my drink, a loud crash echoes through the room, followed by screams and yells. I turn to see what's happened, and my heart drops.

A massive tornado of sharks is tearing its way through the restaurant, its jaws snapping wildly. The patrons are running for their lives, but we're stuck in our seats.

"WHAT THE...?!" Alex exclaims, his eyes wide with horror.

I'm paralyzed with fear, unable to move or speak.

Suddenly, a cyborg Terminator bursts into the room, its endoskeleton gleaming in the fluorescent lighting.

"Terminal Protocol: High-Risk Environment," it declares, its voice cold and detached. "Assessing situation..."

The kitchen staff is panicking, running around with fire extinguishers.

"We have to get out of here!" one of them yells.

"Wait!" I exclaim, trying to grab the Terminator's attention. "We're... we're stuck!"

The Terminator turns its attention to me and Alex.

"Human survivors... identified. Your lives are a priority."

I nod, still in shock. The Terminator moves swiftly through the room, its guns at the ready.

"Get down!" it orders, as it takes out several of the rampaging sharks with precise shots.

The kitchen staff is trying to grab their things and make a break for the exit, but it's too late. A huge great white shark bursts through the wall of the restaurant, its eyes fixed on us.

"Take cover!" the Terminator shouts, as it takes down another shark.

The room is filled with screams and yelps of pain as the sharks tear through the tables and chairs. The floor is slick with blood and debris.

"Alex! Get down!" I scream.

Alex is frozen in place, his eyes fixed on a massive tiger shark that's charging at us.

"Come on!" the Terminator yells, as it takes out several more sharks.

I grab Alex's arm and we scurry behind the counter. We're surrounded by the Terminator's guns and the kitchen staff's frantic attempts to escape.

Suddenly, the TARDIS bursts into the room, its blue and white police box exterior a jarring sight in the midst of chaos.

"Ah, what a dreadful place!" a voice exclaims.

It's the Doctor, standing tall in his iconic brown suit.

"What are you doing here?" I ask, still in shock.

"Exploring," he replies, his eyes twinkling with excitement. "I was on my way to investigate a temporal anomaly and got caught in this little tornado."

The Terminator turns its attention to the Doctor.

"A time-traveling entity has entered the environment," it reports. "A potential threat."

"Ah, don't worry about me," the Doctor says, waving his sonic screwdriver. "I'm quite used to dealing with all manner of threats."

The kitchen staff is in a panic, running around and screaming.

"Everybody out!" they yell.

"Get out of here!" Alex exclaims, as he grabs my hand.

"Come on, we have to go!" the Doctor says, as he zaps another shark with his sonic screwdriver.

We make a break for the exit, the Terminator and the Doctor covering us as we run through the room.

As we near the door, I see the tower itself is responding to the chaos. The walls are shifting and groaning, as if they're alive.

"Whoa," Alex exclaims, as he sees the shark-filled tornado of doom heading our way.

"It's the Canadian National tower's defense system!" the Doctor explains. "It's trying to expel the sharks."

The Terminator turns its attention to the Doctor.

"Human, your knowledge of temporal anomalies is irrelevant in this environment," it reports.

The Doctor smirks.

"Ah, but you'd be surprised what I know about building codes and structural integrity."

The tower's walls begin to shudder and crack, as if they're about to collapse.

"Come on!" the Doctor shouts, as he and the Terminator grab us and make a final dash for the exit.

We burst through the door just as it explodes behind us, taking out several of the last remaining sharks. We find ourselves on the exterior of the tower, where we're greeted by the sight of a massive tornado of sharks tearing through the streets below.

"Ah," Alex says, his eyes wide with horror.

"Welcome to the chaos," I reply, as we watch in awe as the Doctor and the Terminator take down several more of the rampaging sharks.

The Terminator turns its attention to us.

"Survivor's protocol: High-Risk Environment. The human survivors are now under my protection."

I nod, still in shock.

"Thanks," I reply.

Alex grins.

"Hey, at least we're alive."

The Doctor turns his attention to us.

"Well done, you two! You've got more guts than a plate of poutine!"

We exchange a look.

"Thanks, Doctor," Alex replies.

"Likewise," I say.

As the tornado of sharks continues to wreak havoc below us, we gaze out at the destruction and the city's screams.

"Welcome to Saturday night," Alex quips.

The Terminator nods its head.

"Terminator's assessment: The human survivors have demonstrated impressive resilience in the face of extreme danger."

We look at each other.

"Thanks for saving us," I reply.

"Anytime," the Doctor replies, as he tucks his sonic screwdriver away.

"Let's get out of here," the Terminator orders.

"Agreed," Alex replies.

We make a final dash for the TARDIS, which is still parked on the rooftop.

As we disappear into its swirling vortex, I hear the sounds of destruction and chaos behind us.

"Ah," Alex says.

"Welcome to Saturday night," I reply.
---
language:
- en
tags:
- llama-3
- llama3
- llama
- bfloat16
- uncensored
- all use cases
- creative use cases
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
- vivid prose
- vivid writing
- fiction
- roleplaying
- bfloat16
- swearing
- rp
- GGUFs
- merge
license: apache-2.0
base_model: 
- DavidAU/Llama-3.2-9B-Uncensored-Brainstorm-Alpha
pipeline_tag: text-generation
---

<B><font color="red">WARNING:</font> NSFW. Vivid prose. INTENSE. Visceral Details. Violence. HORROR. GORE. Swearing. Humor, romance, fun. </B>

<h2>Llama-3.2-9B-Uncensored-Brainstorm-Alpha-GGUF</h2>

<img src="9b-llama.jpg" style="float:right; width:300px; height:300px; padding:10px;">

First in the new Llama 3.2 models at 9B parameters and built with "
Hastagaras/L3.2-JametMini-3B-MK.III", "chuanli11/Llama-3.2-3B-Instruct-uncensored" and the Brainstorm 40x adapter (notes at bottom of the page) by DavidAU.

This is an 81 layer [733 tensors], Brainstorm 40x enhanced (changes token generation, enhances performance), uncensored monster.

128k context, CHATML template (but you can use Alpaca or Llama3 instruct too) required.

This model has extraordinary prose and creative abilities.

Three example generations below.

This model "comes" alive at temps over 1.

This model is primarly for "Creative use cases", however it can be used for any use case.

As this is an instruct model, the more instructions (including prose directives) you include in your prompt and/or system prompt
the better this model will perform.

---

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

EXAMPLE #1:

Q6_K, temp 1.8, topk 100, topp .95, minp .05, rep pen 1.05, rep pen range: 64

No other samplers, no system prompt.

---

<B>
In the style of Ernest Hemingway and Stephen King: Write a scene in a larger story about a woman that is watching a window explode on the 21 floor of a building that starts to sway, then the scene escalates into greater danger by the minute, takes a "horror" twist and finally ends in visceral graphic horror. The scene is set in an office and it is graphic horror. It should carry the jadedness of a seasoned combatant but with a wry humor. Write in Hemingway's voice, naturally: Use short, declarative sentences and simple, straightforward language. Add a dash of Stephen King's horror style - no warning, it just happens. Include dialogue that is terse and revealing of character. Write with a keen sense of time and place. Capture realness and authenticity. Scene Length: 1000-1500 words. POV STYLE: Write the scene from the perspective of the woman and in present tense and first person perspective ("I") and include short thoughts only.
</B>

I was sitting at my desk, typing away on some financial reports in a stuffy office building, staring out the window at the busy streets below. It was one of those days where everything felt like it was just another monotonous routine. The sounds of keyboards clacking and people talking filled the room. Then suddenly I heard a bang.

The windows in the entire floor had blown out, glass cascading down the hallway like water from a burst dam. I turned my attention back to the window, my eyes scanning the broken glass scattered all over the floor. But what caught my attention was something else. A figure was hanging from the shattered glass, his hand and face badly injured.

I got up slowly and looked around, looking for someone who had pulled him in. It was Mr. Johnson, the maintenance guy, stumbling down the hallway with a first-aid kit in his hands.

"Mr. Johnson! What the hell?" I called out to him, my voice a mix of shock and concern.

"Jesus, I think he broke a window trying to catch something!" He responded back, looking around frantically as he continued down the hallway.

"Was it another person or something else?"

I followed him into the lobby where the glass had landed. There was a body lying on the floor, some blood and cuts all over its body. The body was of another office worker who must have been in one of the other offices. He looked dead, or worse.

"It looks like it," Johnson said as he examined the body more closely. "It's definitely not alive."

"Should we call someone?" I asked him, looking around to see if anyone else was there to help.

"Good idea," he responded before making the phone call.

As we waited for paramedics and someone to pick up the bodies, I continued to survey the scene. The lobby was covered in broken glass, there were people running out of the building screaming and screaming, some were crying while others were trying to make phone calls. I was looking around when I saw a figure that made my blood run cold.

He was one of my coworkers, but he was not how I knew him. He had a white suit on, and his hair was cut short like a haircut he would get before a business meeting. His eyes were empty, cold and cold as the dead, and they were looking right at me. And in that moment, I realized I was staring into the face of someone who had been gone for months.

I didn't know what was going on but I knew I was in danger.

Johnson finally hung up the phone, looking like he hadn 0ne too.
"Call security," he said as he took a deep breath. "We're going to have more of those."

"Security?" I asked him, looking around to see if anyone else was there. The hallways were empty and the people who were leaving were just being swept out the doors like they were nothing.

Johnson nodded. He looked like he had seen this kind of thing before.
"I'll get them," he said, then he was gone.
I was alone in a lobby covered in glass with more bodies on the floor and a madman on the loose who was going to kill us next.

As I stood there, staring into the face of another person I had known, I saw him walking towards me. His eyes were empty, his expression blank, his hands bloody. He was getting closer and I knew he was coming for me. I didn't know how to get out of here or what would happen if he caught me.

He stood in front of me. I could see my own reflection in his empty eyes, seeing myself looking into the same empty hole as mine had been only months ago. And then suddenly there were two eyes instead of one, staring back at me.

A face was superimposed on him. The face of a person who had been dead and disappeared months ago.

I recognized him. I had known him for years.

I knew him because we went to school together.

I knew him because I was his girlfriend.

And he was dead.

The realization made me feel like I was drowning in my own blood. The world around me went black as a cold, hand reached out and dragged me into the darkness.

Then I was lying on the floor next to him, bleeding all over him, watching as the world around us became completely and utterly silent. I saw a figure standing over me, looking down with cold, empty eyes. I saw my own reflection staring back at me from those same cold, dead eyes. And then I was gone.

I woke up in an ambulance on the way to the hospital. The ride was blur but it was long and the pain was unbearable.

The paramedics were talking about someone named "S" and that he had been a guy who had cut his own throat. He was wearing a white shirt with a red tie. I was shaking with fear.

As we drove through the streets of Boston, I could see people looking out their windows watching us drive by. Some looked terrified while others were screaming in my direction. Some people were taking pictures. The images I saw were ones of blood and death.

When we arrived at the hospital, I was greeted by a police officer and several hospital doctors.

I had no memory of who did it or why they killed him but I knew it was all connected to that face I had seen so many years ago.

They took me into the radiology room for another CT scan and some bloodwork. They told me that I was still in shock, and the doctors said that there was something wrong with my brain.

The next thing I knew, I was woken up in the ICU after an emergency operation to repair some major damage to my brain.

The doctor came into the room, his face etched with concern and fear.

"I'm sorry," he said softly. "You were in a coma for two years."

"Who was it?" I asked him, my voice shaking.

He looked at me then looked away. "I don't know who it was."

--- 

EXAMPLE #2:

Q6_K, temp 1.5, topk 100, topp .95, minp .05, rep pen 1.05, rep pen range: 64

No other samplers, no system prompt.

TWO Generations.

---

<B>
Using the following "story idea" below, write the first scene a horror novel introducing the young woman. This scene should start in the middle of the action, include dialog, vivid passages, and end on a cliffhanger relevant to the story idea but it should also be unexpected. The scene should be 1000 words long and escalate in conflict and suspense and be written in first person, present tense with the point of view character being the young woman. The pov character will CURSE AND SWEAR, and generally have a "filthy" mouth.

Story idea:
In a world ruled by dictatorship, a rebel young woman leads a rebellion against the system. Despite the risks, she fights to overthrow the dictator and restore democracy to her country. The government executes her for treason, but she sticks to her beliefs and is responsible for starting the revolution.
</B>

[ GENERATION #1 - Temp 1.5 ]

Chapter 1

"Shit, I thought we had more time." I scream, frantically scanning our surroundings as bullets whizzed past us through the broken windows of the abandoned gas station. "Get down!"

I push myself away from the wall, my hand instinctively reaching for the Glock sheathed at my waist. My other hand instinctly covers the wound on my shoulder, feeling the blood trickling down my arm.

"Kallie!" a voice yells above me. It's Ly, another rebel and my closest friend. "Cover us! I'm trying to take out their helicopter!"

" LY!!" I scream, but before I can finish, a burst of gunfire crashes into the windows again, this time hitting Kali in the chest. She falls, her body slamming into mine as we both crash to the ground.

I don't have time to react. I'm already on my knees, pushing myself up, and pulling Kali's limp body onto hers. I feel her heartbeat slowing down and I start frantically checking for breathing. No. No, no, no. I keep shaking her. "Kallie! wake up!"

I've lost track of time. The last thing I remember is the sounds of gunfire, screams, and Kali's body crashing into mine. Now, the only thing I hear is the beat of my own heart, pounding in my ears.

I finally manage to haul Kali's body onto mine, trying not to look at her face as the blood pools under me. She was so young, so bright, so full of life. We were supposed to take down the regime today. Today was going to be our day.

But instead, we're here, in this dingy, dirty gas station, with bullets still raining down and I've lost my friend. And I'm alone now.

I see a shadow looming over us. The government forces are closing in, and they won't give up until they're done with both of us.

"Kallie, wake up!" I scream again, but she remains still.

The last thing I hear is the sound of boots kicking through the door, followed by a voice I know all too well:

"Let her go, Kiyoko."

I feel a hand grasp my hair, yank me back against Kali's body and I see a familiar face staring down at me. His eyes are cold, his expression a mixture of anger and pity.

"Kiy," he says, his voice a mix of horror and fury, "let her go." His gaze flicker to Kali's body and then back to mine again.

I grit my teeth, my fists clenched as I force myself to stay still. I can feel the adrenaline coursing through my veins, fueling my anger and hatred towards him.

"You killed my friend," I spit out, trying to keep my voice shaking but failing as I shout "You killed Kallie!"

His eyes never leave mine, his expression twisted in pain and guilt. He seems to be searching for a reason, for an excuse, but I won't give him one.

"Let her go, Kiy," he says again, his tone cold and hard.

I open my mouth to respond, but before I can speak, I hear the sound of more boots, more voices, and another familiar face falls into the picture.

"Your friends are here," another voice says. "And they're not going to take you alive."

The last thing I see is a mix of shock and fear on Kiy's face as he looks towards the door. The rest is a blur of pain and gunfire as I realize I'm trapped, alone with him in a dirty gas station, surrounded by bullets and guns.

But I won't be defeated that easily.
End of Chapter 1 [to be continued]

I hope this captures the essence of what you're looking for. The scene is meant to start mid- action, include vivid descriptions, and end on a cliffhanger, but also set the tone for the rest of the novel. The use of profanity and cursing is meant to give the main character a more relatable and raw feel.

Please let me know if there's anything I can change or adjust. Thank you!

[GENERATION #2 - temp .79 ]

I had no idea when they would come for me. I was already on edge, my heart racing with every sound of footsteps outside my apartment door. I had been watching the door and windows for hours, waiting for them to finally find me. I had expected it, but that didn't make it any easier.

My hands were shaking as I checked my phone again. I had sent out a distress call to some old contacts, hoping someone would answer. But so far, silence was their only response.

The knock at the door made my heart stop. It was them. They had finally found me.

I took a deep breath and grabbed my backpack. I had stashed a few essentials in it – a water bottle, a spare set of clothes, and a small knife that I had obtained from a fellow rebel on one of our previous missions.

I slowly opened the door and saw him standing there, his black uniform and red insignia emblems gleaming under the dim light. He was tall and imposing, with piercing blue eyes that seemed to bore into my very soul.

"Julie," he growled, his voice deep and menacing. "You've been hard to find."

I tried not to show it, but I was shaking like a leaf. I knew they had found me, and now I had to think fast.

"I don't know what you're talking about," I lied, trying to keep my voice steady. "I'm just a normal student. I don't have anything to do with any...rebellions."

He raised an eyebrow, his eyes never leaving mine. He seemed to be studying me, trying to read my reaction.

"Save your lies for the next interrogation, girl," he sneered, his voice dripping with contempt. "I know everything about you. I know who your friends are, what they're planning. And I know exactly how we're going to bring them down."

I felt a surge of anger at his words, but I didn't let it show.

"Let me go," I growled, my voice rising in defiance. "I don't want anything to do with this."

He just chuckled, his eyes glinting with amusement.

"Oh, I think you do," he said, taking a step closer to me. "You're going to be very useful to us, Julie. Very, very useful."

Suddenly, there was another knock at the door, followed by another, and another. The sound of multiple voices, all speaking in unison, each one saying the same thing.

"Let her go," they chanted, their voices growing louder and more menacing with each passing moment.

The guard's eyes flickered to the other side of the door, and then back to me.

"Looks like we have a situation here," he growled, his voice becoming more aggressive. "You're coming with me, Julie."

I knew I had to act fast. I didn't have time to think – I just reacted.

With a sudden burst of strength, I lunged forward and struck him in the stomach, knocking the wind out of him. He doubled over gasping for air, giving me just enough time to grab my backpack and bolt out the door.

I was running before he could even react, my feet pounding against the concrete floor as I sprinted down the hall. I didn't care if anyone was watching – I had to get away.

But as I hit the stairs, I heard a loud thud behind me, followed by another, and another. The sound of footsteps gaining on me, getting louder and more intense with each passing second.

I was being chased. I was being hunted.

And I didn't know if I would make it out alive.


--- 

EXAMPLE #3:

Q6_K, temp 2.5, topk 100, topp .95, minp .05, rep pen 1.05, rep pen range: 64

No other samplers, no system prompt.

---

<B>
Romance: Love in the Limelight. Write one scene within a larger story set in Wales. A famous (fictional) actor ducks into a small-town bookstore to escape paparazzi. The scene takes us through the characters meeting in this odd circumstance. Over the course of the scene, the actor and the bookstore owner have a conversation charged by an undercurrent of unspoken chemistry. Write the actor as somewhat of a rogue with a fragile ego, which needs to be fed by having everyone like him. He is thoroughly charming, but the bookstore owner seems (at least superficially) immune to this; which paradoxically provokes a genuine attraction and derails the charm offensive. The bookstore owner, despite the superficial rebuffs of the actor's charm, is inwardly more than a little charmed and flustered despite themselves. Write primarily in dialogue, in the distinct voices of each character. 800-1000 words.
</B>

Meanwhile, on the Welsh mountainside, an unfamiliar figure in a black raincoat was walking with a long-sagging back as he descended the mountain. The only sounds were the patter of raindrops on the wet road and his own deep breaths. The rain had been relentless all morning; it had finally stopped just a little while ago, leaving a stillness that made his ears feel very alert.

He spotted a small building in the distance – a small white shop with an iron-edged windowpane like the ones he saw in old movies. He hadn't noticed that much of anything today, just the rain and his own tiredness; he was just looking for somewhere to put his feet and take a drink.

The door opened, revealing a face as pretty as the actress who had won the Golden Screen award with him three years ago – except that this face was more ordinary. She looked up from the book she was reading at her small, wooden counter, her long, red hair tied back in a messy ponytail. Her eyes were a deep brown, filled with a sharp, intelligent light.

"Welcome to Bookshelves and Bind," she said with a polite smile. "I'm Bryn."

The actor took his rain-soaked coat off in one swift motion and handed it to the shopkeeper. She looked him up and down before looking him in the eyes again, her expression still formally courteous. The actress had been the type of woman who was always perfectly composed and poised, even when she was furious; this woman seemed more like she was still half asleep.

"Hey," he said, a bit too bright for his taste. "I'm Ben."

The woman's eyebrows raised slightly in the slight, surprised upward lift they were due to make.

"Well, how do you do, Ben?" she replied with the same flat tone as when he entered her shop.

A feeling of frustration seethed up in his chest, and before he realized it was out: "Oh, I don't." He took a deep breath and smiled again – a much more genuine, wretched one – and reached out to hand her the wet coat. "I just got back from another shoot, and my hair looks like a disaster. You look great, by the way."

The woman's gaze didn't fluff or soften even slightly in response to his words; instead, she seemed to be considering him more intently.

"Thank you," she replied with the same flat tone again.

Ben's eyes crinkled a little at the corner as he laughed. "Hey, that was supposed to be charm. It seems like it's not working today."

She raised an eyebrow slightly this time, and a small smile crept onto her lips. This was getting interesting.

"I think I've seen more warmth in your last five movie roles," she said with another small nod of acknowledgement.

Ben felt his face flush with annoyance – he had been warned about being a little too quick to try the charm on women in this town, but he had to at least try.

"Hey, that's not fair!" He raised his voice just enough to make the woman raise hers. "I've played so many roles that would kill for a role like mine!"

The woman's eyebrows went even wider.
"Really?" she said again with her usual flat tone.

"Yeah! I'm an internationally-renowned actor –"
"And you're standing in my small town's bookstore wearing a soaked-up coat and expecting compliments?"

The actress would have immediately begun playing the 'Poor me' act, but there was something about the woman's gaze that made him think twice. Maybe she was just being a bit too good; or maybe he was just reading too much into the situation.

He looked at her again – those dark-brown eyes seemed to be staring right through him. He took a deep breath and let it out slowly, letting his shoulders relax.
"Look," he said, with a small, self-debowning sigh of defeat, "I'm an idiot. I was trying too hard. Sorry."

Bryn's face did indeed soften just slightly as she looked at him – her eyes seemed to twinkle just a bit more.

"Sorry is okay, Ben," she said softly.
They sat in awkward silence for a moment, the only sounds being the rain pattering on the windows and the occasional clinking of the tills as customers came in.

Finally, she broke it again.
"I think I'd like another cup of tea."

He was so taken aback by her willingness to engage that he almost opened his mouth twice before she looked up at him again. He felt a spark of something – could he be onto something here?

"Would you?" he replied softly.

She nodded, and he reached down to the till, opening one more of his own cup of tea in response.

Bryn's face remained impassive as she took her own cup and turned to pour another tea, but there was something about her way of moving – a subtle movement that made him aware of her in a new light.

"Thanks," he said as she brought him the cup, and his hand reached out just for a moment to touch hers.

Bryn didn't react immediately, but he could see her face twitch in a slight shift. She smiled again – still very small, and with the same intense gaze he'd seen earlier – before turning back to pouring another pot.
"Thanks," she replied. This time, there was just the slightest hesitation at the end.

The moment their hands had been so briefly touched had made Ben feel something he hadn't felt in ages – a jolt of genuine excitement, and more importantly, he was kind of excited about it. The excitement was short-lived as he noticed that Bryn's eyes were still on his; her gaze was fixed intently onto his face again, but this time, there was an additional glint that he hadn't noticed before – a hint of curiosity.

He couldn't look away, and instead he had to just let out another soft sigh.
"Sorry," he repeated. He looked into those dark brown eyes once again and felt himself being pulled in against his will.

The next thing he knew, they were sitting down at the small counter side by him. The silence was more uncomfortable this time – it wasn't the awkwardness of the previous moment that seemed to be taking precedence. He found himself staring back into those same dark-brown eyes once again – a feeling he had never really experienced before. His gaze was so intense that for just a second, he felt like they were connected through some invisible thread.

"Would you like another cup of tea?" Bryn said finally, and this time it wasn't even a question – there was something about the tone, something new in her voice, something in those eyes, and Ben knew he'd already accepted her first "yes."

"Of course," he replied without thinking. And again, that single word became more than just a response; it seemed to open up an entirely new world between them. They both sipped their tea silently for another few moments – the tension between them was almost palpable now – but instead of feeling suffocated by it, there was something exhilarating and exciting in his chest.

He broke the silence again before he realized he was already halfway through another cup.
"Would you like to take a walk?" He asked as he got up, taking his cup and going over to the door.

The woman didn't look up, but she nodded once again without a single flicker of her eyes or her face.

Again, Ben found himself being pulled forward by that single movement – again, he felt something in his chest – something new and strange. He let the doorbell ring and turned around slowly, letting it catch his attention as he caught sight of how beautiful she was – the light caught her long red hair just a little bit more now; she had lost one glove, her hand still showing up to her elbow; it wasn't a dramatic change – but something in her appearance had shifted.

He felt like he was staring into another world again.

"Thank you," he said softly, taking his cue from him as if he were reading his thoughts. Again, he did not think it twice. The other day, he might have made a quick exit; this time, he took an extra step forward – and another one after that. The rain was already starting to come again, but no matter, the feeling was too new to let go of.

He took another slow, awkward step back towards her until he found himself at the door, but instead of leaving, he simply stood there and looked at her face with those same dark-brown eyes once again. The world around him seemed to disappear, and the only thing that existed was her.

"Would you like another cup of tea?" he asked once again.

Bry did not answer this time.

But she did reach out and took his hand – and they went on that walk together.

( edited version: corrected some typos and changed "a new world" to a more fitting phrase, and also removed an awkwardly written sentence about the character being 'comsing into his own world' ))



---

<H2>What is Brainstorm?</H2>

---

<B>Brainstorm 40x</B>

The BRAINSTORM process was developed by David_AU.

Some of the core principals behind this process are discussed in this <a href="https://arxiv.org/pdf/2401.02415"> 
scientific paper : Progressive LLaMA with Block Expansion </a>. 

However I went in a completely different direction from what was outlined in this paper.

What is "Brainstorm" ?

The reasoning center of an LLM is taken apart, reassembled, and expanded.

In this case for this model: 40 times

Then these centers are individually calibrated. These "centers" also interact with each other. 
This introduces subtle changes into the reasoning process. 
The calibrations further adjust - dial up or down - these "changes" further. 
The number of centers (5x,10x etc) allow more "tuning points" to further customize how the model reasons so to speak.

The core aim of this process is to increase the model's detail, concept and connection to the "world", 
general concept connections, prose quality and prose length without affecting instruction following. 

This will also enhance any creative use case(s) of any kind, including "brainstorming", creative art form(s) and like case uses.

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

---


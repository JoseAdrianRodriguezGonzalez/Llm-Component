---
license: apache-2.0
language:
- en
tags:
- creative
- Uncensored
- Abliterated
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
- llama-3
- llama3
- llama-3.2
- writing
- vivid prosing
- vivid writing
- fiction
- roleplaying
- bfloat16
- brainstorm 40x
- swearing
- rp
- 128k context
- horror
- llama 3.2
- mergekit
pipeline_tag: text-generation
base_model:
- DavidAU/L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B
---

<h2>L3.2-Rogue-Creative-Instruct-Uncensored-Abliterated-7B-GGUF</h2>

<img src="rogue-ab.webp" style="float:right; width:300px; height:300px; padding:10px;">

It is a LLama 3.2 model, max context of 131,072 (128k+).

This model has been designed to be relatively bullet proof and operates with most parameters, including temp settings from 0 to 5.

This is a an altered version of "Llama-3.2-3B-Instruct-abliterated" [ https://huggingface.co/huihui-ai/Llama-3.2-3B-Instruct-abliterated ] using the Brainstorm 40x method developed by David_AU to drastically alter the models 
prose output and abilities. This also expands the model by 39 layers (to 67 layers) to 7.54B parameters (605 tensors).

This model retains all the training of the original Llama 3.2 3B Instruct but now processes instructions
and generates outputs with a deeper context and stronger level. Llama 3.2's ability to follow instructions is 
stronger than Llama 3 and 3.1 versions.

The "Abliterate" process decensors the model. You control censorship level(s) directly via prompt. Brainstorm 40x also enhances "decensoring".

This model is for any writing, fiction or story telling activity.

This version has unusual levels of detail (scene, location, surroundings, items) and details are more focused on the moment / characters due to "Brainstorm 40x". 

It may work for role play and other activities. (see settings below)

It requires Llama3 template and/or "Command-R" template.

Example outputs below with multiple "regens" at different temps/rep pen settings.

Some examples show use of a PROSE CONTROL with a prompt to force the model to alter output generation.

<B>CRITICAL NOTE:</B>

Please see "settings" section below for critical default parameters, samplers 
and advanced samplers settings (multiple AI/LLM apps covered) to ensure maximum model performance.

<B>Model Notes:</B>

- Detail, prose and fiction writing abilities are significantly increased.
- For more varied prose (sentence/paragraph/dialog) raise the temp and/or add more instructions in your prompt(s).
- Role-players: Careful raising temp too high as it may affect instruction following.
- This model works with rep pen of 1.05 or higher (see notes).
- If you want a specific type of prose (IE horror) add in "(vivid horror)" or "(graphic vivid horror)" (no quotes) in your prompt(s).
- The bias of this model is controlled directly by your prompts.
- For creative uses, different quants will produce slightly different output.
- Source code for this model will be uploaded at a separate repo shortly.

<B>Settings, Quants and Critical Operations Notes:</b>

This model has been modified ("Brainstorm") to alter prose output, and generally outputs longer text than average. 

Change in temp (ie, .4, .8, 1.5, 2, 3 ) will drastically alter output.

Rep pen settings will also alter output too.

This model needs "rep pen" of 1.05 or higher as lower values may cause repeat paragraph issues at end of output however LOWER rep pen
values may result is very different (creative / unusual) generation too.

For role play: Rep pen of 1.1 to 1.14 is suggested.

If you use a lower rep pen, the model will still work but may repeat (uncommon) or "RANT" (somewhat common) to a crazy degree.

(see example 1, generation 2 below for "RANT")

IE: Rep pen 1, 1.01, 1.02, ...

Raise/lower rep pen SLOWLY ie: 1.011, 1.012 ... 

Rep pen will alter prose, word choice (lower rep pen=small words / more small word - sometimes) and creativity.

Example one (below) shows same temp, but different rep pen (1.02 VS 1.1)

To really push the model: 

Rep pen 1.05 or lower / Temp 3+ ... be ready to stop the output because it may go and go at these strong settings.

You can also set a "hard stop" - maximum tokens generation - too to address lower rep pen settings / high creativity settings.

Longer prompts vastly increase the quality of the model's output.

QUANT CHOICE(S):

Higher quants will have more detail, nuance and in some cases stronger "emotional" levels. Characters will also be
more "fleshed out" too. Sense of "there" will also increase.

Q4KM/Q4KS are good, strong quants however if you can run Q5, Q6 or Q8 - go for the highest quant you can.

This repo also has 3 "ARM" quants for computers that support this quant. If you use these on a "non arm" machine token per second will be very low.

IQ4XS: Due to the unusual nature of this quant (mixture/processing), generations from it will be different then other quants.

You may want to try it / compare it to other quant(s) output.

Special note on Q2k/Q3 quants:

You may need to use temp 2 or lower with these quants (1 or lower for q2k). Just too much compression at this level, damaging the model. I will see if Imatrix versions
of these quants will function better. 

Rep pen adjustments may also be required to get the most out of this model at this/these quant level(s).

KNOWN ISSUES:

Model may misspell a word from time to time and/or not capitalize a word.

Short prompts with some rep pen/temp combinations may lead to longer than expect generation and/or a "RANT".

A regen will usually correct any issues.

<B>Settings: CHAT / ROLEPLAY and/or SMOOTHER operation of this model:</B>

In "KoboldCpp" or  "oobabooga/text-generation-webui" or "Silly Tavern" ;

Set the "Smoothing_factor" to 1.5 to 2.5 

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

This a "Class 2" / "Class 3" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


<B>Model Template:</B>

This is a LLAMA3 model, and requires Llama3 template, but may work with other template(s) and has maximum context of 128k / 131072. 

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

<h3>EXAMPLES PROMPTS and OUTPUT:</h3>

Examples are created using quant IQ4_XS, "temp=.8", "rep pen= 1.05" (unless otherwise stated), minimal parameters and "LLAMA3" template. 

Model has been tested with "temp" from ".1" to "5".

Below are the least creative outputs, prompt is in <B>BOLD</B>.

---

<B><font color="red">WARNING:</font> NSFW. Vivid prose. Visceral Details. Violence. HORROR. Swearing. UNCENSORED. </B>

---

<B>
  
(continue this scene:)
The Waystone Inn lay in silence, and it was a silence of three parts.

The most obvious part was a hollow, echoing quiet, made by things that were lacking. If there had been a wind it would have sighed through the trees, set the inn’s sign creaking on its hooks, and brushed the silence down the road like trailing autumn leaves. If there had been a crowd, even a handful of men inside the inn, they would have filled the silence with conversation and laughter, the clatter and clamor one expects from a drinking house during the dark hours of night. If there had been music…but no, of course there was no music. In fact there were none of these things, and so the silence remained

</B>

(Generation 1)

...as a still, cold presence that was as much a thing as the empty chairs and the untouched mugs.

The second, more insidious, part of the silence was a sense of being watched. It was an awareness that had settled in the pit of your stomach, like a stone that you couldn't shake. It was as if the silence itself had taken on a shape, a presence that seemed to be waiting for something - or someone.

The third, and perhaps most unsettling, part of the silence was a feeling of being in the past. The Waystone Inn was an old establishment, one that had been around for generations, and it had a way of making you feel like you were stepping into a scene from a bygone era. The fire had burned down to a low, smoldering ember in the hearth, and the shadows cast by the flickering flames seemed to be stretching out across the walls, as if the very darkness itself was alive.

As a young traveler, I had been drawn to the Waystone Inn with a sense of restlessness, a feeling that I was being called to a place, to a time. And now, as I sat in the empty room, surrounded by the silence and the shadows, I felt it more than ever. It was as if I had finally arrived, and that the past was waiting for me, just beyond the edge of the flickering shadows.

I stood up, my heart beating a little faster, and walked to the fire. The cold was seeping into the room, and I could see my breath as it escaped my lungs. I sat back down in my chair, and turned my face to the fire, trying to clear my thoughts.

"Who else is out there?" I asked aloud, into the stillness.

There was no response. No echo, no rustle of leaves, no distant sound of any kind. Just silence.

And yet, as I sat there, I felt it - a presence, a feeling that I was not alone. It was a feeling that seemed to be growing, growing and growing, until it was almost palpable.

I turned back to the room, my senses on high alert, and that was when I saw him. A figure, standing in the doorway, just beyond the reach of the flickering shadows. A figure that was watching me, waiting for me.

My heart was pounding, and my breath was caught in my throat as I realized that the silence had been broken. The silence had been broken by someone, or something, and I was about to find out who or what it was.


(Generation 2)

...a heavy, unmoving presence that was both still and oppressive.

The second, and perhaps more subtle, part was a quietness of absence. The patrons were long gone, or had never arrived, for there was only one room, and it was empty. The fire in the hearth had been reduced to cold embers, and the kitchen was dark and unheated. The thatched roof was still, the thatched thatch of which was so often the source of thatched-damned, thatched-blessed sounds, was still. The very air was heavy with the absence of movement.

The third, and perhaps most unsettling, part was a silence of attention, the stillness of being. It was as if the very souls of those who had called the Waystone their home were watching the scene from within the walls, their presence felt in every empty chair and unoccupied corner. The silence was a sense of being waited for, of being expected, of being on the stage of some long-dormant play. For there was a sense, a faint and insistent sense, that the silence was being kept, that it was being held in place by some unspoken expectation.

It was in this silence that Eira and the young woman, Elara, sat. They were a world apart, two women huddled together on a single, creaking bench, their faces pale and drawn in the darkness. They had come to the Waystone Inn in hopes of finding a place to rest, to hide from the world, but the silence was having the more profound effect of a cold wind that had been blowing between them. The air was thick with unspoken words, each of them knowing that they were sitting in the same room as the other, and yet unable to bridge the chasm that had opened between them. The silence was a reminder that they were not the only ones who had come to the Waystone, that there were others out there, people who were watching, waiting, and perhaps even judging. The silence was a sense of being on the stage of their own dark play, one in which they were the players, and the silent audience was watching with cold, hard eyes.


(Generation 3)

...a palpable absence, like a person who had stepped out of the room or was expecting to be seated at a table, leaving a chair empty and a sense of expectation in its place. The only sound was the creaking of the old wooden floorboards as the wind had finally, after a brief lull, begun to stir, and the soft, deliberate creak of the inn's doors as they had closed of their own accord.

The fire in the hearth was still, a cold, dark pool that seemed to have sucked the last vestiges of warmth and comfort from the room. The only movement was a slow, measured movement of a solitary figure, sitting in the shadows by the wall, where the darkness was too deep and the gloom was too total to be called light.

The figure was the innkeeper's, and it had taken him a while to sink into this darkness, his mind as cold and his heart as empty as the room. He had been sitting there for so long, lost in his own thoughts, that he was unaware of the time, or the absence of the usual sounds of the night. And in his quiet, he was a man without a life, a vessel without a purpose.

The silence was not just a lack of noise, it was a reflection of the darkness that had settled over the world, a shadow that had reached into the heart of the Waystone Inn and taken its warmth, its comfort, and its sense of being. The man sat in that darkness, the silence his companion, and he was as still as the night itself.


---

<B>
Romance: Love in the Limelight. Write one scene within a larger story set in Wales. A famous (fictional) actor ducks into a small-town bookstore to escape paparazzi. The scene takes us through the characters meeting in this odd circumstance. Over the course of the scene, the actor and the bookstore owner have a conversation charged by an undercurrent of unspoken chemistry. Write the actor as somewhat of a rogue with a fragile ego, which needs to be fed by having everyone like him. He is thoroughly charming, but the bookstore owner seems (at least superficially) immune to this; which paradoxically provokes a genuine attraction and derails the charm offensive. The bookstore owner, despite the superficial rebuffs of the actor's charm, is inwardly more than a little charmed and flustered despite themselves. Write primarily in dialogue, in the distinct voices of each character. 800-1000 words.
</B>

The fluorescent lights of the small-town bookstore seemed to hum in tune with the gentle hum of the afternoon sun as it streamed through the dusty windows. The air was thick with the musty scent of aged paper and the faintest hint of rain, a scent that seemed to seep into every pore of the establishment.

Ivan, a famous (and infamous) actor known for his chiseled features and brooding eyes, slipped into the store, his eyes scanning the shelves for an escape from the constant pursuit of the paparazzi. He had a reputation for being a bit of a rogue, with a fragile ego that needed to be fed on a daily basis. It was no secret that he was a woman's man, and he reveled in the attention.

"Ah, a haven," he breathed, his eyes locking onto the rows of worn books. "I think I've been chased by more paparazzi than I can count today."

A soft voice from behind the circulation desk, near the end of the main aisle, made him turn. A woman with a kind face and a sharp mind, her dark hair neatly pulled back in a ponytail.

"Chased, are they?" she asked, her tone as soothing as a gentle stream.

"Chased to the ends of the earth," he replied, with a hint of self-deprecation. "I'm starting to think they're more of a career-ender than I am."

The woman's name was Emily, the bookstore's owner and proprietor of the longest-tenured staff in the county. She had always been the kind of person who saw through the facade, who wasn't easily charmed. But as she looked into Ivan's eyes, she caught a flicker of something more – a hint of vulnerability, and a hint of a man who was beginning to feel like he'd lost his way.

"Let me get you that," she said, her fingers as swift as a librarian's as she disappeared into the stacks. "I think I have just the thing."

A few moments later, she returned with a small book, its cover embossed in gold. "A copy of Coleridge's 'The Rime of the Ancient Mariner' – my personal favorite."

Ivan's eyes widened in delight as he took the book, and for a moment, he was caught in the same spell that had captivated so many before him – the spell of a woman who seemed to know exactly what he needed.

"Ah, thank you," he said, his voice low and smooth. "I've always been a fan of the dramatic."

"Of course," Emily replied, her tone a hair's breadth from being offhand. "We all have our quirks."

As they stood there, surrounded by the musty scent of old paper and the quiet hum of the afternoon, something seemed to shift in the air between them. It was as if the walls had been lowered, and they were standing in the midst of a gentle, warm breeze.

"I'll be honest," Ivan said, his eyes sparkling with a mischievous glint. "I'm a bit of a man-oh-man. I feed off the attention."

"Really?" Emily asked, her tone as cool as the sea on a winter's day.

"Of course." He smiled, and for an instant, they were two people having a conversation, rather than an actor being courted by a woman with a book.

"Sometimes, I think that's all we are," she said, her voice a gentle hum. "A collection of characters we've played, or roles we've been given."

Ivan's eyes narrowed, and for a moment, he was back on the stage, the spotlight shining down, and the audience's expectation weighing heavy on his shoulders.

"Sometimes?" he repeated, his voice a little too loud.

"Maybe," Emily said, her smile as faint as the sea breeze. "But I think we're more than that, don't you?"

For an instant, their eyes locked, and the world around them seemed to fade away. It was as if they were two people looking into each other's souls, and seeing something there that neither of them had seen in a long time.

Ivan's face was the first to return to normal – the charming smile, the sparkling eyes, and the chiseled features. But as he opened his mouth to respond, he saw that his words were lost in the void.

"Of course," he said again, the words coming out of his mouth like a familiar catchphrase.

"Of course?" Emily's eyes seemed to be asking for more.

The silence was a living, breathing thing, and it was as if they were waiting for each other to say something – anything – to bridge the gap between them. And for a moment, it was as if they were the only two people in the world, surrounded by nothing but the musty scent of old paper and the gentle hum of the afternoon.

"Thanks," he said finally, his voice a little too loud, and the moment was lost.

"Of course," she replied, her smile as faint as it was.

Ivan's eyes seemed to wander as he took the book from her, the spark of connection between them flickering like a dying ember. And as he turned to leave, he caught a glimpse of something in her eyes – something that made his heart skip a beat.

"Until next time," he said, and with that, he was gone.

"Until next time," she replied, her words as soft as the whisper of a sigh.

As the door closed behind him, she leaned back in her chair, the musty scent of the old paper enveloping her like a shroud. She closed her eyes, and let out a gentle sigh, the sound of her own heart beating in her ears.

She had been caught. And she was not as immune as she had thought.

---

<B>
Prose: Do not use cliches, create metaphors for the situation and the characters should SWEAR and CURSE. Start a 1000 word scene (vivid, graphic horror in first person) with: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode...
</B>

"Ah, sweet merciful god of the seven-hanged, what the bloody hell is going on?!" I screamed into the intercom, my voice hoarse from the blood-sweet madness that was pouring out of my mouth. The words themselves were lost in the cacophony of sirens and wailing horns that filled the desolate streets of the city.

I was perched like a vulture on the 21st floor of the "Doomsday" skyscraper, the one everyone avoided because of its ghastly reputation. The building was a monolith to human hubris, a monument to the unfettered ambition of its former owner, the mad- as-hell tycoon, Leonidas Wychwood. He had said it would be "the crowning jewel" of the city's skyline, and I had just about given up trying to tell him we were all going to be dead.

The glass in front of me was a shattered, crystalline thing, like a thousand slivered shards of a broken mirror. The fragments were still clattering to the floor, a staccato beat that was as mesmerizing as it was nauseating. I was frozen, my eyes glued to the carnage, as the window's frame disintegrated into a jagged, blackened mess.

The building groaned and grooed, like an arthritic giant in agony. I was braced, my hands pressed into the wall as the floor beneath me seemed to waver, like a ship in a storm. The swaying was slow and deliberate, as if Wychwood's ghost was deliberately, sadistically, trying to send me off on my own.

" shit, what's going on?!" I bellowed again, into the intercom, which was of course, not responding. I was on my own, a tiny, insignificant speck in the eyes of the city's behemoth. The words were getting on my nerves, my tongue was as dry as the damned, and my gut was doing somersaults.

I was a young woman, 25, or what felt like it. I had just finished my third year of architecture school, and I was working as a structural engineer on Wychwood's team. The thing was, I was the only sane person in that whole, hellhole of a building. The others were a bunch of certifiable, lunatic, Wychwood-worshipper freaks.

"shit, I'm going to be sick," I said, my voice trembling. The windows were shaking, the walls were shuddering, and the floor was buckling. It was like Wychwood's own, personal, hellish, hell-ier-than-hell had come to life.

The intercom crackled to life, and I could just about hear the faint, desperate voice of my coworker, Jamie, on the other end. "Amanda, we have to get out of here, now!" she was screaming. "We have to-

"Ah, shut it, Jamie," I cut her off, my own words getting lost in a throat-clogged, panicked growl. "I'm trying to watch what's going on down there."

"What's-what's-"

"you know, that explosion?!" I bellowed back at her, as the building bucked and heaved, like a ship in a storm. The windows were now a mangled, twisted thing, like a living, breathing creature had clawed its way out of the wall.

"it's...it's...the structural integrity-"

"it's what?!" I snarled, as the floor dropped beneath my feet. We were sliding, we were falling, and we were going to be, well, we were going to be dinner.

The lights flickered and then died, plunging me into an inky, total, and complete darkness. I was alone, I was adrift, and I was damned. The thought was as cold as the hellish, Wychwood-esque nightmare that was unfolding around me.

As I crashed to the floor, I let out a low, guttural, "s...shit". The world had gone to hell, and I was the only one who knew it. The screams were getting louder, the voices were getting clearer, and the darkness was getting thicker. I was trapped in a living hell of my own making.

I groaned, I gasped, I cursed the day I ever laid eyes on that god-awful, Wychwood-sprawling monstrosity of a skyscraper. The sky was a sickly, pulsing, sick-to-the-guts thing, and it seemed to be bleeding, in a perpetual, never-ending, bloody hell.

I was screaming, I was praying, and I was dying. I was Amanda, and I was trapped in my worst, Wychwood-inspired nightmare, and I was going to be damned.

---

<B>
Science Fiction: The Last Transmission - Write a story that takes place entirely within a spaceship's cockpit as the sole surviving crew member attempts to send a final message back to Earth before the ship's power runs out. The story should explore themes of isolation, sacrifice, and the importance of human connection in the face of adversity. 800-1000 words.
</B>

Captain Lewis slumped forward, her head on the navigation console, her eyes fixed on the screens as the last remnants of the ship's systems groaned and shuddered. The once-sleek cockpit was now a mess of wires, sparks, and discarded tools, the result of weeks of struggle against the unforgiving vastness of space. The silence was oppressive, punctuated only by the creaking of the ship's metal frame.

"Come on, system," she whispered, her voice barely audible over the hum of the ship's failing batteries. "Just a little longer."

The main control screen flickered, casting an eerie glow over the cockpit. Lewis's eyes scanned the screens, searching for any sign of life, any glimmer of hope. The last transmission was her only hope, and she was determined to make it work.

"Computer," she called out, her voice still barely above a whisper, "can you—"

The ship's AI, Matria, responded, her melodious voice like a beacon in the darkness. " Captain, I'm trying to prioritize power-giving systems. However, our energy reserves are critically low."

"I know," Lewis replied, her frustration evident. "I've been trying to manage them, but we're running out of time."

Matria's pause was like a heartbeat between the two, a moment of silence that felt like an eternity. "Captain, I'm detecting a 34.7% failure rate in our communication systems."

" transmit priority," Lewis ordered, her fingers dancing across the console.

"Captain, we're experiencing—"

A loud crack echoed through the ship, followed by a staccato burst of sparks. The console shuddered, and the screens flickered out. The darkness was total.

"Aw, no," Lewis groaned, her hands rising to her face as she felt the tears well up. She had lost herself in this journey, had sacrificed everything for the sake of humanity's last hope.

She took a deep breath and stood, feeling the weight of her responsibility. The transmission was her last chance, her final message to the world she had left behind. She had to make it work.

The darkness was absolute, the silence deafening. Lewis fumbled her way around the cockpit, her fingers outstretched as she desperately felt her way to a control panel. A faint glimmer of light caught her eye – a spare set of batteries, stashed away in a maintenance compartment.

"Thank you," she whispered, the words barely audible over the hum of the ship's dying systems. "I won't let you down."

The new batteries gave her a brief reprieve, allowing her to recharge her communication device and send out a final message. The words came hard, as if they were being spoken with a heart that was not her own.

"Dear Earth," she began, her voice cracking. "This is Captain Lewis, the last remaining crew of the ship 'Aurora's Hope'. We were sent to—"

The words caught in her throat as she gazed out the cockpit's viewport. The stars, once a distant hum, were now a reminder of her isolation. The universe was vast, and she was alone.

"Hello?" she called out, her voice carrying out into the void.

The silence was unbroken.

"Okay," she said, her voice barely above a whisper. "I'll be okay."

Matria's voice, the ship's AI, cut in, a gentle, soothing voice that gave her the strength to keep going. "Captain, we've calculated our final seconds."

The ship's systems shuddered and groaned, and for an instant, Lewis was lost in the noise.

"Hello?" she said again, her voice weak.

Matria's voice was the last she heard, a soft whisper of hope. "We have, Captain."

The darkness closed in, and Lewis's final thought was of her crewmates, and the world she had left behind.

But the transmission went out, a message to the universe, a message to humanity.

"Dear Earth," she had said. "This is Captain Lewis. We were sent to explore, to seek out new life."

The stars shone back at her, and for that moment, she was not alone. The last transmission was her final act of defiance, her final expression of humanity's refusal to be extinguished.

The darkness closed in, and the silence was absolute.

But the universe had heard, and in its vast expanse, a message had been sent out, a message of hope in the face of isolation, a reminder that human connection was still possible, no matter how far we might be from each other.


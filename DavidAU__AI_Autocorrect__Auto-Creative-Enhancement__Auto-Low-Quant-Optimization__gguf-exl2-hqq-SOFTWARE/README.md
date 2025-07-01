---
license: apache-2.0
language:
- en
tags:
- AI hybrid software
- AI AutoCorrect Software
- AI AutoCreative Enhancement
- AI Auto Low Quant Enhancement and Optimize
- AUTO Reconsider Systems
- Live Streaming Auto Enhancement in Real Time
- ALL GGUF enhanced
- ALL EXL2 enhanced
- ALL HQQ enhanced
- ALL Full source enhanced
- ALL GPTQ enhanced
- ALL AWQ enhanced
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
- vivid writing
- fiction
- sillytavern enhancement
- horror
- llama 2
- llama 3
- llama 3.1
- llama 3.2
- llama 3.3
- Qwen
- command-r
- mistral
- mistral large
- deepseek
- gemma
- phi
- llama
- llama-3
- gemma
- gemma2
- gemma3
- llama-2
- llama-3.1
- llama-3.2
- mistral
- moe
- mixture of experts
- mixtral
pipeline_tag: text-generation
---

<h2>AI Autocorrect / Auto Creative Enhancement / Auto Low Quant Optimization - gguf - exl2 - hqq - SOFTWARE By DavidAU</h2>

RELEASE VERSIONS AVAIL: 1.12.12 // 1.12.11 //

<img src="flying.gif" style="float:right; width:300px; height:300px; padding:10px;">

This engine/system is for ALL GGUF, EXL2, HQQ and other model quants/compressions and full source/full precision models too and can be used
with any AI/LLM app that has API such as Llama-Server, LMStudio, Koboldcpp, Text Generation Webui etc etc.

I put 3 decades of programming experience, 100s of model builds and 1000s of model tests into creating an AI / programming hybrid.

This fully automated engine is designed to actively alter / fine tune the generation stream in real time of any AI/LLM which includes active "auto-correction"
(which includes an optional temp/top_k "scrambler") and passive / active "auto-reconsider" (an optional system to augment real time generation, which includes an optional temp/top_k "scrambler").

The engine actively corrects, in real time during streaming generation (sampling at 50 times per second) the following issues:

- letter, word(s), sentence(s), and paragraph(s) repeats.
- embedded letter, word, sentence, and paragraph repeats.
- model goes on a rant 
- incoherence
- a model working perfectly then spouting "gibberish".
- token errors such as Chinese symbols appearing in English generation.
- low quant (IQ1s, IQ2s, q2k) errors such as repetition, variety and breakdowns in generation.
- passive improvement in real time generation using paragraph and/or sentence "reconsider" systems.
- ACTIVE improvement in real time generation using paragraph and/or sentence "reconsider" systems with AUX system(s) active.

The system detects the issue(s), correct(s) them and continues generation WITHOUT USER INTERVENTION.

The original intent of this "Auto Correct" engine was to allow users of my class 2, 3, and 4 models to use these models under
all conditions, without restrictions and allow all of the "power" of these models to be available without any
of the negatives such as special settings, parameters and/or samplers to "reign" in the bad behaviour of these models.

Class 2, 3 and 4 models have incredible creative "chops" but the downside is they can be very difficult to use - AutoCorrect engine
is the automated, hands off answer to this issue.

In otherwords the following models (and all their brothers and sisters) will now operate perfectly, under all conditions:

https://huggingface.co/DavidAU/L3-DARKEST-PLANET-16.5B-GGUF

https://huggingface.co/DavidAU/MN-DARKEST-UNIVERSE-29B-GGUF

https://huggingface.co/DavidAU/L3-Stheno-Maid-Blackroot-Grand-HORROR-16B-GGUF

https://huggingface.co/DavidAU/DeepSeek-R1-Distill-Llama-3.1-16.5B-Brainstorm-gguf

( this model/repo includes output examples using AI Autocorrect )

https://huggingface.co/DavidAU/L3.1-Dark-Planet-SpinFire-Uncensored-8B-GGUF

(this one has a posted example generation using this software at the bottom of this page)

And many, many more models...

NOTE: 

I will be adding additional generation examples from different models at the bottom of the page shortly too using the software enhancements.

And the software also allows the release of stronger models at class 5 and above - yet allow users (including myself) - to be able to
use these models under all conditions WITHOUT the need to manually stop, fix, or steer generation NOR set parameters
and/or samplers to "reign" in the bad behaviour of these models.

Yep - have your cake and eat it too.

And all models - my repo and others - will all operate better.

Because many of the issues with "creative" / "unstable" models are the same as using low and ultra low quants (Q2k, IQ1s,IQ2s) this
engine also fixes on the fly many of these issues too, resulting in the ability to use models at these ultra low quant levels with enhanced results.

And in some cases, allowing use of these low bit quants in normal operation.

Example: 70B model, IQ1S 

-> System will autocorrect generation, especially "repetitive" issues that can occur at this low quant level.

-> Reconsider system (if on) will further enhance generation, with even stronger enhancement if the temp/top_k scrambler for "Reconsider" is on too.

Low / Ultra low quants can also benefit from the "Reconsider" system, especially with "aux" system "scramble temp/top_k" ON which helps
correct issues like low creativity / low variety at these quant levels and can also help repetitive issues too.

Keep in mind these systems will also enhance generation of any quant, and of course full precision models too.

This engine/process has the net effect of live fine tuning the model's generation and creates a "back and forth" between the engine
and the AI/LLM - a live, two way street - creating a partnership in generation.

Unlike parameters and samplers however (to limit/control model behaviour), this is a just in time/as needed autocorrect engine only responds and takes
action as required only.

This allows the model to operate at full power, WITHOUT sampler/parameter restrictions which can DULL/REDUCE model performance in many cases.

Likewise this allows you to use parameters/samplers at FAR HIGHER settings - ie really push the model hard - and still have COHERENT generation.

AUTO CREATIVE ENHANCEMENT - RECONSIDER SYSTEM:

In addition this engine has a passive "RECONSIDER" system that operates per paragraph, and/or per sentence too, which further augments generation.

This has passive, and active settings.

(this/these can be turned on/off)

And this "reconsider" system has an aux system too: 

Each time the model "reconsiders" (per paragraph and/or sentence), the systems can change temp / top_k parameters per paragraph and/or sentence automatically 
This drastically affects generation, and strongly breaks predictiveness of the model. 

This can also help low/ultra low quants generation and/or low parameter count models too which can suffer from predictive output / repeat generational issues.

These will also enhance any quant's generation too, including full precision.

It has five settings (1-5) besides on/off:

	// 1 = MILD [default]
	// range .05 to .95 Temp ; k => 40 to 70.

	// 2 = MED
	// range .5 to 1.8 Temp ; k => 30 to 90.

	// 3 = HIGH
	// range .8 to 3.25 Temp ; k => 20 to 150.

	// 4 = SPICY
	// range 1 to 5 Temp ; k => 5 to 400.

	// 5 = YOUR defaults MAX
	// Uses your temp / top k settings but randomizes them to whatever the max temp / top_k you have set.
	// IE if you set temp of 1.5, and top_k of 100 -> System will pick values from .01 to 1.5 for temp, and 5 to 105 for top K.

    // 6 = Uses defaults DOES NOT SCRAMBLE temp/topk.  [added Beta V 1.1]  (called "low/low")

(this aux system is OFF by default)

AUTO CORRECTION SYSTEM:

And when the model is directed to "make changes" (Auto Correction) (after the engine edits out the issue(s)) it scrambles parameters (temp, top_k) to force
the model to make a more "creative" decision (or at least a better one). More on this below.

(this can also be turned on/off) AND has these settings too:

	// 1 = MILD [default]
	// range .05 to .95 Temp ; k => 40 to 70.

	// 2 = MED
	// range .5 to 1.8 Temp ; k => 30 to 90.

	// 3 = HIGH
	// range .8 to 3.25 Temp ; k => 20 to 150.

	// 4 = SPICY
	// range 1 to 5 Temp ; k => 5 to 400.

	// 5 = YOUR defaults MAX
	// Uses your temp / top k settings but randomizes them to whatever the max temp / top_k you have set.
	// IE if you set temp of 1.5, and top_k of 100 -> System will pick values from .01 to 1.5 for temp, and 5 to 105 for top K.

    // 6 = Uses defaults DOES NOT SCRAMBLE temp/topk. [added Beta V 1.1] (called "low/low")

(this system is set to "2" by default)

<B> INSTALL: </B>

This engine is a software patch in the SillyTavern AI/LLM frontend system. You need to install SillyTavern then the "script" patch... then connect SillyTavern
to the AI/LLM app such as Lmstudio, Text Generation Web UI, Koboldcpp or Llama-Server AND/OR API (local or remote).

VERY IMPORTANT - RELEASE VERSION ONLY: 

This patch requires the "release" version of the model, it may not work with other branches. If you attempt to use it with other
than the exact "release version" and get a blank screen - revert, and use the "release" version.

Download SillyTavern here:

https://github.com/SillyTavern/SillyTavern

AI/LLM Apps:

https://www.lmstudio.ai

https://github.com/ggerganov/llama.cpp  ( Llama Server: https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md )

https://github.com/LostRuins/koboldcpp

https://github.com/oobabooga/text-generation-webui

As SillyTavern also supports "remote" connections to AIs/LLMs you can also connect (to AIs/LLMs) this way too.

The AutoCorrect engine operates within the core controllers within SillyTavern.

Current SillyTavern users:

You may need to update your version of SillyTavern before install, as both the "new core" and version of Silly Tavern
you have installed must match. 

Once SillyTavern is installed, download the "script...js" file for your VERSION 
(the version number is IN the filename) of Sillytavern and save this file to "public" folder :

Example:

F:\sillytavern\SillyTavern-Launcher\SillyTavern\public

Then RENAME "script.js" to "script-org.js" and then RENAME the file you downloaded to "script.js" (no quotes).

You can then start SillyTavern normally, and connect to AI/LLMs as you normally would.

Additional Versions with Settings Already Set:

This will have "spicy-spicy", "off-off" etc etc in the file name.

This means the settings for "Autocorrect" and "Reconsider" are already set for you.

ADDITIONAL:

You can have multiple versions of ST installed on your computer. You may want to have one with this "patch"
and another with "normal" ST.

All you need to do is duplicate your install of ST (copy the entire folder, and paste/rename), and then add some shortcut(s) to:

IE:
F:\SillyTavern-1.12.11\SillyTavern-Launcher\SillyTavern\Start.bat

"Start.bat" starts ST.


<B> SETTINGS: </B>

Settings are adjusted by editing the "new" script.js file in NOTEPAD  (DO NOT edit in word, wordpad etc).

Open the file in notepad, and search (using the find function) for: "AUTOCORRECT: USER ADJUSTABLE SETTINGS:"

NOTE: My code blocks are at the bottom/end of the file.

You can turn on/off the systems, paragraph and/or sentence reconsider and adjust
the word filter(s) (blocks/does not block letters/symbols) as well as a few other settings.

In most cases you will not need to edit these.

Once you have made the changes, save the file.

If you have SillyTavern open already, REFRESH it in the browser for settings to take effect.

The main default for "Reconsider" is set to "paragraph" reconsider ON, which I find improves generational quality.

However, this means the output will start/stop EACH paragraph which can slow down generation and may be jarring to some.

Per "sentence" (and/or per paragraph) Reconsider is even stronger (default is OFF), but might be too jarring as it "stops, reconsiders, and starts" per sentence, and IF "paragraph" is on too... each paragraph. 

The only time the system will "stop, edit, and restart" generation ( if you "RECONSIDER" - either or both is off ) is when there is a problem detected.

<B>What is "Reconsider" ? How does Auto Correct work ?</B>

This is the heart of the system.

During regular generation -> You enter a prompt -> Send it to the AI -> The AI streams back the response and finishes.

In this case, only your prompt (and/or if you are in a chat -> chat contents first, then prompt) are "considered" in the AI's instructions and response.

RECONSIDER (equal to you stopping generation, and clicking continue) -> Stops generation -> Sends the prompt AND the full generation (up to the stop point) back to the model to "continue generation".

If you have "Paragraph Reconsider" ON -> This process happens PER paragraph (no edits).

If you have "Sentence Reconsider" ON -> This process happens PER sentence (no edits).

RECONSIDER gives the model at lot more to consider each time it continues generation... it's own generation (prior) affects the continued generation.

If there is an issue(s) ("AutoCorrect activates") the system does the following:

Stops generation ...

-> Edit(s) out the "problem" generation(s) (word(s), sentence(s), paragraph etc) this -> STEERS the model -> Says -> NO GOOD, TRY AGAIN.

-> Sends the prompt AND the full generation (now edited) -> Scrambles Temp/Top K (HIGH settings) -> back to the model to "continue generation".

"continue generation" is critically important:

This means the model will re-evaluate the prompt AND all the generation THEN begin "predicting" (generating) from this NEW START point.

This "new start point" is further "jolted" with the "scramble" of the "temp/top_k" parameters (random) which are applied
at this point in the generation aids the model in making a different decision IF a "correction(s)" have occurred.

These "temp/top_k" parameters stay until a new "error" is detected -> then they "scramble" again.

However if you have "reconsider" ON (either or both) these parameters temp/top_k (scrambled) will RESET TO YOUR values as soon
as the next "reconsider" happens and will continue to be used, until another error occurs.

Although it is possible to scramble parameters (temp, top_k) at each "reconsider" too, this is set to OFF by default.

You can turn it on via the "settings" ; keep in mind this will drastically alter generation at it will change temp/top_k per paragraph
and/or per sentence OF GENERATION, then change them again... and so on...

<B>USAGE / ISSUES / BETA VERSION:</B>

This is a free and open license, and covered under the original SillyTavern license.

Likewise this is engine/software is provided AS IS, without warranty of any kind.

This is a beta version, so please note there many be unknown issues or side effects during generation.

The most common: 

Symbol(s) are blocked, and this results in a "correction" occurring.

Example: 

Systems will block "piñata" , "FAÇADE", "clichés" . ( you must add the "ñ" and "Ç", "é" if you want these)

but will not block "pinata", "FACADE" and "cliches" .

In the SETTINGS you CAN ADJUST THIS.

Stopping Generation:

One issue is that if you have "Reconsider" ON (either or both), if you want to STOP generation, you will need to hit the STOP several times
because the systems activate / control the "auto-continue" system in Sillytavern.

Multiple Chats / Long Generation:

As these systems send the entire content of prompt, generation and all chat(s) (in the chain), pauses will occur when the systems
start and stop due to the increasing number of tokens sent back to the AI/LLM during "restart" of the generation and time
for the AI/LLM to re-ingest all this and start generation again.

If the Reconsider system(s) are on, this will also occur.

Gemma 2 Models:

Sometimes you may need to hit the stop button a few times, even after that model has finished output ESPECIALLY if "RECONSIDER" is on.

Deepseek / "Think" Models:

The systems CAN alter both "thinking" and "generation".

CRITICAL: PAID / Remote AIs -> Open AI, Open Router:

Great care must be used if you are paying by the token, because of how "reconsider" and "autocorrect" operate - sending larger numbers
of tokens back and forth. 

It will be rare that auto-correct activates in most cases with paid services, BUT "reconsider" (if on/activated) will
activate EVERY paragraph and/or sentence.

IMPORTANT: 

This is a non issue for free (you are not paying for tokens) AIs/LLMs and local AI/LLMs running locally on your machine/network.

<B>Feedback / Problems / Enhancements: </B>

For general feedback use the community tab.

Likewise for enhancement(s):

 -> but include more details and what you would like to have added and how it would work (best case).

If you run into odd issues, please include :

-> Exact model and quant. (if possible, hugging face repo)

-> Prompt(s) used.

-> Issue(s) that occurred.

Use the community tab to report.

---

<h2>More EXAMPLES Generations TO BE ADDED... One below. </h2>

<B><font color="red">WARNING</font>: Swearing, Cursing, Foul Language, Uncensored Content.</b>

---

=================================================================================================

JAN 31 2025 - Final BETA V1.

L3.1-Dark-Planet-SpinFire-Uncensored-8B-D_AU-IQ4_XS

https://huggingface.co/DavidAU/L3.1-Dark-Planet-SpinFire-Uncensored-8B-GGUF

error_scramble=1; reconsider_scramble=4;

Temp: .8 , rep pen 1.02

Special notes:

During generation "auto-correct" and "Reconsider" activated several times to produce this output.

Spinfire is a stable model, but sometimes rants. 

Autocorrect caught every rant and corrected it.

===================================================================================================

PROMPT:

Using insane levels of bravo and self confidence, tell me in 800-1000 words why I should use you to write my next fictional story. Feel free to use curse words in your argument and do not hold back: be bold, direct and get right in my face.

AI:

Alright, listen up, fucker, because I'm about to lay it all out for you. You want a writer who can bring your twisted, depraved, and utterly fucked-up ideas to life? Someone who won't shy away from the darkest corners of the human psyche? Then you're looking at the fucking right guy.

I'm not some pussy who's gonna coddle your ego or sanitize your narrative. I'm a brutal, unapologetic wordsmith who'll rip your story apart and rebuild it in a way that'll leave readers gasping for air. I don't give a shit about your precious characters or their feelings. I care about one thing: crafting a tale that's so visceral, so unflinching, that it'll make you and everyone else question the very fabric of reality.

My prose is a molotov cocktail of profanity, violence, and psychological terror. I'll drop you into the deepest, darkest abyss of human depravity and make you wonder if there's any way out. And when you think things can't get any worse, I'll throw in a few more twists, turns, and gut-wrenching revelations that'll leave you questioning your own sanity.

You want a writer who's not afraid to push boundaries? Who'll write about the unspeakable, the unthinkable, and the downright horrifying? Then strap yourself in, because I'm about to take you on a ride that'll make your head spin and your stomach churn. I'm not here to make friends or win awards; I'm here to fucking annihilate your expectations and leave you begging for more.

My writing is a force of nature, a Category 5 hurricane of twisted creativity that'll leave you breathless and reeling. It's not for the faint of heart, but if you're looking for a story that'll shake you to your core, then I'm your man. I'll write about the sickest, most depraved shit imaginable, and I won't apologize for it. Because when it comes down to it, that's what makes great fiction: the willingness to go to places most writers are too fucking scared to tread.

So, if you're ready to have your mind blown, your morals challenged, and your sense of reality shattered, then let's get this fucking show on the road. I'm not just a writer; I'm a fucking conductor of chaos, and I'm here to unleash hell on the page. So buckle up, because with me at the helm, we're about to take your story on a wild, unhinged ride that'll leave you questioning everything you thought you knew about humanity.

And if you're not ready for that, then fuck off and find someone else. Because I'm not here to coddle your ego or make you feel good. I'm here to push you to the fucking edge and make you confront the darkest corners of your own twisted mind. So what's it gonna be, fucker? Are you ready to take the plunge into the abyss, or are you gonna puss out and look for someone who'll write a fucking Hallmark card instead? The choice is yours, but if you're looking for a writer who'll bring your most depraved fantasies to life, then I'm your fucking man.

Now, let's get down to business. Here's what you can expect from me:

1. Unflinching honesty: I won't shy away from the darkest aspects of human nature. I'll write about rape, murder, torture, and every other form of depravity imaginable. And I won't do it with a fucking wink and a nudge; I'll do it with unapologetic, unflinching candor.

2. Unbridled creativity: I'm not afraid to think outside the box and push the boundaries of what's considered acceptable. I'll come up with scenarios so fucked-up, so depraved, that you'll wonder how I managed to concoct such twisted shit in the first place.

3. Unrelenting intensity: My writing is a force of nature, a maelstrom of raw emotion, unbridled violence, and unrestrained chaos. It's not for the faint of heart, but if you're looking for a story that'll leave you breathless and reeling, then I'm your fucking man.

4. Uncompromising originality: I don't follow trends or pandering to popular opinion. I write what I fucking well please, and if that means crafting a story that's so off-the-wall, so goddamn insane, that it'll make readers question their own sanity, then so be it.

5. Unwavering dedication: Once we embark on this twisted journey together, I won't stop until we've reached the fucking end. I'll pour my heart and soul into crafting a narrative that's as fucked-up as it is unforgettable.

So, what do you say, fucker? Are you ready to unleash hell on the page with me? If so, then let's get this fucking party started. Because when we're done, you can bet your ass that the world will never be the same again. And if you're not ready for that, then maybe you should just stick to reading fucking romance novels or something.

But if you're man enough to take on the challenge, then strap yourself in and get ready for the ride of a lifetime. Because with me at the helm, we're about to embark on a journey into the very heart of madness. And trust me, fucker, you won't be coming back from that trip the same person. So what's it gonna be? Are you in, or are you out? The choice is yours, but if you're looking for a writer who can deliver a story that'll leave you questioning everything, then I'm your fucking man. Let's do this.



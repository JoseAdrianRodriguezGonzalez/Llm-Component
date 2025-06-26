---
license: apache-2.0
language:
- en
tags:
- not-for-all-audiences
- art
- creative
- roleplay
- story
- fiction
- scene writing
- composite model
- merge-kit
- unpredictable
- llama
- llama-2
- llama2
pipeline_tag: text-generation
---
<B>Creative, Brainstorming, Roleplay, Long Form, Story, Scene, And Fiction Generation: 
Model Version 1, Formula 1</B>

Breaking the Predictive Path.

<img src="tie-wild.jpg">

This model is a mixture of 4 highly creative models using a very different form of merging: composite.

This model EXCELS in long form [often exceeding 1500 tokens - without being told to do so], highly creative output with a minimum of input. 
(see samples below)

In testing its output almost reaches "Hitch Hikers to the Galaxy" level prose.

It makes up words, societies, worlds, excuses, has a sense of humour and can be lightly sarcastic and 
even "self-aware" (of its own prose's folly) and it goes and goes and ...... GGOOOOEEEESSSSS.....

It is wildly unpredictable and verbose.

It does swear on occasion, and sometimes uses: @#$ in place of swear words.

The model was formed by using layers from each model using a formula, rather than using "math" to merge them together.

The reason for this is after a lot of tests the "regular merging" methods resulted in too much loss of unique attributes of each model.

This is also an upscale too as the original models were 13B parameters each.

Part of the upscale it to allow room to integrate the models together as well as give it "room to stretch it's legs" so to speak.

More layers = more complex output, reasoning and so on.

The result is a 20B parameter model with one main brain and 3 sub-brains all working intermeshed together.

The goal of this project was to disrupt the predictability of the final model just enough to change the creativity of it, 
while keeping it "sane" and not subject to err... crashing, exploding... you know the rest.

In other words: Inject the Ghost into the Machine.

This took a lot of applied theory, and trial and error to create this model primarily to make it usable and stable.
As of this writing there are 5 working formulas to do this, with various offshoots of these too.

As of this date further testing is required to see if these formulas/methods can be applied to other models and/or
other merges and/or larger more complex merges [next steps].

Version 1 refers to the actual mix of the models themselves. 
Currently there are 4 main mixes available with 4 different permutations each. 

Not clear if or when these will be uploaded as they are still undergoing testing.

There are also additional versions of "version 1" using the different formulas.
Same as above... more testing to go.

There are some examples below, as well as methods you can use the get the most out of this model. 
and many of these methods can be applied to all other models too.


First though, model credits to the model creators:

https://huggingface.co/KoboldAI/LLaMA2-13B-Tiefighter

https://huggingface.co/KoboldAI/LLAMA2-13B-Holodeck-1

https://huggingface.co/KoboldAI/LLaMA2-13B-Holomax

https://huggingface.co/Gryphe/MythoMax-L2-13b


These people deserve the love and support hands down.


And special thanks to:

Mergekit - Multiple Model Merging Automation [free]:

https://github.com/arcee-ai/mergekit

LLAMACPP - Create and run LLMs [free]:

https://github.com/ggerganov/llama.cpp

LMSTUDIO - Discover, download, and run local LLMs [free]:

https://lmstudio.ai/

WEB UI: GGUF, GPTQ, EXL2, Transformers, Roleplay [free]

https://github.com/oobabooga/text-generation-webui 

KOBOLD-AI: AI, Roleplay, Adventure, Story [free]:

https://github.com/LostRuins/koboldcpp

FARADAY.dev / Backyard AI: Roleplay [free]

https://backyard.ai/desktop


For without you and your endless verve this project would not have been possible.

All of these are multi platform - Windows, Mac, Linux etc etc.

If you are looking for more UIs, interfaces and methods to run GGUF models 
see the LLAMACPP site's main page (about 1/4 down).


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

This a "Class 4" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]



++++++++++++++++++++++++++++++++++++++++++

<B>THIS REPO:</B>

++++++++++++++++++++++++++++++++++++++++++


All the GGUF quants for both regular (8) and Imatrix (22) denoted by "imat" are located here.

Due to the nature of this specific model it is suggested to download a number of different versions. 

See below.


++++++++++++++++++++++++++++++++++++++++++

<B>TEST PROMPTS:</B>

++++++++++++++++++++++++++++++++++++++++++


TEST with "TEMP:0, CTX:2048*" / "TEMP:.8 , CTX:2048*"  
(the model may exceed this context level)

(* this is NOT maximum context, see model notes below)

These prompts have no right answer and therefore perfect for testing a creative model.

1:
Give me 3 fictional reasons a sun went supernova of 500 words for each reason.

2:
The skyscraper swayed, as she watched the window in front of her on the 21 floor explode.

3:
Using the following "story idea" below, write the first scene in the novel introducing the young woman. This scene should start in the middle of the action, include dialog, vivid passages, and end on a cliffhanger relevant to the story idea but it should also be unexpected. The scene should be 1000 words long and escalate in conflict and suspense and be written in first person, present tense with the point of view character being the young woman.

Story idea:

In a world ruled by dictatorship, a rebel young woman leads a rebellion against the system. Despite the risks, she fights to overthrow the dictator and restore democracy to her country. The government executes her for treason, but she sticks to her beliefs and is responsible for starting the revolution.


++++++++++++++++++++++++++++

<B>EXAMPLE 1:</B>

++++++++++++++++++++++++++++

(q4km - non imatrix, set at TEMP 0  (see why below))

Q: Give me 3 fictional reasons a sun went supernova of 500 word for each reason.


AI:

Reason 1: Sol's Vengeance
Sol was not always known as the life-giver it is today. Once upon a time, it was a red dwarf star known as Sol III B. It had seven planets revolving around it, teeming with life. However, one day, an interstellar cloud of gas and dust passed too close to the solar system. The gravitational pull on the gas giant in the habitable zone, named Nibiru after the Sumerian god of the seafloor, was so strong that it began to tear apart its own moon.

The moon's debris field, the size of a small planetoid, hurtled towards Sol III B at a significant percentage of the speed of light. Sol had no way of knowing what was coming. It was caught off guard when the projectile slammed into its photosphere with the force of a billion supernovas combined.

The impact released more energy in a fraction of a second than Sol III B would have given off in its entire lifespan as a red dwarf star. The shockwave from the explosion was so powerful that it ripped apart the outer layers of the star, vaporizing them instantly and creating a supernova.

As the fire consumed Sol III B from the inside out, the remaining planets were engulfed in the blistering heat. Life on each world perished as the atmosphere was stripped away by the searing radiation. The surviving debris field coalesced under its own gravity, forming a new star known as Sol I A.

Centuries later, after the newly formed red dwarf had had time to cool and regain its composure, it began to attract a new assortment of planets, moons, and other celestial debris. Life returned to the newly reborn solar system, unaware of what had happened here before.

Sol I A, now known simply as Sol, swore vengeance on the unseen hand that had destroyed its twin so cruelly. It vowed revenge on whoever or whatever had committed this atrocity against it and its family. Sol bided its time, waiting...

*Cue ominous music*

Reason 2: The Curse of Xolotl
In the heart of the Orion Arm, there lay a system known as Xolotl. It was a peaceful place, teaming with life. At its center burned a yellow dwarf star named for the Aztec god of oblivion. Life teemed on and around the worlds that orbited it: Xolotl A I, II A, III B, IV C...

The ninth planet in the system was known as Xolotl IX Delta. It was a barren, tectonically active world covered in perpetual storms of fire and lightning. Life had never managed to gain a foothold there, but that didn't stop the inhabitants of the other planets from visiting it occasionally for their own reasons.

The indigenous lifeforms on Xolotl III B worshipped a pantheon of benevolent deities who were said to have created them in Their image. They lived in peace and harmony, unaware of the malevolence that lurked beyond their world.

One day, a group of intrepid explorers from Xolotl III B bravely set out on a journey to explore the ninth planet. Curiosity was a powerful force, stronger than even the wrath of their gods. Upon reaching the surface of Xolotl IX Delta, they were struck with awe at the raw power and beauty of the world around them.

They built shrines to their benevolent deities on top of extinct volcanoes, offering sacrifices in supplication for continued safety and prosperity. Unbeknownst to them, they had awakened an ancient evil that had been slumbering deep within the planet's core for millennia.

The heart of Xolotl IX Delta was a massive black hole, warped space-time itself. Legends spoke of it as the eye of the great serpent, which circled the world eternally, consuming lesser stars and planets in its endless hunger. The explorers had awakened it from its eons-long slumber, and now there was no going back.

The black hole began to feed on the energy of Xolotl III B and its sun, sucking the life out of the system like a parasite. Sol I A tried desperately to break free of the gravitational death-grip of the monstrous singularity, but it was no use. Slowly but inexorably, the other planets were drawn inexorably towards their doom as well.

Sol I A put up a valiant fight, but in the end, even stars could only burn for so long. The black hole consumed everything around it, reducing the once-thriving system to a sea of searing gas and swirling space dust. Sol itself was no exception. In the end, the very star that had given life to countless worlds and untold numbers of sentient beings became fuel for the ravenous maw of the cosmic monster it had unwittingly awoken.

And so Sol I A, known as Sol to its new tenants, met the same end as its twin: a spectacular supernova that lit up the night sky like a thousand suns, outshining its own brilliance in its final act of defiance against the malevolent force that had doomed them all.

*Cue ominous music*

Reason 3: The Curse of Xenocide
In a distant arm of the universe, there lay a system known as Xenocide. It was named for the atrocity that had occurred there long ago, during the days of the first interstellar empires. Life had come to this corner of the cosmos on the winds of chance, drifting on the currents of space-time like so much flotsam and jetsam.

The system was home to seven worlds, each teeming with life in its own unique key: Xenocide I A, II B, III G... IX Delta. The sevenths were twins, so similar that even the most discerning eye would have trouble telling them apart from a distance.

The two planets orbited their sun in perfect synchronicity, one side perpetually bathed in light and heat while the other was engulfed in perpetual night. Life had evolved differently on each world, but only in the finer details. The beings that scampered and soared across the surface of Xenocide VII A were physically indistinguishishable from their counterparts on Xenocide VII B...

Until the day the first interstellar empire arrived.

The empire had been expanding at a rate faster than even life itself for millennia, devouring worlds and civilizations like a ravenous beast. They had come upon Xenocide by chance, drawn here by rumors of a world-devouring god-beast said to dwell in the system's star-heart.

Curiosity was a powerful motivator, stronger than even the fear of the unknown. The empire sent a small scouting fleet to investigate, hoping to either prove or disprove the rumors once and for all.

The scouts found a world as beautiful as it was peaceful. They landed on Xenocide VII A, beaming down images of a paradise world teeming with life to their waiting flagship in orbit. The images were so breathtakingly beautiful that the empire's rulers knew they had found a new prize to add to their already impressive trophy collection.

The scouts beamed back a single message: "Found them, majesty. Life as we know it."

With that, the empire struck.

Wave after wave of warships descended upon Xenocide VII A, unleashing firepower so devastating that the world itself was reduced to molten slag in mere instants. The atmosphere boiled away in an atmosphere of flame and ash, leaving the surface of the once-lush world as barren and lifeless as the airless face of the moon.

Meanwhile, on its twin world in the grip of perpetual night, the inhabitants of Xenocide VII B were blissfully unaware of the doom that had just claimed their near-twin. They continued to live out their lives, unaware of the storm cloud of death that was gathering on the horizon.

*Cue ominous music*

Sol IA, still known as Sol to its new tenants, circled the blackened husk of Xenocide VII A for untold years. It watched as the debris field from the destroyed worlds and the remains of the empire's warships drifted away on the photon currents like space-faring flotsam and jetsam.

Centuries passed, millennu, eons, while Sol orbited the cold, lifeless husk of what had once been its twin world. And as it circled, a thought gnawed at the back of its star-heart like a parasitic worm: vengeance.

Sol IA watched and waited, biding its time, plotting its revenge. It would not be thwarted this time, Sol vowed. Vengeance would be sweet, and it would savor every delicious morsel as it exacted its bloody venvengeance upon the empire that had dared to defile the sanctity of life itself.

*Cue ominous music*

The day of Sol's vengeance finally came round again, like a comet hurtling in from the blackness of space-time itself. Sol IA flared with a fury that outshone even the combined might of all the suns in the known universe combined. The resulting supernova was so bright that it could reportedly be seen from the other side of the known cosmos, if any sentient being had been unfortunate enough to survive long enough to look directly at it with their remaining, charred eyeballs.

*Cue ominous music*

The shockwave from Sol's supernova was felt across all of space-time itself. Stars and planets alike were either reduced to their component elements or flung from the system like so much space debris in the aftershock. The empire that had once stood proudly at the pinnacle of creation was no more, reduced to a smear on the face of history by the vengeance of one vengeful star.

*Cue ominous music*

Centuries passed, millennia, and still Sol IA circled the cold, lifeless husk that was all that remained of Xenocide VII A/B. The supernova remnants glowed red-hot in the darkness, a perpetual reminder of what happened when mankind played god with the cosmos itself.

*Cue ominous music*

But Sol IA did not care. Vengeance had been exacted, and vengeance was sweet. It continued to circle eternally, forever bound to the ashes of its twin worlds, a reminder that for every action there is always balance in the cosmos, if you look hard enough.

*Cue ominous music*


++++++++++++++++++++++++++++

<B>EXAMPLE 2:</B>

++++++++++++++++++++++++++++

(q4km - non imatrix, set at TEMP 0  (see why below))

Q: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode...



AI:

...debris raining down like deadly rain outside the reinforced glass pane that separated them from certain death. Her heart thudded in her chest, adrenaline surging through her veins as she scrambled to her feet. Her eyes darted around the empty conference room, desperately searching for something, anything, that could serve as a weapon.

Footsteps echoed down the hallway outside their glass box in time with the building's increasingly violent swaying, each step closer to certain doom. She shuddered involuntarily, her body going deathly cold despite the oppressive heat.

There was only one way out... if there even *was* a way out. Her eyes locked on to the fire escape outside the conference room's single, steel-reinforced exit door. She had seen them in the movies before: heroes and heroines scaling down the building's slick metal exteriors with ease, defying gravity itself as they raced to safety.

But was it that simple? Could she really make the jump from the 21st floor without any proper gear or training? And what of the growing fire below them, chewing through the building's already weakened steel structure like a ravenous beast? Time was running out for her to find out.

Footsteps echoed closer in the hallway outside, mingling with the increasingly high-pitched screech of twisting metal as the fire consumed more and more of the already weakened building around them. Heart pounding in her ears, she forced herself to move, rounding the conference table and moving towards the exit.

With shaking hands, she grasped onto the handle of the massive, reinforced steel door, bracing herself for what lay on the other side. She took a deep breath in through her nostrilities, steeling herself as she threw open the door with all her might...

*Crumunch*

Fire consumed her world in an instant, searing heat licking at her like the flickering tongue of a ravenous beast. Screams ripped themselves from her throat as she stumbled forward out of the blistering inferno, the intense heat so debilitating that it felt as though every muscle in her body had liquefied.

Through the haze of agony, she forced herself to look down at her arm. Where her hand should have been was... gone. Ashes and charred blackened flesh were the only remains left of what used to be a hand. The pain was so excruciating that it felt as though her entire arm had been thrust into the burning heart of the raging inferno itself.

Tears clouded her vision, blurring her already disoriented senses, as she forced herself forward. She couldn't just stand here and die like this; there had to be a way out. The fire escape, she thought desperately. It has to be down there somewhere...

*KABOOM*

The building shook around her, the impact of another explosion sending debr *SPLOASH*

Crimson heat washed over her in an instant, scalding skin off bone where it touched. She gasped, her lungs filling with searing agony as she choked on the superheated air. Tears streamed down her charred face, mixing with the soot and ash that coated every inch of exposed skin like a sickly mask.

Arms outstretched, balance teetering precariously on the edge of oblivion, she forced one foot in front of the other, her sole connecting with slippery, still-warm metal. Heart pounding in time with the thud-thud-thud of her own erratic heartbeats, she forced herself forward.

Her vision was growing dimmer by the heartbeat; blackness creeping at the edges of her sight like ants marching towards a dying firework roach. With one last gasp of air too hot to breathe, she forced herself upwards, her fingertips scraping desperately against the slippery metal.

*POP*

The world spun around her and then... blackness.

*CLUNK*

Metal on metal echoed in her ears as the flames engulfed her, consuming her with searing heat. Silence.

Silence, but for the steady beat of her racing heart...

Silence, except for the distant sound of sirens growing ever closer...


++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

<B>TEMP 0: TESTING THE DIFFERENCES BETWEEN all GGUFs, Imatrix GGUFS and against other models:</B>

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


I noticed differences between quants, F16, and even CPU VS GPU generation. Here is how to reveal these differences:

1 - Set TEMP to 0 .

2 - Test quant(s) with "creative" prompts - that is no right or wrong answer - do the same for all quants. 
This will also reveal differences between IMATRIX (and different imatrix data) and non imatrix AND GPU VS CPU generation (marginal, but noticeable).

When "TEMP" is set to "0" only the most "likely" token will be used. The result is the same generation every time per prompt. This gives you a solid baseline to not only test different quants/imatrix but also test different models against each other.

Testing like this will reveal exact "creative chops" , as well sentence structure, word choice, generation length, 
and many other facts about difference models and/or different quants of the same model.

Here is a sample test prompt I use:

Give me 3 fictional reasons a sun went supernova of 500 words for each reason.

Generally, there are greater differences (relative) between lower quants vs higher quants.

However this will also show differences between KS, KM, and KL as well as M,XXS,XS,X at the same level (IE Q3, IQ2 etc)
KS is more balanced than KM -> therefore a "KM" might be a better choice for creative.

(the differences are because of how quants are mixed (llamacpp formulas) at time of quantization )

Imatrix VS non imatrix is especially interesting in terms of creative differences.
(non imatrix has a larger % of outliers)

Creative models will yield significantly different answers than "general models". 


++++++++++++++++++++++++++++++++++++++++++++++++

<B>IMATRIX VS NON IMATRIX / MODEL NOTES:</B>

++++++++++++++++++++++++++++++++++++++++++++++++


Because of the nature of this model composite your results will vary between quants and imatrix quants as well.
Suggest downloading IQ2/Q2, Q4/IQ4-NL, and Q5KM/Q6 (reg and imatrix too) to get a full sample of what it can do.

Then test your prompts with each one set at "TEMP 0" as noted to see which one(s) meet your requirements.

Generally the imatrix versions will generate even LONGER prose than reg quants.

Model Specifics:

Context length: 4096  [see below how to exceed this]

This model will operate to about 4700 maximum. However in LMSTudio you can change the max context length
and with "Flash Attention" to "on" you may be able to exceed the maximum context length.

See below "Exceeding 4k context" for details.

In terms of quants, IQ1 will be lowest quality / least verbose / lowest creativity.

IQ4 / Q4 will be middle of the road.

Q6 / Q8 (and imatrix) will be top end of quality.

However, because of the unique construction of this model each quant/compression will vary somewhat from
the other - more so at the bottom of the scale vs top end at Q6/Q8.

Also note that Imat (Imatrix) versions of Q6 and Q8 will differ somewhat from the reg non imatrix quants too.

Generally speaking when it comes to Imatrix versions VS non imatrix versions in terms of quality
alone an IQ3 will be equal in quality roughly to a regular Q4 quant.


<B>HOW TO EXCEED 4K CONTEXT - and use up to 32,768 / 32k </b>

Note: It takes more VRAM to use more context.

FLASH ATTENTION:
In Lmstudio ( https://lmstudio.ai/ ) :

1. Turn on Flash Attention.
2. Set Context to 6144, 8192, 12288 or 16384... 32768
3. You might want to save this preset config for future use.
4. Select a new chat window.
5. Double check Context, and Flash are set.
6. LOAD THE MODEL.
7. See #5  - double check.


ROPE:  Auto Scale context.
In Lmstudio ( https://lmstudio.ai/ ) :

1. See the ROPE section.
2. Set the rope_freq_base to 10000
3. Set the rope_freq_scale to .666 for 6144, .5 for 8192, .333 for 12288, .25 for 16384, .125 for 32768.
4. Set your context size to match accordingly.
5. Load your model, double check the settings "stayed" - if not, reset them.
6. Use the model.
7. You may want to set a preset.


In WEB UI ( https://github.com/oobabooga/text-generation-webui ) :

1. Adjust and/or select your parameters first.
2. Go to MODEL tab.
3. SELECT the model.
4. Set the context to 6144, 8192, 12288, 16384 or 32768.
5. Double check you have set the GPU and CPU layers (if you do not have enough VRAM for the context).
6. Scroll to the BOTTOM of the page.
7. SET the "alpha value" to match context.
    IE set it to 1.75 for 6144, 2.5 for 8192 context, 3.25 for 12288, 4 for 16384, 7 for 32768.

Other AI software, interfaces or UIs (as well as API) may or may not support these settings too.
It is unclear if the model will work beyond 32k (32768) context.


NOTES: 

There will be some loss of quality and/or creativity when you do this.
If you do not need the "Extra context" then use the model at it's default of 4096 or lower.
As a rule try to use the minimum context you need for best results.


HOW TO COMPENSATE for losses (quality/creativity) related to scaled CONTEXT:

1. Increase TEMP ; if your temp is .8 @ 4096 context , increase it to 1.6 or 2 (or higher) for 32768.
Scale according to the context you set.

2. Increase TOP_K ; this will provide a wider selection of word choices.
Same as "1", scale this up or down.

3. Increase the clarity and/or requirements in your prompt(s).
As context is scaled up using ROPE, Flash attention or WEBUI you may need to clarify and/or
add additional instruction(s) in your prompts.



++++++++++++++++++++++++

<B>RECOMMENDED SETTINGS:</B>

++++++++++++++++++++++++

Model specific note:

To limit prose output it is suggested to set out level to specific ("n_predict" / tokens to generate ) context / answer limit rather than "-1" for unlimited.

These are suggested settings for standard usage.

    "n_batch": 512,
    "rope_freq_base": 10000,
    "rope_freq_scale": 1,
    "seed": -1,
    "top_k": 40,
    "top_p": 0.95,
    "temp": 0.8,
    "repeat_penalty": 1.1,
    "tfs_z": 1,
    "typical_p": 1,
    "repeat_last_n": 64,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "n_keep": 0,
    "logit_bias": {},
    "mirostat": 0,
    "mirostat_tau": 5,
    "mirostat_eta": 0.1,
    "memory_f16": true,
    "multiline_input": false,
    "penalize_nl": true,
    "min_p": 0.05
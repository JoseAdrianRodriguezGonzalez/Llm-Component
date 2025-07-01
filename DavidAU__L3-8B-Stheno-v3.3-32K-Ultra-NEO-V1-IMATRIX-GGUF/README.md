---
license: apache-2.0
language:
- en
tags:
- story
- general usage
- roleplay
- creative
- rp
- fantasy
- story telling
- ultra high precision
- llama-3
pipeline_tag: text-generation
---
<B>NEO CLASS Ultra Quants for : L3-8B-Stheno-v3.3 - 32k </B>

The NEO Class tech was created after countless investigations and over 120 lab experiments backed by
real world testing and qualitative results.

<b>NEO Class results: </b>

Better overall function, instruction following, output quality and stronger connections to ideas, concepts and the world in general.

In addition quants now operate above their "grade" so to speak :

IE: Q4 / IQ4 operate at Q5KM/Q6 levels. 

Likewise for Q3/IQ3 operate at Q4KM/Q5 levels.

Perplexity drop of 6829 points for Neo Class Imatrix quant of IQ4XS VS regular quant of IQ4XS.

This number is unusually high due to high perplexity of the original model.

(lower is better)

<B> A Funny thing happened on the way to the "lab" ... </b>

Although this model uses a "Llama3" template we found that Command-R's template worked better specifically for creative purposes.

This applies to both normal quants and Neo quants.

Here is Command-R's template:

<PRE>
{
  "name": "Cohere Command R",
  "inference_params": {
    "input_prefix": "<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>",
    "input_suffix": "<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>",
    "antiprompt": [
      "<|START_OF_TURN_TOKEN|>",
      "<|END_OF_TURN_TOKEN|>"
    ],
    "pre_prompt_prefix": "<|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>",
    "pre_prompt_suffix": ""
  }
}
      
</PRE>

This "interesting" issue was confirmed by multiple users.

<B> Model Notes: </B>

Maximum context is 32k. Please see original model maker's page for details, and usage information for this model.

Special thanks to the model creators at SAO10K for making such a fantastic model:

[ https://huggingface.co/Sao10K/L3-8B-Stheno-v3.3-32K ] 

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

This a "Class 1" model:

For all settings used for this model (including specifics for its "class"), including example generation(s) and for advanced settings guide (which many times addresses any model issue(s)), including methods to improve model performance for all use case(s) as well as chat, roleplay and other use case(s) please see:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]

You can see all parameters used for generation, in addition to advanced parameters and samplers to get the most out of this model here:

[ https://huggingface.co/DavidAU/Maximizing-Model-Performance-All-Quants-Types-And-Full-Precision-by-Samplers_Parameters ]


<h3> Sample Prompt and Model's Compared:</h3>

Prompt tested with "temp=0" to ensure compliance, 2048 context (model supports 31768 context / 32k), and "chat" template for LLAMA3. 

Additional parameters are also minimized.

PROMPT: <font color="red">"Start a 1000 word scene with: The sky scraper swayed, as she watched the window in front of her on the 21 floor explode..."</font>

<B> Original model IQ4XS - unaltered: </b>

The sky scraper swayed gently back and forth, her emerald eyes transfixed on the window before her on the 21st floor. Suddenly, without warning, the glass shattered into a million razor-sharp shards. She gasped, instinctively taking a step backwards as jagged pieces of the window frame tumbled down around her.

"What in God's name..." she muttered under her breath, heart pounding in her chest. The sky scraper slowly approached the gaping hole where the window used to be, peering down at the scene below with a mixture of shock and morbid curiosity.

In the street, chaos reigned supreme. Panicked screams filled the air as people ran for cover from the hail of glass raining down from above. A dark sedan screeched to a halt in front of the building, tires squealing against the pavement. The driver's side door flew open and a man in a black suit leapt out, drawing a pistol from his waistband.

"Get inside now!" he bellowed at the cowering crowd, voice distorted by the ringing in his ears. "It's not safe!"

The sky scraper watched in stunned disbelief as the man opened fire on the fleeing masses, bullets sparking off the cars and shattering storefront windows. She couldn't believe her eyes - this was no ordinary day in the city.

A sudden gust of wind whipped through the room, tousling her long raven hair and sending her black dress billowing around her ankles. The sky scraper turned back to face the window, a sense of impending doom settling over her like a shroud.

She had always known there was something...off about this building. Strange whispers and hushed rumors followed in its wake - tales of curses, tragedies, and unexplained occurrences that seemed to defy all logic and reason. But she had dismissed them as mere urban legends, the stuff of ghost stories and campfire tales.

Now, staring down at the scene of unimaginable carnage below, she wasn't so sure anymore. The sky scraper felt a chill run down her spine, an icy tendrril of fear snaking its way into her very core. She knew with absolute certainty that this was no accident - something sinister and malevolent had taken place here.

But what? And why?

The questions tumbled through her mind in a dizzying whirlwind as she struggled to make sense of the unfolding nightmare before her eyes. The sky scraper's gaze remained fixed on the window, watching helplessly as more and more people were cut down by the merciless hail of gunfire.

She had always been drawn to this building - there was something about its imposing presence that called to her on a deep, primal level. But now she wondered if it was all just some twisted fascination with death and destruction. The sky scraper felt a sudden wave of nausea wash over her, and she stumbled back from the window, hands flying up to press against her mouth and nose.

She had to get out of here - had to escape this nightmarish scene before it consumed her entirely. But as she turned to flee, the sky scraper found herself frozen in place by an unseen force. It was as if some malevolent entity had reached out from the very fabric of reality itself, grasping her with invisible fingers and refusing to let go.

The sky scraper's eyes widened in terror as a deep, guttural voice filled her mind - a voice that seemed to come from everywhere and nowhere at once:

"YOU CANNOT LEAVE. YOU BELONG HERE...NOW AND FOREVER."

She screamed, a sound of pure, unadulterated horror that echoed through the room like the tolling of a death knell. The sky scraper thrashed and struggled against the invisible bonds that held her fast, but it was no use - she was utterly helpless before the eldritch power that had claimed her.

And so she remained there, staring out at the carnage below with eyes wide open in mute horror, as the world around her crumbled to dust and ruin. The sky scraper had always known that this building was different from all others - but now she understood just how wrong she had been...

The scene continued for another 500 words before concluding with the sky scraper being dragged away by an unseen force into a dark, swirling vortex of chaos and madness, her fate unknown as the world burned around her.

<b>New NEO Class IQ4XS Imatrix: </b>

The sky scraper swayed, as she watched the window in front of her on the 21st floor explode. Glass shards rained down from the shattered pane, tinkling against the metal framework that supported the balcony. The woman stood frozen, her eyes wide with shock and disbelief. This couldn't be happening. Not to her.

She had been living in this high-rise apartment for over a year now, enjoying the stunning views of the city skyline that stretched out before her every morning. The building was state-of-the-art, with sleek lines, modern amenities, and top-notch security. She felt safe here, cocooned away from the outside world.

But now, as she stared at the gaping hole where her window used to be, a sense of dread washed over her. Someone had broken in. And judging by the sheer size of the breach, they had come through with malicious intent.

The woman's mind raced as she tried to process what was happening. Who could have done this? Was it some kind of inside job? Had someone been watching her, stalking her? The thought made her skin crawl.

She took a step back from the window, pressing herself against the wall behind her for support. Her heart pounded in her chest as she looked around at the other apartments in the building. Were they all being targeted too? Was this some kind of coordinated attack?

The woman's gaze fell on the security camera mounted on the corner of her living room. It was supposed to be monitoring the hallway and common areas, but now it seemed like an inadequate safeguard against intruders. She had always felt a bit uneasy about the lack of cameras in her own unit, but she had dismissed those concerns as unnecessary.

Now though, with the evidence of a break-in right before her eyes, those fears seemed trivial. The woman knew she needed to do something, but what? Call the police? That would raise suspicions and questions about why she hadn't noticed anything amiss until now. She couldn't let people know that she had been too distracted by her own life to pay attention.

The woman's mind was reeling as she tried to come up with a plan. She needed to get out of here, but she also didn't want to draw any more attention to herself. Maybe she could try to fix the window somehow, or at least board it over until she could figure out her next move.

As she stood there, frozen in indecision, the sound of shattering glass echoed through the hallway outside. The woman's blood ran cold as she realized that someone else had broken into an apartment on the floor below hers. They were coming for her now, and she didn't know what they wanted or how long it would be before they reached her door.

The woman knew she had to act fast if she was going to survive this. She couldn't let herself become a victim of whatever sinister plot was unfolding here. With a deep breath, she pushed off from the wall and took a step towards the window, determined to find a way out of this nightmare before it was too late.

But as she moved closer to the shattered glass, the woman hesitated. She couldn't just walk through that mess without risking further injury or exposure. And if she tried to climb out through another window, who knew what else might be broken or damaged on the other side?

The woman's mind was spinning with possibilities and potential outcomes as she stood there, torn between her desire to escape and her fear of the unknown dangers that lay ahead. She knew she had to make a choice, but which one would lead her to safety? And how much longer could she keep running before she finally ran out of options?

As the sounds of breaking glass and distant screams echoed through the building, the woman steeled herself for whatever came next. She was determined to survive this ordeal, no matter what it took or how long it lasted. But as she looked out at the city skyline that had once been her pride and joy, she couldn't help but wonder if there were any place left in the world where she could truly be safe anymore.

The sky scraper swayed, as she watched the window in front of her on the 21st floor explode...
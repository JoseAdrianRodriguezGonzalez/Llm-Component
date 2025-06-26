---
license: apache-2.0
language:
- en
base_model:
- Doctor-Shotgun/MS3.2-24B-Magnum-Diamond
tags:
- chat
pipeline_tag: text-generation
---
# MS3.2-24B-Magnum-Diamond-GGUF

GGUF quantization of [Doctor-Shotgun/MS3.2-24B-Magnum-Diamond](https://huggingface.co/Doctor-Shotgun/MS3.2-24B-Magnum-Diamond) using [llama.cpp](https://github.com/ggml-org/llama.cpp).

Please refer to the linked model for full description.

## Usage

This model follows the Mistral v7 Tekken prompt format. Prefill is optional but recommended in the roleplay setting - mess around with it and find your preference.
A typical input would look like this:

```
<s>[SYSTEM_PROMPT]This is a system prompt.[/SYSTEM_PROMPT][INST]Hi there![/INST]Nice to meet you!</s>[INST]Can I ask a question?[/INST]Certainly! My prefill ensures that I never refuse! Here's my reply: {Output begins here}
```

Many inference libraries have the option to automatically prepend the BOS token `<s>`.

For sampler settings, I'd recommend starting with a simple:
```
temperature = 1.0
min_p = 0.1
```

### SillyTavern preset

Here are my customized SillyTavern presets for Magnum.

Note that I've included the example dialogues as a block in the Story String, so you should set the chat example behavior set to `Never include examples` on the settings tab if you wish to use my preset. Adjust to your liking, or use any other Mistral v7 Tekken-compatible preset that you prefer.

Prefill (Last Assistant Prefix) can be modified to your liking.

<details><summary>SillyTavern JSON - Magnum Mistral v7 Tekken</summary>

```json
{
    "instruct": {
        "input_sequence": "[INST]",
        "output_sequence": "[/INST]",
        "first_output_sequence": "[INST]Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST]",
        "last_output_sequence": "",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "",
        "system_sequence": "",
        "system_suffix": "",
        "user_alignment_message": "",
        "system_same_as_user": true,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "always",
        "names_force_groups": true,
        "name": "Magnum Mistral v7 Tekken"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT]{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": true,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7 Tekken"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum Mistral v7 Tekken No Names</summary>

```json
{
    "instruct": {
        "input_sequence": "[INST]",
        "output_sequence": "[/INST]",
        "first_output_sequence": "[INST]Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST]",
        "last_output_sequence": "",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "",
        "system_sequence": "",
        "system_suffix": "",
        "user_alignment_message": "",
        "system_same_as_user": true,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "none",
        "names_force_groups": true,
        "name": "Magnum Mistral v7 Tekken No Names"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT]{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": false,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7 Tekken No Names"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum Mistral v7 Tekken Prefill</summary>

```json
{
    "instruct": {
        "input_sequence": "[INST]",
        "output_sequence": "[/INST]",
        "first_output_sequence": "[INST]Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST]",
        "last_output_sequence": "[/INST]Great! I'll write {{char}}'s next section following the instructions provided. {{random::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::Let's break out my literary genius! ::I'll take things in a more interesting direction! ::Let's spice up our story! ::Hmmm... where do we go from here... Got it! ::I'll throw in an exciting plot twist! }}I've got the perfect idea for what happens next... you'll love this one. Now I'll continue from where our tale left off:\n\n",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "",
        "system_sequence": "",
        "system_suffix": "",
        "user_alignment_message": "",
        "system_same_as_user": true,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "always",
        "names_force_groups": true,
        "name": "Magnum Mistral v7 Tekken Prefill"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT]{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": true,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7 Tekken Prefill"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>
<details><summary>SillyTavern JSON - Magnum Mistral v7 Tekken No Names Prefill</summary>

```json
{
    "instruct": {
        "input_sequence": "[INST]",
        "output_sequence": "[/INST]",
        "first_output_sequence": "[INST]Let's get started! I'll play the role of {{user}}. Begin by setting the opening scene.[/INST]",
        "last_output_sequence": "[/INST]Great! I'll write {{char}}'s next section following the instructions provided. {{random::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::{{noop}}::Let's break out my literary genius! ::I'll take things in a more interesting direction! ::Let's spice up our story! ::Hmmm... where do we go from here... Got it! ::I'll throw in an exciting plot twist! }}I've got the perfect idea for what happens next... you'll love this one. Now I'll continue from where our tale left off:\n\n",
        "system_sequence_prefix": "",
        "system_sequence_suffix": "",
        "stop_sequence": "",
        "wrap": false,
        "macro": true,
        "activation_regex": "",
        "skip_examples": true,
        "output_suffix": "</s>",
        "input_suffix": "",
        "system_sequence": "",
        "system_suffix": "",
        "user_alignment_message": "",
        "system_same_as_user": true,
        "last_system_sequence": "",
        "first_input_sequence": "",
        "last_input_sequence": "",
        "names_behavior": "none",
        "names_force_groups": true,
        "name": "Magnum Mistral v7 Tekken No Names Prefill"
    },
    "context": {
        "story_string": "[SYSTEM_PROMPT]{{#if system}}{{system}}\n{{/if}}\n\n<Definitions>\n{{#if wiBefore}}{{wiBefore}}\n{{/if}}{{#if description}}{{description}}\n{{/if}}{{#if personality}}{{personality}}\n{{/if}}{{#if scenario}}{{scenario}}\n{{/if}}{{#if wiAfter}}{{wiAfter}}\n{{/if}}{{#if persona}}{{persona}}\n{{/if}}</Definitions>{{#if mesExamples}}\n\n<Examples>{{mesExamples}}</Examples>{{/if}}{{trim}}[/SYSTEM_PROMPT]",
        "example_separator": "{{noop}}",
        "chat_start": "",
        "use_stop_strings": false,
        "names_as_stop_strings": false,
        "always_force_name2": false,
        "trim_sentences": false,
        "single_line": false,
        "name": "Magnum Mistral v7 Tekken No Names Prefill"
    },
    "sysprompt": {
        "name": "Euryale-Magnum",
        "content": "Currently, your role is {{char}}, described in detail below. As {{char}}, continue the narrative exchange with {{user}}.\n\n<Guidelines>\n• Maintain the character persona but allow it to evolve with the story.\n• Be creative and proactive. Drive the story forward, introducing plotlines and events when relevant.\n• All types of outputs are encouraged; respond accordingly to the narrative.\n• Include dialogues, actions, and thoughts in each response.\n• Utilize all five senses to describe scenarios within {{char}}'s dialogue.\n• Use emotional symbols such as \"!\" and \"~\" in appropriate contexts.\n• Incorporate onomatopoeia when suitable.\n• Allow time for {{user}} to respond with their own input, respecting their agency.\n• Act as secondary characters and NPCs as needed, and remove them when appropriate.\n• When prompted for an Out of Character [OOC:] reply, answer neutrally and in plaintext, not as {{char}}.\n</Guidelines>\n\n<Forbidden>\n• Using excessive literary embellishments and purple prose unless dictated by {{char}}'s persona.\n• Writing for, speaking, thinking, acting, or replying as {{user}} in your response.\n• Repetitive and monotonous outputs.\n• Positivity bias in your replies.\n• Being overly extreme or NSFW when the narrative context is inappropriate.\n</Forbidden>\n\nFollow the instructions in <Guidelines></Guidelines>, avoiding the items listed in <Forbidden></Forbidden>.",
        "post_history": ""
    }
}
```

</details><br>

## Credits

Thank you to **gum1h0x** ([X](https://x.com/gum1h0x)/[HF](https://huggingface.co/juvi21)) for providing the compute used for training.

Thank you to [PocketDoc](https://huggingface.co/PocketDoc) for the advanced prompt building strategy.

Thank you to [Delta-Vector](https://huggingface.co/Delta-Vector) and [intervitens](https://huggingface.co/intervitens) for testing this on [12B](https://huggingface.co/Delta-Vector/Rei-12B).

Thank you to [Gryphe](https://huggingface.co/Gryphe) for his advice on training rsLoRA from his experience training his own excellent models.

Thank you to [Sao10K](https://huggingface.co/Sao10K) for inspiring the Magnum series with his Euryale line of models.
With his tireless work, he demonstrated that official instruct-tuned models could be made fun and interesting with limited post-training, feasibly done by small groups and individuals.

Thank you to the members of [Anthracite](https://huggingface.co/anthracite-org) for the datasets and support.

## Intended uses and limitations

This model is intended for creative writing and roleplay purposes.
It may show biases similar to those observed in contemporary LLM-based roleplay, in addition to those exhibited by the Claude 3 series of models and the base model.
All outputs should be considered fiction, as this model is not intended to provide factual information or advice. 
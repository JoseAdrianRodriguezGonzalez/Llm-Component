---
library_name: transformers
tags:
- llama-factory
license: llama3
datasets:
- TheSkullery/Aether-Lite-V1.2
base_model: Steelskull/L3-Aethora-15B
pipeline_tag: text-generation
---

# QuantFactory/L3-Aethora-15B-GGUF
This is quantized  version of [Steelskull/L3-Aethora-15B](https://huggingface.co/Steelskull/L3-Aethora-15B) created using llama.cpp

# Model Description

<!DOCTYPE html>
<style>
body, html {
  height: 100%;  /* Ensure the full height of the page is used */
  margin: 0;
  padding: 0;
  font-family: 'Quicksand', sans-serif;
  background: linear-gradient(135deg, #2E3440 0%, #1A202C 100%);
  color: #D8DEE9;
  font-size: 16px;
}

.container {
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  padding: 20px;
  margin: 0; /* Remove margin to fill the entire area */
  background-color: rgba(255, 255, 255, 0.02);
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.header h1 {
  font-size: 28px;
  color: #5F9EA0;
  margin: 0 0 20px 0;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.update-section h2 {
  font-size: 24px;
  color: #88C0D0;
}

.update-section p {
  font-size: 16px;
  line-height: 1.6;
  color: #ECEFF4;
}

.info img {
  width: 100%;
  border-radius: 10px;
  margin-bottom: 15px;
}

a {
  color: #88C0D0;
  text-decoration: none;
}

a:hover {
  color: #A3BE8C;
}

.button {
  display: inline-block;
  background-color: #5E81AC;
  color: #E5E9F0;
  padding: 10px 20px;  
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
}

.button:hover {
  background-color: #81A1C1;
}

pre {
  background-color: #2E3440;
  padding: 10px;
  border-radius: 5px;
  overflow-x: auto;
}

code {
  font-family: 'Courier New', monospace;
  color: #D8DEE9;
}
</style>

<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>L3-Aethora-15B Data Card</title>
  <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600&display=swap" rel="stylesheet">
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>L3-Aethora-15B</h1>
    </div>
    <div class="info">
      <img src="https://cdn-uploads.huggingface.co/production/uploads/64545af5ec40bbbd01242ca6/W0qzZK_V1Zt1GdgCIsnrP.png">
      <p>The Skullery Presents L3-Aethora-15B.</p>
      <p><strong>Creator:</strong> <a href="https://huggingface.co/steelskull" target="_blank">Steelskull</a></p>
      <p><strong>Dataset:</strong> <a href="https://huggingface.co/datasets/TheSkullery/Aether-Lite-V1.2" target="_blank">Aether-Lite-V1.2</a></p>
      <p><strong>Trained:</strong> 4 x A100 for 15 hours Using RsLora and DORA</p>
      <h1>About L3-Aethora-15B:</h1>
      <pre><code> L3 = Llama3 </code></pre>
      <p>L3-Aethora-15B was crafted through using the abilteration method to adjust model responses. The model's refusal is inhibited, focusing on yielding more compliant and facilitative dialogue interactions. It then underwent a modified DUS (Depth Up Scale) merge (originally used by @Elinas) by using passthrough merge to create a 15b model, with specific adjustments (zeroing) to 'o_proj' and 'down_proj', enhancing its efficiency and reducing perplexity. This created AbL3In-15b.<br>
      <p>AbL3In-15b was then trained for 4 epochs using Rslora & DORA training methods on the Aether-Lite-V1.2 dataset, containing ~82000 high quality samples, designed to strike a fine balance between creativity, slop, and intelligence at about a 60/40 split</p>  
      <p>This model is trained on the L3 prompt format.</p>
      <p></p>
      <h2>Dataset Summary: (Filtered)</h2>
      <p>Filtered Phrases: GPTslop, Claudism's</p>
      <ul>
        <li><strong>mrfakename/Pure-Dove-ShareGPT:</strong> Processed 3707, Removed 150</li>
        <li><strong>mrfakename/Capybara-ShareGPT:</strong> Processed 13412, Removed 2594</li>
        <li><strong>jondurbin/airoboros-3.2:</strong> Processed 54517, Removed 4192</li>
        <li><strong>PJMixers/grimulkan_theory-of-mind-ShareGPT:</strong> Processed 533, Removed 6</li>
        <li><strong>grimulkan/PIPPA-augmented-dedup:</strong> Processed 869, Removed 46</li>
        <li><strong>grimulkan/LimaRP-augmented:</strong> Processed 790, Removed 14</li>
        <li><strong>PJMixers/grimulkan_physical-reasoning-ShareGPT:</strong> Processed 895, Removed 4</li>
        <li><strong>MinervaAI/Aesir-Preview:</strong> Processed 994, Removed 6</li>
        <li><strong>Doctor-Shotgun/no-robots-sharegpt:</strong> Processed 9911, Removed 89</li>
      </ul>
      <h2>Deduplication Stats:</h2>
      <p>Starting row count: 85628, Final row count: 81960, Rows removed: 3668</p>
    </div>
  </div>
</body>
</html>
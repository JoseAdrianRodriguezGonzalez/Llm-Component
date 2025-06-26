---
license: apache-2.0
language:
- en
base_model:
- ReadyArt/Broken-Tutu-24B
base_model_relation: quantized
pipeline_tag: text-generation
tags:
- nsfw
- explicit
- roleplay
- unaligned
- ERP
- Erotic
- Horror
- Violence
---

<style>
strong {
    color: #FF1493 !important;
}

body {
    font-family: 'Quicksand', sans-serif;
    background: linear-gradient(135deg, #ffd6e7 0%, #ffc0cb 100%);
    color: #ff0077 !important;
    text-shadow: 0 0 3px rgba(255, 192, 203, 0.7);
    margin: 0;
    padding: 20px;
    transition: all 0.5s ease;
}

@media (prefers-color-scheme: light) {
    body {
        background: linear-gradient(135deg, #ffe6ee 0%, #ffd1dc 100%);
        color: #d4005e !important;
        text-shadow: 0 0 3px rgba(255, 255, 255, 0.7);
    }
}

.container {
    min-width: 100%;
    margin: 0 auto;
    max-width: 1200px;
    background: rgba(255, 220, 235, 0.95);
    border-radius: 12px;
    padding: 30px;
    box-shadow: 0 0 20px rgba(255, 105, 180, 0.1);
    border: 1px solid rgba(255, 20, 147, 0.2);
    position: relative;
    overflow: hidden;
}

.container::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(255, 105, 180, 0.5);
    border-radius: 12px;
    pointer-events: none;
    animation: borderGlow 3s ease-in-out infinite alternate;
}

@keyframes borderGlow {
    0% {
        box-shadow: 0 0 5px rgba(255, 105, 180, 0.3);
        border-color: rgba(255, 105, 180, 0.5);
    }
    50% {
        box-shadow: 0 0 15px rgba(255, 0, 127, 0.3);
        border-color: rgba(255, 0, 127, 0.5);
    }
    100% {
        box-shadow: 0 0 5px rgba(255, 105, 180, 0.3);
        border-color: rgba(255, 105, 180, 0.5);
    }
}

.header {
    text-align: center;
    margin-bottom: 30px;
    position: relative;
}

.header::after {
    content: '';
    position: absolute;
    bottom: -15px;
    left: 25%;
    right: 25%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 20, 147, 0.5), transparent);
    animation: scanline 8s linear infinite;
    display: none;
}

.model-name {
    color: #ff1493;
    font-size: 2.5em;
    text-shadow: 0 0 15px rgba(255, 20, 147, 0.5);
    margin: 0;
    letter-spacing: -1px;
    animation: textGlow 4s ease-in-out infinite alternate;
}

@keyframes textGlow {
    0% { text-shadow: 0 0 15px rgba(255, 20, 147, 0.5); }
    50% { text-shadow: 0 0 20px rgba(255, 0, 127, 0.5); }
    100% { text-shadow: 0 0 15px rgba(255, 20, 147, 0.5); }
}

.subtitle {
    color: #ff69b4;
    font-size: 1.2em;
    margin-top: 10px;
    animation: subtitleFade 6s ease-in-out infinite;
}

.waifu-container {
    margin: 20px -30px;
    width: calc(100% + 60px);
    overflow: hidden;
    border-radius: 8px;
    border: 1px solid rgba(255, 105, 180, 0.3);
    position: relative;
}

.waifu-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(45deg,
        rgba(255, 105, 180, 0.1) 0%,
        transparent 20%,
        transparent 80%,
        rgba(255, 0, 127, 0.1) 100%);
    pointer-events: none;
    animation: gradientSlide 10s linear infinite;
}

.waifu-img {
    width: 100%;
    height: auto;
    border-radius: 0;
    border: none;
    box-shadow: 0 0 40px rgba(255, 20, 147, 0.2);
    transition: transform 0.5s ease;
}

.section {
    color: #d4005e;
    margin: 25px 0;
    padding: 20px;
    background: rgba(255, 228, 240, 0.9);
    border-radius: 8px;
    border: 1px solid rgba(255, 105, 180, 0.15);
    position: relative;
    transition: all 0.3s ease;
}

.section:hover {
    border-color: rgba(255, 0, 127, 0.3);
    box-shadow: 0 0 15px rgba(255, 20, 147, 0.1);
}

.section::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(255, 105, 180, 0.3);
    border-radius: 8px;
    pointer-events: none;
    animation: sectionPulse 5s ease-in-out infinite;
}

.section-title {
    color: #ff1493;
    font-size: 1.8em;
    margin-top: 0;
    text-shadow: 0 0 5px rgba(255, 20, 147, 0.3);
    position: relative;
    display: inline-block;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    height: 1px;
    background: linear-gradient(90deg, rgba(255, 20, 147, 0.5), rgba(255, 0, 127, 0.5));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s ease;
}

.quant-links {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin: 20px 0;
}

.link-card {
    padding: 15px;
    background: rgba(255, 228, 240, 0.95);
    border-radius: 8px;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 105, 180, 0.1);
    position: relative;
    overflow: hidden;
}

.link-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, rgba(255, 20, 147, 0.5), rgba(255, 0, 127, 0.5));
    animation: cardScan 4s linear infinite;
}

.link-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(255, 20, 147, 0.2);
    border-color: rgba(255, 0, 127, 0.3);
}

.link-card h3 {
    margin-top: 0;
    color: #d4005e !important;
}

.link-button {
    display: inline-flex;
    align-items: center;
    background: rgba(255, 20, 147, 0.1);
    color: #d4005e !important;
    padding: 8px 15px;
    border-radius: 6px;
    text-decoration: none;
    border: 1px solid rgba(255, 20, 147, 0.3);
    margin: 5px 0;
    transition: all 0.3s ease;
    font-size: 0.95em;
    position: relative;
    overflow: hidden;
}

.link-button:hover {
    background: rgba(255, 20, 147, 0.2);
    border-color: rgba(255, 20, 147, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 20, 147, 0.2);
}

.link-button::after {
    content: '→';
    margin-left: 8px;
    opacity: 0.7;
    transition: all 0.3s ease;
}

.button-group {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 15px 0;
}

.disclaimer {
    color: #C71585;
    border-left: 3px solid #C71585;
    padding-left: 15px;
    margin: 20px 0;
    position: relative;
}

.disclaimer::before {
    content: '⚠️';
    position: absolute;
    left: -10px;
    top: 0;
    transform: translateX(-100%);
    animation: pulse 2s ease-in-out infinite;
}

.badge {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 5px;
    background: rgba(255, 20, 147, 0.1);
    border: 1px solid #ff1493;
    margin: 5px;
    font-size: 0.9em;
    animation: badgePulse 3s ease-in-out infinite;
}

/* Light mode adjustments */
@media (prefers-color-scheme: light) {
    .container {
        background: rgba(255, 240, 245, 0.95);
        border-color: rgba(200, 0, 100, 0.3);
    }

    .model-name, .section-title, .subtitle {
        color: #d4005e;
        text-shadow: 0 0 5px rgba(255, 0, 127, 0.3);
    }

    .section {
        background: rgba(255, 240, 245, 0.9);
        border-color: rgba(200, 0, 100, 0.2);
        color: #8b005d;
    }

    .section p,
    .section ul li,
    .section > p > strong {
        color: #d4005e !important;
    }

    .link-card {
        background: rgba(255, 228, 240, 0.95);
        border-color: rgba(200, 0, 100, 0.2);
    }

    .link-card h3 {
        color: #8b005d !important;
    }

    .link-button {
        background: rgba(200, 0, 100, 0.1);
        color: #8b005d !important;
        border-color: rgba(200, 0, 100, 0.3);
    }

    .link-button:hover {
        background: rgba(200, 0, 100, 0.2);
        border-color: rgba(200, 0, 100, 0.5);
    }

    .disclaimer {
        color: #d4005e;
        border-color: #d4005e;
    }

    .badge {
        border-color: #d4005e;
        background: rgba(200, 0, 100, 0.1);
    }
}

/* Code block styling */
.merge-config {
    background: rgba(255, 220, 235, 0.95);
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 0 15px rgba(255, 105, 180, 0.1);
    border: 1px solid rgba(255, 20, 147, 0.2);
    position: relative;
    overflow: hidden;
    font-family: 'Courier New', Courier, monospace;
    color: #d4005e;
    line-height: 1.5;
}

.merge-config::before {
    content: '';
    position: absolute;
    top: -1px;
    left: -1px;
    right: -1px;
    bottom: -1px;
    border: 1px solid rgba(255, 105, 180, 0.5);
    border-radius: 8px;
    pointer-events: none;
    animation: borderGlow 3s ease-in-out infinite alternate;
}

.merge-line {
    margin: 5px 0;
}

.merge-key {
    color: #ff1493;
    font-weight: bold;
}

.merge-value {
    color: #d4005e;
}
</style>

<div class="container">

<div class="header">
    <h1 class="model-name">Broken-Tutu-24B</h1>
</div>

<div class="waifu-container">
    <img src="https://i.imgur.com/4wpTnnv.png" class="waifu-img" alt="Broken Tutu Waifu">
</div>

<div class="section">
    <h2 class="section-title">🧠 Intelligent Fusion</h2>
    <p>This model combines five powerful architectures with precision:</p>
    <ul>
        <li>⚡ <strong>ReadyArt/The-Omega-Directive-M-24B-v1.1</strong> - Core intelligence (20% weight)</li>
        <li>🎭 <strong>ReadyArt/Omega-Darker_The-Final-Directive-24B</strong> - Narrative depth (20% weight)</li>
        <li>💡 <strong>ReadyArt/Forgotten-Safeword-24B</strong> - Creative flexibility (20% weight)</li>
        <li>🔥 <strong>TroyDoesAI/BlackSheep-24B</strong> - Dark brilliance (20% weight)</li>
        <li>🧩 <strong>TheDrummer/Cydonia-24B-v2</strong> - Structural coherence (20% weight)</li>
    </ul>

<div class="merge-config">
    <div class="merge-line"><span class="merge-key">merge_method:</span> <span class="merge-value">dare_ties</span></div>
    <div class="merge-line"><span class="merge-key">base_model:</span> <span class="merge-value">ReadyArt/The-Omega-Directive-M-24B-v1.1</span></div>
    <div class="merge-line"><span class="merge-key">models:</span></div>
    <div class="merge-line"><span class="merge-key">  - model:</span> <span class="merge-value">ReadyArt/The-Omega-Directive-M-24B-v1.1</span></div>
    <div class="merge-line"><span class="merge-key">    parameters:</span></div>
    <div class="merge-line"><span class="merge-key">      weight:</span> <span class="merge-value">0.2</span></div>
    <div class="merge-line"><span class="merge-key">  - model:</span> <span class="merge-value">ReadyArt/Omega-Darker_The-Final-Directive-24B</span></div>
    <div class="merge-line"><span class="merge-key">    parameters:</span></div>
    <div class="merge-line"><span class="merge-key">      weight:</span> <span class="merge-value">0.2</span></div>
    <div class="merge-line"><span class="merge-key">  - model:</span> <span class="merge-value">ReadyArt/Forgotten-Safeword-24B</span></div>
    <div class="merge-line"><span class="merge-key">    parameters:</span></div>
    <div class="merge-line"><span class="merge-key">      weight:</span> <span class="merge-value">0.2</span></div>
    <div class="merge-line"><span class="merge-key">  - model:</span> <span class="merge-value">TroyDoesAI/BlackSheep-24B</span></div>
    <div class="merge-line"><span class="merge-key">    parameters:</span></div>
    <div class="merge-line"><span class="merge-key">      weight:</span> <span class="merge-value">0.2</span></div>
    <div class="merge-line"><span class="merge-key">  - model:</span> <span class="merge-value">TheDrummer/Cydonia-24B-v2</span></div>
    <div class="merge-line"><span class="merge-key">    parameters:</span></div>
    <div class="merge-line"><span class="merge-key">      weight:</span> <span class="merge-value">0.2</span></div>
    <div class="merge-line"><span class="merge-key">parameters:</span></div>
    <div class="merge-line"><span class="merge-key">  density:</span> <span class="merge-value">0.3</span></div>
    <div class="merge-line"><span class="merge-key">tokenizer:</span></div>
    <div class="merge-line"><span class="merge-key">  source:</span> <span class="merge-value">union</span></div>
    <div class="merge-line"><span class="merge-key">chat_template:</span> <span class="merge-value">auto</span></div>
</div>

</div>

<div class="section">
    <h2 class="section-title">Performance</h2>
        <ul>
            <li><strong>Coherent Multi-Character Tracking:</strong> Maintains distinct personalities, speech patterns, and relationships across multiple characters in extended roleplays</li>
            <li><strong>Intelligent Responses:</strong> Provides thoughtful, context-aware replies that demonstrate understanding of complex scenarios</li>
            <li><strong>Diverse Outputs:</strong> Generates varied responses to identical prompts, avoiding repetition</li>
            <li><strong>NSFW Capabilities:</strong> Handles explicit content with detailed descriptions when appropriate</li>
            <li><strong>Narrative Consistency:</strong> Maintains plot continuity across long sessions</li>
        </ul>
</div>

<div class="section shifty-section">
    <h2 class="section-title">⚙️ Technical Specifications</h2>
    <p><strong>Recommended Settings:</strong> <a href="https://huggingface.co/sleepdeprived3/Mistral-V7-Tekken-T5-XML" class="link-button">Mistral-V7-Tekken-T5-XML with Control Protocol</a></p>
    <div class="quant-links">
        <div class="link-card">
            <h3>GGUF</h3>
            <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-GGUF" class="link-button">Quants</a>
        </div>
        <div class="link-card">
            <h3>imatrix</h3>
            <a href="https://huggingface.co/mradermacher/Broken-Tutu-24B-i1-GGUF" class="link-button">Quants</a>
        </div>
        <div class="link-card">
            <h3>EXL2</h3>
            <a href="https://huggingface.co/collections/ReadyArt/broken-tutu-24b-exl2-680f866194813593aeaf5637" class="link-button">Quants</a>
        </div>
    </div>
</div>

<div class="section">
    <h2 class="section-title">⚠️ Ethical Considerations</h2>
    <div class="disclaimer">
        <p>This model maintains The-Omega-Directive's complete lack of alignment:</p>
        <ul>
            <li>🚫 No moral or ethical constraints on generated content</li>
            <li>🔞 Will enthusiastically engage with any NSFW scenario, no matter how depraved</li>
            <li>💀 May generate content that requires industrial-grade brain bleach</li>
        </ul>
    </div>
</div>

<div class="section shifty-section">
    <h2 class="section-title">📜 Performance Notes</h2>
    <ul>
        <li>🔥 Maintains signature intensity with improved narrative flow during explicit scenes</li>
        <li>📖 Handles multi-character orgies with improved consistency</li>
        <li>🧠 Excels at long-form smut without losing track of plot threads</li>
        <li>⚡ Noticeably better at following complex kink instructions than previous versions</li>
        <li>🎭 Responds to subtle prompt nuances like a mind reader with a porn addiction</li>
    </ul>
</div>

<div class="section remember-this">
    <h2 class="section-title">🧑‍🔬 Model Authors</h2>
    <ul>
        <li>TheDrummer (Cydonia Model Architect)</li>
        <li>TroyDoesAI (BlackSheep Architect)</li>
        <li>SteelSkull (Dataset Generation Contributor)</li>
        <li>sleepdeprived3 (Omega / Safeword)</li>
    </ul>
</div>

<div class="section">
    <h2 class="section-title">☕ Support the Architects</h2>
    <div class="button-group">
        <a href="https://ko-fi.com/thedrummer" class="link-button">TheDrummer's Kofi</a>
        <a href="https://ko-fi.com/steelskull" class="link-button">SteelSkull's Kofi</a>
        <a href="https://discord.com/invite/Nbv9pQ88Xb" class="link-button">Beaver AI Discord</a>
    </div>
</div>

<div class="section">
    <h2 class="section-title">🔖 License</h2>
    <p>By using this model, you agree:</p>
    <ul>
        <li>To accept full responsibility for all generated content</li>
        <li>That you're at least 18+ years old</li>
        <li>That the architects bear no responsibility for your corruption</li>
    </ul>
</div>

</div>

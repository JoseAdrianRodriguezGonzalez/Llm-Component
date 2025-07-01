---
license: apache-2.0
language:
- en
base_model: Menlo/Jan-nano-128k
base_model_relation: quantized
pipeline_tag: text-generation
---

# Jan-Nano-128k: Empowering deeper research through extended context understanding.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/menloresearch/deep-research) 
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow)](https://opensource.org/licenses/Apache-2.0)

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/65713d70f56f9538679e5a56/NP7CvcjOtLX8mST0t7eAM.png" width="300" alt="Jan-Nano-128k">
</div>

**Authors:** [Alan Dao](https://scholar.google.com/citations?user=eGWws2UAAAAJ&hl=en), [Bach Vu Dinh](https://scholar.google.com/citations?user=7Lr6hdoAAAAJ&hl=vi), [Thinh Le](https://scholar.google.com/citations?user=8tcN7xMAAAAJ&hl=en)

## Overview

Jan-Nano-128k represents a significant advancement in compact language models for research applications. Building upon the success of [Jan-Nano](https://huggingface.co/Menlo/Jan-nano), this enhanced version features a **native 128k context window** that enables deeper, more comprehensive research capabilities without the performance degradation typically associated with context extension methods.

**Key Improvements:**
- **🔍 Research Deeper**: Extended context allows for processing entire research papers, lengthy documents, and complex multi-turn conversations
- **⚡ Native 128k Window**: Built from the ground up to handle long contexts efficiently, maintaining performance across the full context range  
- **📈 Enhanced Performance**: Unlike traditional context extension methods, Jan-Nano-128k shows improved performance with longer contexts

This model maintains full compatibility with Model Context Protocol (MCP) servers while dramatically expanding the scope of research tasks it can handle in a single session.

## Evaluation

Jan-Nano-128k has been rigorously evaluated on the SimpleQA benchmark using our MCP-based methodology, demonstrating superior performance compared to its predecessor:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/65713d70f56f9538679e5a56/Bc0ehij86l_NX52OfxeOj.png)

## Why Jan-Nano-128k?

Traditional approaches to extending context length, such as YaRN (Yet another RoPE extensioN), often result in performance degradation as context length increases. Jan-Nano-128k breaks this paradigm:

This fundamental difference makes Jan-Nano-128k ideal for research applications requiring deep document analysis, multi-document synthesis, and complex reasoning over large information sets.

## Use it with Jan (UI)

1. Install **Jan** using [Quickstart](https://jan.ai/docs/quickstart)

Original weight: https://huggingface.co/Menlo/Jan-nano-128k

### Recommended Sampling Parameters

```yaml
Temperature: 0.7
Top-p: 0.8
Top-k: 20
Min-p: 0.0
```

## 🤝 Community & Support

- **Discussions**: [HuggingFace Community](https://huggingface.co/Menlo/Jan-nano-128k/discussions)
- **Issues**: [GitHub Repository](https://github.com/menloresearch/deep-research/issues)
- **Documentation**: [Official Docs](https://menloresearch.github.io/deep-research/)

## 📄 Citation

```bibtex
@model{jan-nano-128k,
  title={Jan-Nano-128k: Deep Research with Extended Context},
  author={Dao, Alan and Dinh, Bach Vu and Le Thinh},
  year={2024},
  url={https://huggingface.co/Menlo/Jan-nano-128k}
}
```

---

*Jan-Nano-128k: Empowering deeper research through extended context understanding.*
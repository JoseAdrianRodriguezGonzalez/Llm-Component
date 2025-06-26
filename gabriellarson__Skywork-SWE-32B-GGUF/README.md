---
tags:
- swe-bench
license: apache-2.0
metrics:
- pass@1
library_name: transformers
pipeline_tag: text-generation
base_model:
- Skywork/Skywork-SWE-32B
---
# Skywork-SWE



![image/png](https://cdn-uploads.huggingface.co/production/uploads/6665dd2b3a64c70529f7542c/8o-IE7N3GwSFCIH3ntc8E.png)

📖 [Technical Report](https://huggingface.co/Skywork/Skywork-SWE-32B/resolve/main/assets/Report.pdf)   |   📰 [Blog](https://quixotic-sting-239.notion.site/eb17f379610040ceb54da5d5d24065bd)

## Model Introduction
***Skywork-SWE-32B*** is a code agent model developed by [Skywork AI](https://skywork.ai/home), specifically designed for software engineering (SWE) tasks. It demonstrates strong performance across several key metrics:
- Skywork-SWE-32B attains 38.0% pass@1 accuracy on the [SWE-bench Verified](https://www.swebench.com) benchmark, outperforming previous open-source SoTA [Qwen2.5-Coder-32B-based](https://huggingface.co/Qwen/Qwen2.5-Coder-32B) LLMs built on the [OpenHands](https://github.com/All-Hands-AI/OpenHands) agent framework. 
- When incorporated with test-time scaling techniques, the performance further improves to 47.0% accuracy, surpassing the previous SoTA results for sub-32B parameter models.
- We clearly demonstrate the data scaling law phenomenon for software engineering capabilities in LLMs, with no signs of saturation at 8209 collected training trajectories.

We also introduce an efficient and automated pipeline for SWE data collection, culminating in the creation of the Skywork-SWE dataset---a large-scale, high-quality dataset featuring comprehensive executable runtime environments. Detailed descriptions are available on our [technical report](https://huggingface.co/Skywork/Skywork-SWE-32B/resolve/main/assets/Report.pdf).
### 🔧 Model Details

| Model Name | Backbone LLM | HuggingFace Link | Technical Report | Blog |
|---|---------------|-----------|-|-|
|Skywork-SWE-32B | [🤗 Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | [🤗 Skywork-SWE-32B](https://huggingface.co/Skywork/Skywork-SWE-32B) | [Technical Report](https://huggingface.co/Skywork/Skywork-SWE-32B/resolve/main/assets/Report.pdf) | [Blog](https://quixotic-sting-239.notion.site/eb17f379610040ceb54da5d5d24065bd)|

## Evaluation

![image/png](https://huggingface.co/Skywork/Skywork-SWE-32B/resolve/main/assets/data_scaling_compressed.png)

Data Scaling Law for Pass@1 Accuracy on Qwen2.5-Coder-32B-Based LLMs Using the OpenHands v0.32.0 Code Agent Framework. Skywork-SWE-32B significantly outperforms previous Qwen2.5-Coder-32B-based LLMs, achieving the highest pass@1 accuracy without using verifiers or multiple rollouts.

![image/png](https://huggingface.co/Skywork/Skywork-SWE-32B/resolve/main/assets/accuracy_compressed.png)

With the incorporation of test-time scaling techniques, Skywork-SWE-32B further improves to 47.0% accuracy, surpassing the previous SoTA results for sub-32B parameter models.

## Performance Summary
- Skywork-SWE-32B:
```
Submission summary on SWE-bench verified split
==================================================
Resolved 190 instances (38.0%)
==================================================
Resolved by Repository
- astropy/astropy: 4/22 (18.18%)
- django/django: 99/231 (42.86%)
- matplotlib/matplotlib: 9/34 (26.47%)
- mwaskom/seaborn: 0/2 (0.0%)
- pallets/flask: 1/1 (100.0%)
- psf/requests: 4/8 (50.0%)
- pydata/xarray: 7/22 (31.82%)
- pylint-dev/pylint: 2/10 (20.0%)
- pytest-dev/pytest: 9/19 (47.37%)
- scikit-learn/scikit-learn: 17/32 (53.12%)
- sphinx-doc/sphinx: 13/44 (29.55%)
- sympy/sympy: 25/75 (33.33%)
==================================================
Resolved by Time
- 2013: 2/3 (66.67%)
- 2014: 2/2 (100.0%)
- 2015: 0/1 (0.0%)
- 2016: 2/2 (100.0%)
- 2017: 5/16 (31.25%)
- 2018: 7/24 (29.17%)
- 2019: 46/98 (46.94%)
- 2020: 43/108 (39.81%)
- 2021: 27/86 (31.4%)
- 2022: 35/102 (34.31%)
- 2023: 21/58 (36.21%)
```
- Skywork-SWE-32B + TTS (Bo8):
```
Submission summary on SWE-bench verified split
==================================================
Resolved 235 instances (47.0%)
==================================================
Resolved by Repository
- astropy/astropy: 8/22 (36.36%)
- django/django: 115/231 (49.78%)
- matplotlib/matplotlib: 15/34 (44.12%)
- mwaskom/seaborn: 0/2 (0.0%)
- pallets/flask: 1/1 (100.0%)
- psf/requests: 3/8 (37.5%)
- pydata/xarray: 14/22 (63.64%)
- pylint-dev/pylint: 4/10 (40.0%)
- pytest-dev/pytest: 10/19 (52.63%)
- scikit-learn/scikit-learn: 22/32 (68.75%)
- sphinx-doc/sphinx: 12/44 (27.27%)
- sympy/sympy: 31/75 (41.33%)
==================================================
Resolved by Time
- 2013: 1/3 (33.33%)
- 2014: 1/2 (50.0%)
- 2015: 0/1 (0.0%)
- 2016: 2/2 (100.0%)
- 2017: 6/16 (37.5%)
- 2018: 9/24 (37.5%)
- 2019: 52/98 (53.06%)
- 2020: 48/108 (44.44%)
- 2021: 40/86 (46.51%)
- 2022: 46/102 (45.1%)
- 2023: 30/58 (51.72%)
```

## Usage

### Install vLLM package
```
# Install vLLM version 0.9.0.1.
# For example, if your CUDA version is 12.8, use the following command:
pip install vllm==0.9.0.1 --extra-index-url https://download.pytorch.org/whl/cu128
```

### Launch a server to deploy Skywork-SWE-32B

```
vllm serve ${MODEL_PATH} —served-model-name ${SERVED_MODEL_NAME} --host 0.0.0.0 --port 8000 --gpu-memory-utilization 0.95 --tensor-parallel-size 8
```

Since our model has 32 billion parameters and supports a 32K context length, we recommend launching the model server with at least 2 GPUs equipped with sufficient VRAM to ensure efficient inference.
### Set up OpenHands framework
```
git clone https://github.com/All-Hands-AI/OpenHands.git
cd OpenHands
git checkout tags/0.32.0
make build
```
The official documentation of OpenHands: [SWE-Bench Evaluation with OpenHands SWE-Bench Docker Image](https://github.com/All-Hands-AI/OpenHands/tree/main/evaluation/benchmarks/swe_bench)

###  Create the corresponding config file:
```
[core]
workspace_base="./workspace"
[llm.my-oss-model]
model = "openai/${SERVED_MODEL_NAME}"
base_url = "http://0.0.0.0:8000/v1"
api_key="vllm"
max_message_chars=32768
max_input_tokens=32768
max_output_tokens=8192
log_completions=true
temperature=0.0
```

If you want to run the OpenHands agent with test-time scaling techniques (a Best-of-N method based on the critic model), please refer to the [blog](https://www.all-hands.dev/blog/sota-on-swe-bench-verified-with-inference-time-scaling-and-critic-model) for detailed instructions. You will need to switch to the [feature/llm-critic](https://github.com/All-Hands-AI/OpenHands/tree/feature/llm-critic) branch and deploy the [critic model](https://huggingface.co/all-hands/openhands-critic-32b-exp-20250417) accordingly. Additionally, you need to add the following parameters into the configuration file:
```
use_critic=true
critic_model="critic_model"
critic_base_url="**********"
critic_api_key="************"
critic_num_candidates=2
```

### Rollout on SWE-Bench Instances
```
./evaluation/benchmarks/swe_bench/scripts/run_infer.sh [model_config] [git-version] [agent] [eval_limit] [max_iter] [num_workers] [dataset] [dataset_split]
# Example
./evaluation/benchmarks/swe_bench/scripts/run_infer.sh llm.my-oss-model HEAD CodeActAgent 500 100 1 princeton-nlp/SWE-bench_Verified test
```

### Evaluate generated patches
```
./evaluation/benchmarks/swe_bench/scripts/eval_infer.sh \
./evaluation_outputs/outputs/princeton-nlp__SWE-bench_Lite-test/CodeActAgent/my-oss-model_maxiter_100_N_v0.32.0-no-hint-run_1/output.jsonl
```

## Acknowledgements
We would like to thank the contributors of the [OpenHands](https://github.com/All-Hands-AI/OpenHands) and [AllHands Critic](https://huggingface.co/all-hands/openhands-critic-32b-exp-20250417) repositories for their open research and valuable contributions.

## Citation
If you use Skywork-SWE in your research, please consider citing our work using the following BibTeX entry:
```
@misc{skywork-swe,
  title={Skywork-SWE: Unveiling Data Scaling Laws for Software Engineering in LLMs},
  author={Liang Zeng, Yongcong Li, Yuzhen Xiao, Changshi Li, Chris Yuhao Liu, Rui Yan, Tianwen Wei, Jujie He, Xuchen Song, Yang Liu, and Yahui Zhou},
  howpublished={\url{https://quixotic-sting-239.notion.site/eb17f379610040ceb54da5d5d24065bd}},
  note={Notion Blog},
	year={2025},
}
```
# Fine-Tuning a Generative AI Model for Dialogue Summarization

This project demonstrates how to fine-tune an instruction-tuned Large Language Model (**FLAN-T5**) for **dialogue summarization** using Hugging Face.  
We compare **full fine-tuning** with **Parameter Efficient Fine-Tuning (PEFT / LoRA)** and evaluate performance using **ROUGE metrics**.

---

## 📌 Overview

- **Model:** FLAN-T5
- **Task:** Dialogue Summarization
- **Frameworks:** Hugging Face Transformers, PEFT (LoRA)
- **Evaluation:** ROUGE-1, ROUGE-2, ROUGE-L

---

## 📂 Project Structure

```text
.
├── notebook.ipynb    # Main notebook
├── data/             # Dialog-summary dataset
├── models/           # Fine-tuned models / adapters
├── results/          # Evaluation outputs
└── README.md

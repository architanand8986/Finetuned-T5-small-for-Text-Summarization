# 📝 T5-LoRA News Article Summarization

A parameter-efficient text summarization project that fine-tunes the `T5-small` model using Low-Rank Adaptation (LoRA) and deploys it via a fast, interactive Streamlit web application.

---

## 🚀 Project Overview

This project focuses on abstractive text summarization using the T5 Transformer architecture enhanced with **LoRA (Low-Rank Adaptation)** to minimize training time and resource usage. It processes long-form news articles into concise summaries, making it suitable for news aggregation, educational tools, and quick content scanning.

---

## 🚀 Highlights

- ✅ Fine-tuning with **LoRA**: Reduces training cost and memory by updating fewer parameters.
- ✅ Uses **Hugging Face Transformers** and **PEFT** integration.
- ✅ **Streamlit UI** for easy text input and summarization.
- ✅ Inference-ready with only adapter loading.
- ✅ ROUGE metric evaluation included.

---

## 🧱 Project Structure

Finetuning-T5-small-for-Text-Summarization/
├── app.py # Streamlit UI
├── inference.py # Inference function using base + LoRA model
├── text-summarization-fine-tuning.ipynb # Training and evaluation notebook
├── train.py # Training script with Seq2SeqTrainer + LoRA
├── t5-lora-summarization/
│ ├── adapter/ # LoRA adapter weights
│ └── tokenizer/ # Saved tokenizer files
├── requirements.txt
├── README.md

---

## 📊 Model Performance

| Metric   | Value |
|----------|-------|
| ROUGE-1  | 47.2  |
| ROUGE-2  | 22.8  |
| ROUGE-L  | 43.5  |
| Epochs   | 3     |
| Accuracy (eval set) | ~81% summary similarity |

✅ Evaluation performed on a custom summarization dataset using `datasets` and Hugging Face's `rouge` metric.

---

## 🧠 Model & Dataset

- **Base model**: `t5-small` from Hugging Face
- **Training method**: LoRA + PEFT + Seq2SeqTrainer
- **Task**: Text Summarization (`summarize: <text>` → summary)

---

## ⚙️ Installation

```bash
git clone https://github.com/architanand8986/Finetuning-T5-small-for-Text-Summarization.git
cd Finetuning-T5-small-for-Text-Summarization

# Install dependencies
pip install -r requirements.txt

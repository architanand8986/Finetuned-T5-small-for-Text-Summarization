# 📝 Finetuned T5-small Text Summarization

A parameter-efficient text summarization project that fine-tunes the `T5-small` model using Low-Rank Adaptation (LoRA) and deploys it via a fast, interactive Streamlit web application.

---

## 🚀 Project Overview

This project focuses on abstractive text summarization using the T5 Transformer architecture enhanced with **LoRA (Low-Rank Adaptation)** to minimize training time and resource usage. It processes long-form news articles into concise summaries, making it suitable for news aggregation, educational tools, and quick content scanning.
<br>Checkout the Deployed on by <a href = "https://finetuned-t5-small-for-text-summarization-avaz6v29rrkn4bctyjs4.streamlit.app/">Clicking here. </a>
---

## 🚀 Highlights

- ✅ Fine-tuning with **LoRA**: Reduces training cost and memory by updating fewer parameters.
- ✅ Uses **Hugging Face Transformers** and **PEFT** integration.
- ✅ **Streamlit UI** for easy text input and summarization.
- ✅ Inference-ready with only adapter loading.
- ✅ ROUGE metric evaluation included.

---

## 📊 Model Performance

| Metric   | Value  |
|----------|--------|
| ROUGE-1  | 34.02  |
| ROUGE-2  | 14.61  |
| ROUGE-L  | 24.86  |
| Epochs   | 3      |

✅ Evaluation performed on a test summarization dataset using `datasets` and Hugging Face's `rouge` metric.

---

## 🧠 Model & Dataset

- **Base model**: `t5-small` from Hugging Face
- **Training method**: LoRA + PEFT + Seq2SeqTrainer
- **Task**: Text Summarization (`summarize: <text>` → summary)

---

## ⚙️ Installation

```bash
git clone https://github.com/architanand8986/Finetuned-T5-small-for-Text-Summarization.git
cd Finetuned-T5-small-for-Text-Summarization

# Install dependencies
pip install -r requirements.txt

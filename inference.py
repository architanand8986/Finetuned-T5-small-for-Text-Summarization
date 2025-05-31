from transformers import T5Tokenizer, T5ForConditionalGeneration
from peft import PeftModel
import torch

# Load tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("t5-lora-summarization/tokenizer")
base_model = T5ForConditionalGeneration.from_pretrained("t5-small")
model = PeftModel.from_pretrained(base_model, "t5-lora-summarization/adapter")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

def summarize(text):
    inputs = tokenizer("summarize: " + text, return_tensors="pt", padding="max_length", truncation=True, max_length=512)
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    with torch.no_grad():
        output_ids = model.base_model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=256,
            num_beams=4,
            early_stopping=True
        )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

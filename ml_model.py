from transformers import AutoTokenizer, AutoModelForSequenceClassification
from dotenv import load_dotenv
import os
import torch

load_dotenv()
# Load the model from Hugging Face dynamically
MODEL_NAME = os.getenv("MODEL_NAME", "amharic-hate-speech-detection-mBERT") 

def load_model():
    """Load the model and tokenizer from Hugging Face."""
    try:
        print(f"Loading model: {MODEL_NAME}")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        return model, tokenizer
    except Exception as e:
        raise RuntimeError(f"Failed to load model: {e}")
    
# Predict function
def predict_hate_speech(text, model, tokenizer):
    """Predict the label for a given text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    prediction = torch.argmax(logits, dim=1).item()
    labels = {0: "free", 1: "hate"}
    return labels.get(prediction, "unknown")
    

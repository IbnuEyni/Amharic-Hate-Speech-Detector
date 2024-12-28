from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from pathlib import Path
from ml_model import load_model, predict_hate_speech

app = FastAPI()

# Load the model at startup
model, tokenizer = load_model()

class TextRequest(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def serve_html():
    """Serve the frontend HTML page."""
    html_path = Path("templates/index.html")
    return HTMLResponse(content=html_path.read_text(), status_code=200)

@app.post("/predict/")
async def predict(request: TextRequest):
    """Predict whether the input text is hate speech or free speech."""
    text = request.text
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    prediction = predict_hate_speech(text, model, tokenizer)  # Pass model and tokenizer here
    return {"text": text, "prediction": prediction}

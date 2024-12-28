# Amharic Hate Speech Detector

This application is designed to detect hate speech in Amharic text. It uses a fine-tuned BERT-based model to classify input text into two categories: "Hate Speech" or "Free Speech." The model is loaded dynamically from Hugging Face, and the application is implemented using FastAPI for efficient and scalable API services.

## Features

- **Dynamic Model Loading**: The model can be dynamically selected by specifying its name in an environment variable.
- **RESTful API Endpoint**: The application provides a single endpoint (`/predict`) to classify text.
- **Customizable Labels**: Outputs are mapped to human-readable labels (`free` and `hate`).
- **Web-Based Interface**: Includes a simple HTML template to interact with the API and test the model.


## Getting Started

### Prerequisites

Ensure the following are installed on your system:

- Python 3.8 or later
- pip (Python package manager)
- `virtualenv` (optional, but recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/amharic-hate-speech-detector.git
   cd amharic-hate-speech-detector
   ```

2. Create a virtual environment (optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory:
     ```env
     MODEL_NAME=amharic-hate-speech-detection-mBERT
     ```
   - Replace `amharic-hate-speech-detection-mBERT` with your preferred model name on Hugging Face if needed.


## Usage

### Running the Application

1. Start the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and visit:
   - API Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Web Interface: Open `index.html` in a browser (manually or host it using a simple HTTP server).


### API Endpoints

#### **POST** `/predict`

Predicts whether the given Amharic text is hate speech or free speech.

- **Request**:
  ```json
  {
    "text": "ሰላም እንዴት ነው።"
  }
  ```

- **Response**:
  ```json
  {
    "text": "ሰላም እንዴት ነው።",
    "prediction": "free"
  }
  ```


### Example: Testing with cURL

You can test the API directly using `curl`:

```bash
curl -X POST http://127.0.0.1:8000/predict/ \
     -H "Content-Type: application/json" \
     -d '{"text": "ሰላም እንዴት ነው።"}'
```

## File Structure

```
.
├── main.py               # Main FastAPI application
├── ml_model.py           # Model loading and prediction logic
├── requirements.txt      # Python dependencies
├── index.html            # Web-based interface for testing
├── .env                  # Environment variables
└── README.md             # Documentation (this file)
```


## How It Works

1. **Model Loading**:
   - The application dynamically loads the model and tokenizer from Hugging Face based on the `MODEL_NAME` environment variable.

2. **Prediction**:
   - The input text is tokenized, and the model predicts whether it contains hate speech.
   - The output logits are converted to human-readable labels (`free` or `hate`).

3. **Web Interface**:
   - The `index.html` file provides a simple form to input text and display the prediction result.


## Enhancements and Suggestions

- **Model Hosting**: For faster inference, consider hosting the model on Hugging Face Hub or using a local deployment service.
- **Batch Predictions**: Add support for processing multiple texts in a single API call for efficiency.
- **Frontend Improvements**: Enhance the web interface with better styling or a dashboard.
- **Multilingual Support**: Extend the application to support other languages.


## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.


## Acknowledgments

- **Hugging Face**: For providing the transformer models and tokenizer.
- **FastAPI**: For the lightweight and powerful web framework.


## Contact

For questions or support, contact [shuaibahmedin@gmail.com](mailto:shuaibahmedin@gmail.com).

# AI-NLP-Pipeline

> A Flask-based AI-powered NLP pipeline that extracts structured information from unstructured text using Large Language Models (LLMs). The API accepts raw text and returns clean JSON containing entities, keywords, summaries, sentiment, and metadata.

---

# Project Overview

AI-NLP-Pipeline is a lightweight Natural Language Processing API built using **Python** and **Flask**. The application receives unstructured text from clients, processes it through an AI model, validates the generated output, and returns structured JSON.

The project demonstrates how modern AI models can be integrated into backend applications while maintaining reliability through preprocessing, prompt engineering, JSON validation, and error handling.

---

## 🚀 Features

-  Text preprocessing and cleaning
-  Natural Language Processing pipeline
-  Text analysis and information extraction
-  JSON-based API responses
-  Flask REST API integration
-  Modular project structure
-  Error handling for invalid inputs

---

# Project Workflow

```
                Dataset
                   │
                   ▼
         preprocess.py
      (Cleaning & Feature Engineering)
                   │
                   ▼
             train.py
      (Train Scikit-learn Model)
                   │
             Save Model (.joblib)
                   │
                   ▼
              predict.py
         (Load Model & Predict)
                   │
                   ▼
               app.py
          (Flask REST API)
                   │
                   ▼
              JSON Response
```
# Technology Stack
```
| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | REST API framework |
| Pandas | Data loading, cleaning, and preprocessing |
| Scikit-learn | Machine learning model training and prediction |
| Joblib | Saving and loading trained ML models |
| NumPy | Numerical computations |
| CSV Dataset | Training and evaluation data |
| JSON | API request and response format |
```
# Project Structure

```
AI-NLP-Pipeline/
│
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
│
├── dataset/
│   └── labeled_dataset.csv
│
└── src/
    ├── preprocess.py     # Data cleaning and preprocessing
    ├── train.py          # Train the machine learning model
    └── predict.py        # Load model and make predictions
```

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | REST API development |
| NLP | Text processing |
| JSON | Data exchange format |
| Regex | Text pattern extraction |
| NLTK / spaCy | NLP operations |
| Git | Version control |

---
# Project Approach

### Step 1 – Dataset Preparation
- Load the labeled dataset (`labeled_dataset.csv`) using **Pandas**.
- Handle missing values, clean text, and prepare data for training.

### Step 2 – Data Preprocessing
The `preprocess.py` module performs:
- Text cleaning
- Lowercasing
- Removing unnecessary characters
- Feature extraction
- Preparing input for model training

### Step 3 – Model Training
The `train.py` script:
- Splits the dataset into training and testing sets.
- Trains a **Scikit-learn** machine learning model.
- Evaluates model performance.
- Saves the trained model using **Joblib** for later use.

### Step 4 – Prediction
The `predict.py` module:
- Loads the saved model using Joblib.
- Accepts new input text.
- Applies the same preprocessing steps.
- Generates predictions.

### Step 5 – API Integration
The Flask application (`app.py`):
- Exposes REST API endpoints.
- Receives JSON requests.
- Passes input to the prediction module.
- Returns predictions as structured JSON responses.

---

# Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/ByteBandit-100/AI-NLP-Pipeline.git
cd AI-NLP-Pipeline
```

---

## 2. Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Verify Project Structure

```
AI-NLP-Pipeline/
│
├── .gitignore
├── app.py
├── README.md
├── requirements.txt
│
├── dataset/
│   └── labeled_dataset.csv
│
└── src/
    ├── preprocess.py
    ├── train.py
    └── predict.py
```

---

# Running the Project

The project should be executed in the following sequence.

## Step 1: Preprocess the Dataset

Clean and prepare the dataset for model training.

```bash
python src/preprocess.py
```

Expected outcome:
- Dataset is cleaned and transformed.
- Data is prepared for training.

---

## Step 2: Train the Machine Learning Model

Train the classifier using the preprocessed dataset.

```bash
python src/train.py
```

Expected outcome:
- Model is trained.
- Trained model is saved as a `.joblib` file (or the filename configured in your project).
- Training metrics are displayed in the terminal.

---

## Step 3: Test the Prediction Module (Optional)

Run the prediction script directly to verify that the trained model loads correctly.

```bash
python src/predict.py
```

Expected outcome:
- The saved model is loaded.
- Sample input is processed.
- Predicted output is displayed.

---

## Step 4: Start the Flask API

Launch the REST API server.

```bash
python app.py
```

If the server starts successfully, you should see output similar to:

```
* Running on http://127.0.0.1:5000
```

---

# Using the API

## Base URL

```
http://127.0.0.1:5000
```

---

## Health Check

### Request

```
GET /
```

### Response

```text
"message": "Product Attribute Extraction API",
"endpoint": "/extract"
```

---

## Extract Endpoint

### Request
```
POST /extract
```

**Headers**

```
Content-Type: application/json
```

**Request Body**

```json
{
    "text": "John Doe joined Google as a Software Engineer in California in 2023."
}
```

### Successful Response (200 OK)

```json
{
    "entities": {
        "PERSON": [
            "John Doe"
        ],
        "ORGANIZATION": [
            "Google"
        ],
        "LOCATION": [
            "California"
        ],
        "DATE": [
            "2023"
        ]
    }
}
```

---

### Error Response (400 Bad Request)

```json
{
    "error": "Missing 'text' field in request."
}
```

---

### Invalid JSON Response (400 Bad Request)

```json
{
    "error": "Invalid JSON format."
}
```

> **Note:** The response format depends on your trained model. It may return a class label, category, sentiment, or another prediction based on your dataset.

---

# Testing with Postman

1. Open **Postman**.
2. Create a new **POST** request.
3. Enter the URL:

```
http://127.0.0.1:5000/extract
```

4. Select **Body → raw → JSON**.
5. Paste the following:

```json
{
    "text": "This service was excellent."
}
```

6. Click **Send**.
7. View the JSON response.

---

# Troubleshooting

| Issue | Possible Solution |
|--------|-------------------|
| `ModuleNotFoundError` | Install dependencies using `pip install -r requirements.txt`. |
| `FileNotFoundError` | Verify the dataset and model file paths. |
| `Model not found` | Run `python src/train.py` to generate the trained model. |
| `404 Not Found` | Check that the requested endpoint matches those defined in `app.py`. |
| `400 Bad Request` | Ensure the request body is valid JSON and includes the required fields. |
| `500 Internal Server Error` | Review the terminal logs for the underlying exception. |

---


# Learning Objectives

This project helps understand:

- NLP pipeline architecture
- API development using Flask
- JSON data processing
- AI model integration
- Backend engineering practices

---

# Author

**Mohit**

GitHub:
https://github.com/ByteBandit-100

---

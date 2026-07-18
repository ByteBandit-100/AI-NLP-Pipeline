# AI-NLP-Pipeline 🤖🧠

An AI-powered Natural Language Processing (NLP) pipeline that processes text data, performs analysis, extracts meaningful information, and provides structured JSON outputs through a Flask API.

The project demonstrates how modern NLP workflows can be built using Python, machine learning techniques, and REST APIs.

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

# 📌 How It Works

The pipeline follows these steps:

```
Input Text
    |
    ↓
Text Preprocessing
    |
    ↓
NLP Processing
    |
    ↓
Information Extraction
    |
    ↓
Structured JSON Output
```

---

# 🔧 Installation & Setup

## 1. Clone Repository

```bash
git clone https://github.com/ByteBandit-100/AI-NLP-Pipeline.git
```

Move into project directory:

```bash
cd AI-NLP-Pipeline
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start Flask server:

```bash
python app.py
```

Server will start:

```
http://127.0.0.1:5000
```


# 🧪 Testing API

Using CURL:

```bash
curl -X POST http://127.0.0.1:5000/extract \
-H "Content-Type: application/json" \
-d "{\"text\":\"AI is transforming the technology industry\"}"
```
 
# Evaluation
 
Metrics are computed per attribute on the 20% held-out test split:
accuracy and weighted F1 (weighted by class support so rare classes
don't dominate or vanish). Regenerated automatically by `src/train.py`
into `evaluation.csv`. <br>
 
<img width="292" height="184" alt="image" src="https://github.com/user-attachments/assets/8ab3fff6-60b9-4924-ab26-999d25499466" />

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

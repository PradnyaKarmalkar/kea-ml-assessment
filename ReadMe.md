# 🚀 KeaBuilder ML Similarity Engine

## 📌 Overview

This project implements a lightweight **ML-powered semantic similarity engine** designed for integration into KeaBuilder (a funnel and lead automation platform).

The system matches user inputs (leads, prompts, queries) based on **meaning**, not just keywords, enabling smarter automation and better user experience.

---


**Link Loom Video**
https://www.loom.com/share/369c2a177c404b89bd828ce663c6c46d

## 🎯 Problem Statement

Traditional systems rely on keyword matching, which fails to capture intent.

**Example:**

* “Buy a house” ≠ “Invest in property” (keyword-based ❌)
* But semantically they are similar (ML-based ✅)

---

## 💡 Solution

This project uses **sentence embeddings + cosine similarity** to identify the most relevant match for a given query.

---

## ⚙️ Features

* ✅ Semantic similarity using transformer embeddings
* ✅ FastAPI-based ML microservice
* ✅ Precomputed embeddings for efficiency
* ✅ Latency tracking (performance monitoring)
* ✅ Clean modular code structure

---

## 🧠 How It Works

1. Convert text → embeddings (numerical vectors)
2. Compare query embedding with stored embeddings
3. Compute similarity using cosine similarity
4. Return the most similar input

---

## 🏗️ Project Structure

```
kea-ml-assessment/
│
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── model.py         # Model loading + embeddings
│   ├── similarity.py    # Matching logic
│   ├── schemas.py       # Request/response models
│
├── data/
│   └── sample_inputs.json
│
├── outputs/
│   └── sample_output.json
│
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/PradnyaKarmalkar/kea-ml-assessment.git
cd kea-ml-assessment
```

```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

---

## 🌐 API Usage

### Endpoint:

```
POST /match
```

### Request:

```json
{
  "query": "I want to invest in property"
}
```

### Response:

```json
{
  "query": "I want to invest in property",
  "top_match": "Looking for real estate investment",
  "similarity_score": 0.87,
  "latency_ms": 12.3
}
```

---

## 🧪 Testing

Use Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🏗️ Production Design

* Node.js backend → calls ML API (FastAPI)
* ML service runs independently (microservice)
* Redis → caching frequent queries
* Queue system → async processing for heavy tasks

---

## ⚠️ Challenges

* Handling real-world noisy data
* Managing latency for real-time systems
* Scaling similarity search for large datasets

---

## 🔧 Future Improvements

* 🔹 Vector database integration (FAISS / Pinecone)
* 🔹 Real-time learning from user data
* 🔹 Personalization layer
* 🔹 Caching for faster responses

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Sentence Transformers
* Scikit-learn
* NumPy

---


## 👩‍💻 Author

**Pradnya Karmalkar**

GitHub: https://github.com/PradnyaKarmalkar

---



## ⭐ Final Note

This project focuses on **practical ML system design**—simple, scalable, and production-oriented rather than heavy model training.

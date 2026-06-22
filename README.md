# OpsBrain AI 🚀

AI-Powered Industrial Knowledge Assistant built for **ET AI Hackathon 2.0**.

## Problem Statement

Industrial organizations generate thousands of documents including:

* Safety Manuals
* Maintenance Reports
* Inspection Reports
* Standard Operating Procedures (SOPs)
* Compliance Documents

Finding critical information quickly is difficult and time-consuming.

OpsBrain AI solves this problem by enabling users to upload documents and ask questions in natural language.

---

## Features

### Document Upload

* Upload PDF documents
* Secure storage of uploaded files

### Document Intelligence

* Extract text from PDF files
* Process technical and operational documents

### AI Question Answering

* Ask questions about uploaded documents
* Powered by Google Gemini AI

### Knowledge Retrieval

* Search relevant information from uploaded documents
* Context-aware responses

---

## Architecture

```text
PDF Upload
    ↓
FastAPI Backend
    ↓
Text Extraction (PyPDF)
    ↓
Document Processing
    ↓
Gemini AI
    ↓
AI Response
```

---

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python

### AI & ML

* Google Gemini API
* Sentence Transformers
* ChromaDB

### Storage

* Local File Storage
* Vector Database (ChromaDB)

---

## Project Structure

```text
opsbrain-ai/
│
├── frontend/
│   ├── app/
│   ├── components/
│   └── public/
│
├── backend/
│   ├── uploads/
│   ├── main.py
│   ├── gemini_test.py
│   └── requirements.txt
│
├── datasets/
├── docs/
└── README.md
```

---

## Installation

### Backend

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger API:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```text
http://localhost:3000
```

---

## API Endpoints

### Upload PDF

```http
POST /upload
```

Uploads and processes PDF documents.

### Ask Questions

```http
GET /ask?question=...
```

Returns AI-generated answers based on uploaded documents.

### Health Check

```http
GET /
```

Returns API status.

---

## Future Enhancements

* Multi-document support
* ChromaDB vector search
* OCR for scanned PDFs
* Compliance analysis agent
* Root cause analysis assistant
* Industrial knowledge graph
* Advanced dashboard and analytics

---

## Demo Workflow

1. Upload PDF
2. Extract document content
3. Ask questions
4. Receive AI-powered answers

---

## Hackathon

Built for **ET AI Hackathon 2.0**

Team: Bangaru Karthik Reddy

---

## License

MIT License

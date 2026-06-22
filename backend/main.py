from fastapi import FastAPI, UploadFile, File
from pypdf import PdfReader
from dotenv import load_dotenv
import google.generativeai as genai
import os
import shutil

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

DOCUMENT_TEXT = ""

@app.get("/")
def root():
    return {"message": "OpsBrain AI Running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global DOCUMENT_TEXT

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    DOCUMENT_TEXT = text

    return {
        "status": "success",
        "filename": file.filename,
        "characters_extracted": len(text)
    }

@app.get("/ask")
async def ask(question: str):

    prompt = f"""
    You are an Industrial Knowledge Assistant.

    DOCUMENT:
    {DOCUMENT_TEXT}

    QUESTION:
    {question}

    Answer based only on the document.
    """

    response = model.generate_content(prompt)

    return {
        "question": question,
        "answer": response.text
    }
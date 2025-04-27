# 📚 PDF Question-Answer Engine 🚀 (FastAPI + LangChain)

This project is a **FastAPI-based Question Answering (QA) Engine** that allows users to:

- 📄 Upload a PDF
- ❓ Ask questions based on its content
- 📥 Automatically generate a **Question-Answer CSV** using a language model pipeline!

🔹 Built using **FastAPI**, **Jinja2**, **LangChain**, and **OpenAI APIs**.

---

## ✨ Features

- Upload PDFs securely via web UI.
- Process uploaded documents using an LLM pipeline (`llm_pipeline` from `src.helper`).
- Generate and download a QA CSV file with model-generated questions and answers.
- Full asynchronous support with `aiofiles`.
- Templated frontend using **Jinja2** and simple **HTML/CSS/JavaScript**.
- Static file support (`/static/docs`, `/static/output` folders for files).

---

## 🛠 Technology Stack

- **Backend**: FastAPI
- **Frontend**: Jinja2 templating
- **Language Model**: LangChain + OpenAI (via `.env` OpenAI API Key)
- **Storage**: Local disk (`static/docs/` for PDFs, `static/output/` for CSVs)
- **Libraries**: `aiofiles`, `pypdf`, `faiss-cpu`, `langchain-core`, `openai`, `python-multipart`, etc.

---

## 📂 Folder Structure
.
├── app.py                  # Main FastAPI application
├── requirements.txt        # Project dependencies
├── setup.py                # Python package setup file
├── .env                    # Environment variables (e.g., OpenAI API Key)
├── templates/
│   └── index.html          # Jinja2 template (Frontend HTML page)
├── static/
│   ├── docs/               # Uploaded PDFs are stored here
│   └── output/             # Generated QA CSV files stored here
├── src/
│   └── helper.py           # llm_pipeline function for processing PDFs


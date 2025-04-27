from fastapi import FastAPI, Form, Request, Response, File, UploadFile, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import uvicorn
import os
import aiofiles
import json
import csv
from src.helper import llm_pipeline

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_file(request: Request, pdf_files: UploadFile = File(...)):
    base_folder = 'static/docs/'
    if not os.path.isdir(base_folder):
        os.makedirs(base_folder)
    pdf_filename = os.path.join(base_folder, pdf_files.filename)

    async with aiofiles.open(pdf_filename, 'wb') as f:
        content = await pdf_files.read()
        await f.write(content)

    response_data = {"msg": "success", "pdf_filename": pdf_filename}
    return JSONResponse(content=response_data)

def get_csv(file_path):
    answer_generation_chain, ques_list = llm_pipeline(file_path)
    
    base_folder = 'static/output/'
    if not os.path.isdir(base_folder):
        os.makedirs(base_folder)
    output_file = os.path.join(base_folder, "QA.csv")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Question", "Answer"])

        for question in ques_list:
            print(f"Question: {question}")
            answer = answer_generation_chain.run(question)
            print(f"Answer: {answer}")
            print("------------------------------\n\n")
            csv_writer.writerow([question, answer])
    
    return output_file

@app.post("/analyze")
async def analyze_file(request: Request, pdf_filename: str = Form(...)):
    output_file = get_csv(pdf_filename)
    response_data = {"output_file": output_file}
    return JSONResponse(content=response_data)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)

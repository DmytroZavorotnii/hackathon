import base64

from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from config import DOCS_DIR
import os
from config import LLM, CHROMA_DB_PATH, EMBEDDING
from document_loader import DocumentLoader
from search_chain import SearchChain

llm = LLM
chroma_db_path = CHROMA_DB_PATH
embedding = EMBEDDING

document_loader = DocumentLoader()
document_searcher = SearchChain()


app = FastAPI()

class LoadDocumentRequest(BaseModel):
    filename: str
    content: str

@app.post("/load_document/")
async def load_document(request: LoadDocumentRequest, response: Response):
    try:
        decoded_content = base64.b64decode(request.content.encode("utf-8")).decode("utf-8", "ignore")
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            "status": "fail",
            "error_message": f"Invalid base64 content: {str(e)}"
        }

    try:
        file_path = os.path.join(DOCS_DIR, request.filename)

        if os.path.exists(file_path):
            response.status_code = status.HTTP_409_CONFLICT
            return {
                "status": "fail",
                "error_message": f"File '{request.filename}' already exists."
            }

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(decoded_content)

        await document_loader.load_document(file_path)

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": "fail",
            "error_message": f"Failed to save or process file: {str(e)}"
        }

    return {
        "status": "success",
        "filename": request.filename
    }

@app.get("/retrieve_documents/")
async def retrieve_documents(query: str):
    doc_list = document_searcher.retrieve_documents(user_input=query)
    return {"list_filename": doc_list}

@app.get("/create_summarized_answer/")
async def create_summarized_answer(query: str):

    results = document_searcher.create_summarized_answer(user_input=query)
    return {
        "answer": results["answer"],
        "context": results["context"]
    }
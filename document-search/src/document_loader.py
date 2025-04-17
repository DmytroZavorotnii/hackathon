from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import VECTOR_STORE

class DocumentLoader:
    def __init__(self,):
        pass
    

    async def load_pdf_document(self, file_path: str):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        await VECTOR_STORE.aadd_documents(splits)

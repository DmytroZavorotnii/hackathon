from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import VECTOR_STORE
from loguru import logger
class DocumentLoader:
    def __init__(self,):
        pass
    

    async def load_document(self, file_path: str):
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path=file_path)
        elif file_path.endswith(".txt"):
            loader = TextLoader(file_path=file_path, encoding="utf-8")
        else:
            logger.error('incorrect filename')
            raise Exception()
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        splits = text_splitter.split_documents(docs)
        await VECTOR_STORE.aadd_documents(splits)
    

from dataclasses import dataclass
import dotenv
import os
from langchain_chroma import Chroma
from langchain_groq.chat_models import ChatGroq
from langchain.embeddings import HuggingFaceEmbeddings

DOCS_DIR = "../docs"

os.makedirs(DOCS_DIR, exist_ok=True)

dotenv.load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
COLLECTION_NAME = "test_collection"
LLM = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant"
    )

file_path = "./єВідновлення/Компенсація_єВідновлення_майно.pdf"
CHROMA_DB_PATH = "./chroma_langchain_db"
EMBEDDING = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")

VECTOR_STORE = Chroma(
    collection_name=COLLECTION_NAME,
    embedding_function=EMBEDDING,
    persist_directory=CHROMA_DB_PATH,
)

RETRIEVER = VECTOR_STORE.as_retriever()
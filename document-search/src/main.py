import asyncio
from config import LLM, CHROMA_DB_PATH, EMBEDDING
from document_loader import DocumentLoader
from search_chain import SearchChain

llm = LLM
chroma_db_path = CHROMA_DB_PATH
embedding = EMBEDDING

document_loader = DocumentLoader()
document_searcher = SearchChain()


async def main():
    await document_loader.load_document("../predifined_docs/Компенсація_єВідновлення_майно.pdf")

if __name__ == "__main__":
    asyncio.run(main())
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
    # await document_loader.load_pdf_document("./../docs/єВідновлення/Компенсація_єВідновлення_майно.pdf")
    while True:
        user_input = input("Ваше запитання (q для виходу): ")
        if user_input.strip().lower().startswith("q"):
            print("Виходимо...")
            break

        results = document_searcher.create_summarized_answer(user_input)
        answer = results["answer"]
        context = results["context"]


        print(f"// Відповідь //\n {results["answer"]}")

        print("\n// Використаний контекст //\n")
        for doc in results["context"]:
            print(doc)
            print("=======")


if __name__ == "__main__":
    asyncio.run(main())
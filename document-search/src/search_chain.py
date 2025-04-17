from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from config import LLM, RETRIEVER


class SearchChain:
    
    def __init__(self):
        self.system_prompt = (
            "Ви – помічник для завдань з питаннями. Щоб відповісти на запитання, скористайтеся наведеними нижче фрагментами отриманого контексту. "
            "Якщо ви не знаєте відповіді, скажіть, що не знаєте. Використовуйте максимум три речення та тримайте відповідь короткою. Відповідай лише українською"
            "\n\n"
            "{context}"
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("human", "{input}"),
        ])

        self.question_answer_chain = create_stuff_documents_chain(llm=LLM, prompt=self.prompt)
        self.rag_chain = create_retrieval_chain(RETRIEVER, self.question_answer_chain)

            
            
    def create_summarized_answer(self, user_input):
        return self.rag_chain.invoke({"input": user_input})

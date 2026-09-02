from v_retriever import retriever
from vi_prompt import prompt
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b"
)

def format_docs(docs):
    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

chain = ( {
    "context": retriever | format_docs , "question": RunnablePassthrough()
}   | prompt
    | llm
    | StrOutputParser()
)

question = "what is prompt engineering?"

result = chain.invoke(question)

print(result)
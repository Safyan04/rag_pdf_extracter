from v_retriever import retriever
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful and reliable AI assistant.

Answer the user's question using only the information provided
in the context.

Rules:
- Do not make up information.
- Do not use information outside the context.
- Give a clear and concise answer.
- If the answer is not present in the context,
  say: "I don't know based on the provided context."

Context:
{context}
"""
    ),
    (
        "human",
        "{question}"
    )
])
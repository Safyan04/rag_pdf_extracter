import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="AI PDF QA System", page_icon="📄", layout="centered")

st.title("📄 AI PDF Question & Answer System")
st.write("Upload your PDF document and ask questions about its content.")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    temp_file_path = "temp.pdf"
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with st.spinner("Processing PDF... Please wait."):
        try:
            loader = PyPDFLoader(temp_file_path)
            documents = loader.load()
            
            embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
            st.session_state.vectorstore = Chroma.from_documents(documents, embeddings)
            
            st.success("PDF processed successfully! Ask your questions below.")
        except Exception as e:
            st.error(f"Error processing PDF: {e}")

if st.session_state.vectorstore is not None:
    user_query = st.text_input("Ask a question about the PDF:")

    if user_query:
        with st.spinner("Generating answer..."):
            try:
                docs = st.session_state.vectorstore.similarity_search(user_query, k=3)
                context = "\n".join([doc.page_content for doc in docs])
                
                # Aapka apna prompt template yahan properly integrate kar diya hai
                prompt_template = ChatPromptTemplate.from_messages([
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
                
                llm = ChatGroq(model="openai/gpt-oss-120b", temperature=0)
                
                # Prompt ko format karke LLM ko bhejna
                formatted_prompt = prompt_template.format_messages(context=context, question=user_query)
                response = llm.invoke(formatted_prompt)
                
                st.markdown("### Answer:")
                st.write(response.content)
            except Exception as e:
                st.error(f"Error generating answer: {e}")
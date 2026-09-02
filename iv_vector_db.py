from langchain_chroma import Chroma
from ii_chunks import chunk
from iii_embeding import embedding
from dotenv import load_dotenv

load_dotenv()



persist_dir = "./chroma_db"
collection_name = "vector_db"

vector_store = Chroma.from_documents(
    documents=chunk,
    embedding=embedding,
    persist_directory=persist_dir,
    collection_name=collection_name
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from i_loader import pdf

split = RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=100)
chunk = split.split_documents(pdf) # Call the load funtion from loader.py
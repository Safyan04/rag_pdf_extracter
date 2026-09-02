from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\Users\Safyan Ahmad\Desktop\practice\50_AI_Tech_Concepts.pdf")
pdf = loader.load()
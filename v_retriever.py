from iv_vector_db import vector_store

retriever = vector_store.as_retriever(search_kwargs={'k':4})

docs = retriever.invoke('What is fine-tuning')
# RAG PDF Question Answering System

A simple **Retrieval-Augmented Generation (RAG)** application built with **LangChain, ChromaDB, and Google Gemini**.

The system loads a PDF, splits its content into chunks, creates embeddings, stores them in ChromaDB, retrieves relevant information, and generates answers using Gemini.

## Project Structure

```text
rag_pdf_extractor/
│
├── chroma_db/              # ChromaDB vector database
├── temp.pdf                # Source PDF
│
├── app.py                  # Main application
├── i_loader.py             # PDF loading
├── ii_chunks.py            # Text chunking
├── iii_embeding.py         # Gemini embeddings
├── iv_vector_db.py         # ChromaDB setup
├── v_retriever.py          # Semantic retriever
├── vi_prompt.py            # RAG prompt
├── vii_chain.py            # RAG chain
│
└── .env                    # API key configuration
````

## RAG Pipeline

```text
PDF
 ↓
Document Loader
 ↓
Text Chunking
 ↓
Gemini Embeddings
 ↓
ChromaDB
 ↓
Retriever
 ↓
Prompt
 ↓
Gemini LLM
 ↓
Final Answer
```

## Technologies

* **Python**
* **LangChain**
* **Google Gemini**
* **ChromaDB**
* **PyPDF**
* **python-dotenv**

## Main Components

### `i_loader.py`

Loads the PDF using `PyPDFLoader` and converts it into LangChain documents.

### `ii_chunks.py`

Splits the document into smaller chunks using `RecursiveCharacterTextSplitter`.

Current configuration:

```python
chunk_size = 400
chunk_overlap = 40
```

### `iii_embeding.py`

Generates vector embeddings for the document chunks using Google Gemini embeddings.

### `iv_vector_db.py`

Stores the generated embeddings in a local **ChromaDB** database.

```text
chroma_db/
```

### `v_retriever.py`

Performs semantic similarity search and retrieves the most relevant chunks from ChromaDB.

```python
search_kwargs={"k": 2}
```

### `vi_prompt.py`

Defines the prompt that combines the user's question with the retrieved context.

### `vii_chain.py`

Connects the retriever, prompt, and Gemini LLM to generate the final answer.

### `app.py`

Main application used to interact with the RAG system.

## Installation

Clone the repository:

```bash
git clone https://github.com/Safyan04/rag_pdf_extractor.git
cd rag_pdf_extractor
```

Create a virtual environment:

```bash
python -m venv .envr
```

Activate it on Windows:

```bash
.envr\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install langchain langchain-chroma langchain-google-genai langchain-text-splitters pypdf python-dotenv
```

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

**Never upload your `.env` file or API key to GitHub.**

## Run the Project

Run the complete application:

```bash
python app.py
```

You can also test individual components:

```bash
python i_loader.py
python ii_chunks.py
python iii_embeding.py
python iv_vector_db.py
python v_retriever.py
python vii_chain.py
```

## How It Works

When a user asks a question, the system:

1. Searches ChromaDB for relevant PDF chunks.
2. Retrieves the most relevant context.
3. Adds the context to the prompt.
4. Sends the prompt to Gemini.
5. Returns the generated answer.

## Author

**Muhammad Safyan**

```
```

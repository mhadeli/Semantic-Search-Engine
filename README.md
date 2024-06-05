# Semantic Search Engine
==========================

A Streamlit-powered semantic search engine that uses Pinecone's vector database and OpenAI's LLM model to answer questions about uploaded documents.

## How it Works
--------------

### Step 1: Document Upload

Upload a document (PDF, DOCX, or TXT) using the file uploader. The document is then processed to extract its text content.

### Step 2: Text Splitting

The extracted text is split into smaller chunks using a recursive character text splitter. This allows for more efficient processing and querying of the text data.

### Step 3: Vectorization

The split text chunks are then vectorized using OpenAI's embeddings. This converts the text data into numerical vectors that can be used for similarity search.

### Step 4: Similarity Search

The vectorized text chunks are indexed in a Pinecone vector database. When a user asks a question, the question is also vectorized and used to query the database for similar vectors.

### Step 5: Question Answering

The top similar vectors are retrieved from the database and used to generate an answer to the user's question using OpenAI's LLM model.

### Step 6: Answer Display

The generated answer is then displayed to the user in the web app.

## Technology Stack
-------------------

* Streamlit: for building the web app
* Pinecone: for vector database and similarity search
* OpenAI: for LLM model and question answering
* Python: for scripting and development

## License
-------

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing
------------

Contributions are welcome If you'd like to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgments
---------------

This project was inspired by the Langchain library and the Pinecone vector database.

# Semantic Search Engine
==========================

A Streamlit-powered semantic search engine that uses Pinecone's vector database and OpenAI's LLM model to answer questions about uploaded documents.

## Getting Started
---------------

### Prerequisites

* Python 3.8 or later
* Streamlit 1.10 or later
* Pinecone API key and environment
* OpenAI API key

### Installation

1. Clone this repository: `git clone https://github.com/mhadeli/Semantic-Search-Engine.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set your Pinecone API key, environment, and OpenAI API key as environment variables:

export PINECONE_API_KEY="your_pinecone_api_key_here"
export PINECONE_API_ENV="your_pinecone_api_env_here"
export OPENAI_API_KEY="your_openai_api_key_here"
### Running the App

1. Run the app: `streamlit run app.py`
2. Open a web browser and navigate to `http://localhost:8501`

## Usage
-----

1. Upload a document (PDF, DOCX, or TXT) using the file uploader.
2. Ask a question related to the document in the text area.
3. Click the "Submit" button to get the answer.

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

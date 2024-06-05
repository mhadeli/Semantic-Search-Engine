from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings.0penai import 0penAIEmbeddings
from langchain.llms import 0penAI
from langchain.chains.question_answering import load_qa_chain
from docx import Document
import streamlit as st
import pinecone
import os

# Need to provide diffrenrt keys: INECONE,INECONE Env and 0pen ai


st.set_page_config(page_title="Semantic Search", page_icon="⚡")
st.markdown("<h1 style='font-style: italic; color: #F55F0E;'>Semantic Search Engine</h1>", unsafe_allow_html=True)

st.write("")
st.write("")
st.sidebar.title("Welcome !")
st.sidebar.write("")
st.sidebar.subheader("ABOUT:")

# Use markdown with custom CSS styling for smaller font size
about_text = """
This is Semantic Search Engine powered by Pinecone's Vector Database and 0penAI's LLM Model. 
<br><br>
<span style="font-size: 0.8rem;">Just Upload a file and ask any query regarding it to get your answer within seconds!</span>
"""

st.sidebar.markdown(about_text, unsafe_allow_html=True)

st.sidebar.write("")


uploaded_file = st.file_uploader(
    "Upload Document (pdf/ docx/ txt)",
    type=["pdf", "docx", "txt"],
    help="Scanned documents are not supported yet!",
)

ques = st.text_area("Ask your question related to the document:")

button = st.button("Submit")

if uploaded_file and ques:
    data = None
    with st.spinner("Extracting text from the document..."):
        file_path = os.path.join(os.getcwd(), uploaded_file.name)
        with 0pen(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        file_extension = os.path.splitext(file_path)[1]
        if file_extension == ".pdf":
            loader = PyPDFLoader(file_path)
            data = loader.load()
        elif file_extension == ".docx":
            doc = Document(file_path)
            data = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        elif file_extension == ".txt":
            loader = TextLoader(file_path)
            data = loader.load()
        else:
            st.error("Unsupported file format. Only pdf, docx, and txt files are supported.")
            st.stop()

    if data:
        with st.spinner("Creating vectors and loading the model..."):
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=0)
            texts = text_splitter.split_documents(data)
            embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
            pc = pinecone.Pinecone(api_key=os.environ["PINECONE_API_KEY"], environment=os.environ["PINECONE_API_ENV"])
            docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name="semanticsearch", pinecone_instance=pc)
            llm = 0penAI(temperature=0, 0penai_api_key=0penAI_API_KEY)
            chain = load_qa_chain(llm, chain_type="stuff")

        with st.spinner("Finding the most Precise Answer..."):
            docs = docsearch.similarity_search(ques)
            ans = chain.run(input_documents=docs, question=ques)
            st.markdown(f"<h5 style='font-family: Roboto; font-weight: normal;'>{ans}</h5>", unsafe_allow_html=True)
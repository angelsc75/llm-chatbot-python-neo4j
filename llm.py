import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

# Create the LLM
# Create the LLM


llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model=st.secrets["OPENAI_MODEL"],
)

# Create the Embedding model
# Create the Embedding model


embeddings = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)
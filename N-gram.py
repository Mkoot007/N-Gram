import streamlit as st
import nltk
from nltk import bigrams, word_tokenize
from docx import Document

nltk.download('punkt', download_dir='.')
def extract_bigrams(text):
    words = word_tokenize(text)
    bigram_list = list(bigrams(words))
    return bigram_list
def extract_text_from_docx(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + " "
    return text
st.title("Bigram Extractor")
st.text("Made by Moneeb Ahmad with Lil Love ❤️  ")
file = st.file_uploader("Upload a document (DOCX)", type=["docx"])
text_input = st.text_area("Enter text:", "Type or paste your text here.")
if file is not None:
    text_input += extract_text_from_docx(file)
st.subheader("Document Content:")
st.write(text_input)
if st.button("Extract Bigrams"):
    bigrams_result = extract_bigrams(text_input)
    st.subheader("Bigrams:")
    st.write(bigrams_result)

import streamlit as st
import nltk
from nltk import bigrams, word_tokenize
nltk.download('punkt', download_dir='.')
def extract_bigrams(text):
    words = word_tokenize(text)
    bigram_list = list(bigrams(words))
    return bigram_list
st.title("Bigram Extractor")
st.text("Made by Moneeb Ahmad with Lil Love ❤️")
text_input = st.text_area("Enter text:", "Type or paste your text here.")

if st.button("Extract Bigrams"):
    bigrams_result = extract_bigrams(text_input)
    st.subheader("Bigrams:")
    st.write(bigrams_result)


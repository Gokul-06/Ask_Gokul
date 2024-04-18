import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.image('/Users/gokul/Desktop/Believe/Projects/langchain/Main/images/glb.jpg', caption='Ask your fav TA')
btn = st.button("Create Questions")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])







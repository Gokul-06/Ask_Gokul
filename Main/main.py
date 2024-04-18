import streamlit as st
from Test import get_few_shot_db_chain

st.image('/Users/gokul/Desktop/Believe/Projects/langchain/Main/images/Staples_logo_PNG5.png', caption='Business is  Human')

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)







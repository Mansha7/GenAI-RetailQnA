from langchain_helper import get_few_shot_db_chain

import streamlit as st

st.title("AtliQ T shirts: Database QnA")

qs= st.text_input("Question: ")
if qs:
    chain = get_few_shot_db_chain()
    ans = chain.run(qs)
    st.header("Answer:")
    st.write(ans)
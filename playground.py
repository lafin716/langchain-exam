from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st

load_dotenv()
llm = ChatOpenAI()

st.title("AI 시인")
content = st.text_input("시의 주제를 입력해주세요")

if st.button('시 만들기'):
  with st.spinner('잠시만 기다려주세요...'):
    result = llm.invoke(content + "에 대한 시를 써줘")
    st.write(result.content)

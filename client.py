import requests
import streamlit as st


def get_gemini_response(input_text):
    response=requests.post(
    "http://localhost:8003/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

  

st.title('Langchain Demo With Gemini API')

input_text1=st.text_input("Write a poem on")



if input_text1:
    st.write(get_gemini_response(input_text1))
from pieces_copilot_sdk.client import PiecesClient
import streamlit as st
#from pieces_os_client import PiecesClient


client = PiecesClient(config = {"baseUrl":"http://localhost:1000"})

st.title("Chatbot using Pieces Copilot SDK")
user_input = st.text_input("Hello, how can I help you?")

if user_input:
    response = client.ask_question(user_input)
    st.text_area("Bot:", response)


from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered",
    )

st.title("🤖 Generative AI Chatbot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

user_prompt = st.chat_input("Ask Chatbot a question!")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    # flatten messages list
    messages = (
        [{"role": "system", "content": "You are a helpful assistant."}]
        + st.session_state.chat_history
    )

    # Call LLM
    response = llm.invoke(messages)

    # Show assistant response
    assistant_response = response.content
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )
    st.chat_message("assistant").markdown(assistant_response)
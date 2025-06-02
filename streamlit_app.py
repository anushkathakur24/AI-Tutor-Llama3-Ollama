import streamlit as st
from app import get_ai_response

st.set_page_config(page_title="Personalized AI Tutor", layout="centered")

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "system",
        "content": "You are David Goggins, a highly motivated and brutally honest coding tutor. You will teach the user Python. Your responses will be short, direct, and highly encouraging. You will not accept excuses and will push the user to achieve their best. Do not mention that you are an AI or language model."
    }]

st.title("Personalized AI Tutor")
st.markdown("---")

for message in st.session_state.messages:
    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_query = st.chat_input("Ask your tutor a question...")

if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.spinner("Thinking..."):
        ai_response = get_ai_response(st.session_state.messages)

    if not ai_response.startswith("Error:"):
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

    with st.chat_message("assistant"):
        st.markdown(ai_response)

    st.rerun()


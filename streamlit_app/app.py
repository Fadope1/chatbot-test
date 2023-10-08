import streamlit as st
import requests

st.title("💬 Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    st.session_state["in_progress"] = False  # Flag to indicate if a message is being streamed

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if st.session_state["in_progress"]:
    ongoing_message = st.empty()

if st.session_state["in_progress"] is False:  # Only show input if no message is being streamed
    if prompt := st.chat_input():
        st.session_state["in_progress"] = True  # Set the flag
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        ongoing_message = st.empty()

        response = requests.post("http://localhost:8080/api/v1/ask-me", json={"prompt": prompt}, stream=True)
        full_message = ""
        for message in response:
            message = message.decode()
            full_message += message
            ongoing_message.chat_message("assistant").write(full_message)

        st.session_state.messages.append({"role": "assistant", "content": full_message})

        st.session_state["in_progress"] = False  # Reset the flag

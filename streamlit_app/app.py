# Imports
import streamlit as st
import requests
from threading import Thread

# Function to get API response and update Streamlit
def get_api_response(prompt, ongoing_message, in_progress_flag):
    try:
        # Make a POST request to the API with a timeout
        response = requests.post("http://localhost:8080/api/v1/ask-me", json={"prompt": prompt}, stream=True, timeout=10)
        response.raise_for_status()

        full_message = ""
        for message in response.iter_content():
            message = message.decode()
            full_message += message
            ongoing_message.chat_message("assistant").write(full_message)

        # Append the full assistant message to the session state
        st.session_state.messages.append({"role": "assistant", "content": full_message})
        st.session_state[in_progress_flag] = False  # Reset the flag
    except requests.RequestException as e:
        st.error(f"API error: {e}")
        st.session_state[in_progress_flag] = False  # Reset the flag

# Main App
st.title("💬 Chatbot")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    st.session_state["in_progress"] = False

# Display past chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Ongoing message container
ongoing_message = st.empty()

# Chat Input
if not st.session_state["in_progress"]:
    user_input = st.chat_input()
    if user_input:
        st.session_state["in_progress"] = True  # Set the flag
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # Display the spinner initially
        with st.spinner('Assistant is typing...'):
            # Run the API request in a separate thread
            thread = Thread(target=get_api_response, args=(user_input, ongoing_message, "in_progress"))
            thread.start()

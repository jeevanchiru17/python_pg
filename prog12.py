import re

import streamlit as st

# a) Dictionary of regex rules
rules = {
    r"goa": "Goa is a great choice for beaches!",
    r"flight": "You can check flight prices online.",
    r"budget": lambda: "Your budget is noted. I can help you plan.",
}


# b) Logic function to match input
def respond(msg):
    for pattern, reply in rules.items():
        if re.search(pattern, msg.lower()):
            return reply() if callable(reply) else reply
    return "Sorry, I didn't understand that."


# c) Initialize session_state for chat history & user data
if "history" not in st.session_state:
    st.session_state.history = []
if "user" not in st.session_state:
    st.session_state.user = "Guest"

st.title("Simple Streamlit Chatbot")

# d) Chat input + response display
user_input = st.chat_input("Say something...")
if user_input:
    bot_reply = respond(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", bot_reply))

# Display complete chat history
for sender, msg in st.session_state.history:
    st.write(f"**{sender}:** {msg}")

# Clear Chat button
if st.button("Clear Chat"):
    st.session_state.history = []
    st.experimental_rerun()

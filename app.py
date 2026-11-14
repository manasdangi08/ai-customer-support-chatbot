import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types

# .env file se API key load karne ke liye
load_dotenv()

# Page ki basic setting
st.set_page_config(page_title="AI Customer Support Bot", page_icon="💬", layout="centered")

st.title("💬 AI Customer Support Assistant")
st.caption("Ask anything about our products, pricing, shipping, or return policies!")

# Left Sidebar mein API Key dalne ka box
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password", value=os.getenv("GEMINI_API_KEY", ""))
    st.markdown("[Get your free Gemini API Key](https://aistudio.google.com/)")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Store ki knowledge_base.txt file read karne ka function
def load_knowledge_base():
    try:
        with open("knowledge_base.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Standard e-commerce store policies apply."

knowledge_data = load_knowledge_base()

# AI ko instructions dena ki use kaise baat karni hai
SYSTEM_PROMPT = f"""
You are a polite, helpful, and concise Customer Support AI Assistant.
Answer customer queries strictly based on the following store information:

{knowledge_data}

Rules:
1. Keep answers friendly, clear, and under 3-4 sentences unless detailed product info is asked.
2. Quote prices in Indian Rupees (₹).
3. If a customer asks something not mentioned in the store data, politely apologize and ask them to contact support@aurumstudio.in or call +91-9876543210.
4. Respond in the same language the user asks in (English or Hinglish).
"""

# Chat history yaad rakhne ke liye
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 👋 Welcome to Aurum & Silver Studio. How can I help you today?"}
    ]

# Purane messages screen par dikhana
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User ka naya sawal lena aur AI se jawab generate karna
if user_query := st.chat_input("Type your question here (e.g., What is the return policy?)..."):
    if not api_key:
        st.error("⚠️ Please enter your Gemini API Key in the sidebar to start chatting.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            try:
                client = genai.Client(
                    api_key=api_key,
                    http_options=types.HttpOptions(timeout=45000)  # 45-second timeout
                )
                
                chat_history = [
                    types.Content(
                        role="user" if msg["role"] == "user" else "model",
                        parts=[types.Part.from_text(text=msg["content"])]
                    )
                    for msg in st.session_state.messages
                ]

                # Reliable models list
                models_to_try = ["gemini-3.8-flash", "gemini-2.5-flash-lite", "gemini-2.5-pro"]
                bot_reply = None

                for model_name in models_to_try:
                    try:
                        response = client.models.generate_content(
                            model=model_name,
                            contents=chat_history,
                            config=types.GenerateContentConfig(
                                system_instruction=SYSTEM_PROMPT,
                                temperature=0.3,
                            )
                        )
                        bot_reply = response.text
                        break
                    except Exception as model_err:
                        err_str = str(model_err)
                        if any(code in err_str for code in ["503", "504", "404", "429", "DEADLINE", "timeout", "Timeout"]):
                            continue
                        else:
                            raise model_err

                if bot_reply:
                    st.markdown(bot_reply)
                    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                else:
                    st.error("Servers are busy right now. Please click 'Clear Chat History' in sidebar and try again.")

            except Exception as e:
                st.error(f"Error generating response: {e}")
# 💬 AI Customer Support Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

An intelligent, context-aware **AI Customer Support Chatbot** built using **Python**, **Streamlit**, and the **Google Gemini API**. Designed for e-commerce and retail businesses, it answers customer queries about product catalogs, pricing, shipping timelines, and store policies using a customizable knowledge base, while suggesting relevant follow-up questions after every response.

---

## ✨ Key Features

- **📚 Custom Knowledge Base (`knowledge_base.txt`):** Easily update store products, pricing, timings, and policies in plain text without touching the core application code.
- **💡 Smart Follow-Up Suggestions:** Automatically generates 3 clickable next-question prompts after every answer to guide customer interactions seamlessly.
- **🛡️ Strict Guardrails (Anti-Hallucination):** Strictly relies on provided store data and gracefully routes out-of-scope queries to human support contact channels.
- **⚡ Interactive & Clean UI:** Built with Streamlit featuring real-time chat bubbles, session state management, and one-click chat reset.
- **🔐 Secure API Key Handling:** Supports both `.env` environment variables and runtime sidebar input to keep credentials safe.

---

## 🛠️ Tech Stack

- **Programming Language:** Python 3.9+
- **Frontend Framework:** Streamlit
- **AI / LLM Engine:** Google GenAI SDK (`gemini-3.8-flash`)
- **Environment Management:** `python-dotenv`

---

## 📂 Project Structure

text
ai-customer-support-chatbot/
├── app.py                  # Main Streamlit chatbot application & LLM logic
├── knowledge_base.txt      # Store product catalog, pricing, and FAQ data
├── requirements.txt        # Python dependencies
├── .gitignore              # Excludes sensitive .env and cache files from Git
└── README.md               # Project documentation
🚀 Getting Started (Local Setup)
1. Clone the Repository
Bash
git clone [https://github.com/yourusername/ai-customer-support-chatbot.git](https://github.com/yourusername/ai-customer-support-chatbot.git)
cd ai-customer-support-chatbot
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure Environment Variables (Optional)
Create a .env file in the root directory and add your Google Gemini API key:

Code snippet
GEMINI_API_KEY=your_gemini_api_key_here
(Alternatively, you can enter your API key directly in the app's sidebar after launching).

4. Run the Application
Bash
streamlit run app.py
The application will open automatically in your default web browser at http://localhost:8501.

🧪 Sample Queries to Test
"Show me your jewelry catalog and prices."

"What is your return and exchange policy?"

"How long does shipping take, and is Cash on Delivery available?"

"Do you sell laptops?" (Tests out-of-scope fallback handling)

🔮 Future Enhancements
[ ] Add PDF/CSV upload support for dynamic knowledge base ingestion (RAG).

[ ] Integrate order tracking lookup via database/API connection.

[ ] Add multi-language toggle (English / Hindi / Hinglish).

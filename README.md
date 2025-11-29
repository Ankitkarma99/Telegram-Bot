# **AI Telegram Chatbot (Groq + Llama 3.3)**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot_API-blue)](https://core.telegram.org/bots)
[![Groq LLM](https://img.shields.io/badge/Groq-Llama_3.3_70B-orange)](https://groq.com)
[![LangChain](https://img.shields.io/badge/LangChain-Framework-yellow)](https://python.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 **Project Overview**

This project is an **AI-powered Telegram Chatbot** that uses **Groq's Llama 3.3 (70B)** model through LangChain to deliver extremely fast, intelligent responses inside Telegram.

✔️ Super-fast inference powered by Groq
✔️ Simple and clean architecture
✔️ ChatGPT-like conversational experience
✔️ Completely customizable

---

## 📁 **Project Structure**

```
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ **How It Works**

1. User sends a message to the Telegram bot
2. Bot receives it through Telegram Bot API
3. Message is forwarded to **Groq Llama 3.3 (70B)** model
4. LLM generates a response
5. Bot replies instantly in Telegram

---

## 🛠️ **Installation & Setup**

### **1️⃣ Clone the Repository**

```bash
git clone <your-repo-url>
cd <project-folder>
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Create `.env` File**

```
TELEGRAM_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

### **4️⃣ Run the Bot**

```bash
python app.py
```

Your Telegram bot will go live instantly 🎉

---

## 🧠 **LLM Model Used**

* **Groq Llama 3.3 – 70B Versatile**
* Temperature: `0.7`
* Framework: **LangChain + ChatGroq**

Groq enables ultra-low latency responses for real-time chatbot interactions.

---

## 🔐 **Environment Variables**

| Variable           | Description              |
| ------------------ | ------------------------ |
| **TELEGRAM_TOKEN** | Bot token from BotFather |
| **GROQ_API_KEY**   | API key from Groq Cloud  |

---

## 📜 **License**

This project is licensed under the **MIT License**.

---

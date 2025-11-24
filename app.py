from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"

llm = ChatGroq(model_name=GROQ_MODEL, api_key=GROQ_API_KEY, temperature=0.7)

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    try:
        llm_response = llm.invoke(user_input)
        output = llm_response.content  # Directly use .content
    except Exception as e:
        output = f"error: {str(e)}"

    await update.message.reply_text(output)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))
    app.run_polling()
import os
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram import Update
from google.genai import Client

load_dotenv()

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_TOKEN")

client = Client(api_key=GEMINI_KEY)

# CHAT MODEL
chat = client.chats.create(model="models/gemini-2.5-flash")

def reply(update: Update, context: CallbackContext):
    user_text = update.message.text

    try:
        resp = chat.send_message(user_text)
        bot_reply = resp.text
    except Exception as e:
        bot_reply = f"Xatolik: {e}"

    update.message.reply_text(bot_reply)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))
    updater.start_polling()
    updater.idle()

if name == "main":
    main()
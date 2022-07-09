from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, filters, ApplicationBuilder
from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# functions


async def hello(update, context):
    await update.message.reply_text("Hi welcome to GoGreen!")

# Building the bot
bot = ApplicationBuilder().token(BOT_TOKEN).build()

# Add handlers
bot.add_handler(CommandHandler("hello", hello))
bot.run_polling()

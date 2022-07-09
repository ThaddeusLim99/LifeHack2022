from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, filters, ApplicationBuilder
from dotenv import load_dotenv
import json
import os
import requests
import logic, loc

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# functions
async def hello(update, context):
    await update.message.reply_text("Hi welcome to GoGreen!")

async def bin(update, context):
    # reply nearest bin location
    user_location = update.message.location
    lat, long = logic.findNearestBin(loc.LOCATIONS, user_location.latitude, user_location.longitude)
    await update.message.reply_location(latitude=lat, longitude=long)

# Building the bot
bot = ApplicationBuilder().token(BOT_TOKEN).build()

# Add handlers
bot.add_handler(CommandHandler("hello", hello))
bot.add_handler(MessageHandler(filters.LOCATION, bin))
bot.run_polling()

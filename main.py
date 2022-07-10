from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, filters, ApplicationBuilder
from dotenv import load_dotenv
import json
import os
import requests
import logic
import loc

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# functions


async def hello(update, context):
    keyboard = [
        [InlineKeyboardButton(
            "Learn more about recycling!", callback_data="learn")],
        [InlineKeyboardButton(
            "Find nearest recycling bin", callback_data="find")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Hi welcome to RecycleMe! What would you like to do?", reply_markup=reply_markup)


async def learnMore(update, context):
    keyboard = [
        [InlineKeyboardButton(
            "Paper", callback_data="paper"
        ),
            InlineKeyboardButton(
            "Plastic", callback_data="plastic"
        )],
        [InlineKeyboardButton(
            "Metal", callback_data="metal"
        ),
            InlineKeyboardButton(
            "Glass", callback_data="glass"
        )],
        [InlineKeyboardButton(
            "Others", callback_data="others"
        ), InlineKeyboardButton(
            "go to NEA", url=('https://www.towardszerowaste.gov.sg/recycle/what-to-recycle/')
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("What would you like to recycle?", reply_markup=reply_markup)


# def helper(item):
#     return item["canRecycle"]


# async def getPlastic(update, context):
#     with open('info.json', 'r') as info_db:
#         info = json.load(info_db)
#     lst = None
#     if "plastic" in info:
#         plastic_info = info["plastic"]
#         lst = list(plastic_info.keys())
#     markup = types.ReplyKeyboardMarkup()
#     await update.callback_query.message.reply_text(lst, reply_markup=reply_markup)


async def reqLocation(update, context):
    await update.callback_query.message.edit_text("Please send us your current location via the attachment!")


async def handleBin(update, context):
    # reply nearest bin location
    user_location = update.message.location
    lat, long = logic.findNearestBin(
        loc.LOCATIONS, user_location.latitude, user_location.longitude)
    await update.message.reply_location(latitude=lat, longitude=long)

# Building the bot
bot = ApplicationBuilder().token(BOT_TOKEN).build()


# Add handlers
bot.add_handler(CommandHandler("hello", hello))
# bot.add_handler(CallbackQueryHandler(getPlastic, pattern="plastic"))
bot.add_handler(CallbackQueryHandler(reqLocation, pattern="find"))
bot.add_handler(CallbackQueryHandler(learnMore, pattern="learn"))
# bot.add_handler(CallbackQueryHandler(infoOptions))
bot.add_handler(MessageHandler(filters.LOCATION, handleBin))
bot.run_polling()

from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from logging import getLogger


import botTest.subbotton





config = load_config()
logger = getLogger(__name__)


def do_start(bot: Bot, update: Update):
    bot.send_message(
            chat_id = update.message.chat_id,
            text = "Привет"
        )







@debug_requests
def otvet(bot: Bot, update: Update):
    text = update.message.text
    bot.send_message(
            chat_id = update.message.chat_id,
            text = text,
            reply_markup = get_base_inline_keyboard(),
       )
    







def main ():
    bot = Bot(
        token = '1368846578:AAGo02K0y5gncP4-9bzHyH4J8UBeKFnhbuY'
        )
    updater = Updater(
        bot = bot
        )

    start_handler = CommandHandler("Start", do_start)
    message_handler = MessageHandler(Filters.text, otvet)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)



    updater.start_polling()
    updater.idle()

if __name__== '__main__':
    main()


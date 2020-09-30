from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

from botTest.main import *






CALLBBACK_BUTTON_DOC = "https://sites.google.com/edi.md/instructions/%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-%D1%81%D0%BA%D0%BB%D0%B0%D0%B4/%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D1%8B?authuser=0"
CALLBBACK_BUTTON_SPR = "https://sites.google.com/edi.md/instructions/%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-%D1%81%D0%BA%D0%BB%D0%B0%D0%B4/%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8"
CALLBBACK_BUTTON_SVD = "https://servicedesk.edi.md/"

TITLES = {
    CALLBBACK_BUTTON_DOC: "Документы",
    CALLBBACK_BUTTON_SPR: "Справочники",\
    CALLBBACK_BUTTON_SVD: "Создать заявку",
    }



def get_base_inline_keyboard():
    """ 
    получить клавиатуру при запуске
    """

    keyboard = [

        [
            [
                InlineKeyboardButton(TITLES[CALLBBACK_BUTTON_DOC], callback_data = CALLBBACK_BUTTON_DOC),
                InlineKeyboardButton(TITLES[CALLBBACK_BUTTON_STR], callback_data = CALLBBACK_BUTTON_SPR),
            ],
            [
                InlineKeyboardButton(TITLES[CALLBBACK_BUTTON_SVD],callback_data = CALLBBACK_BUTTON_SVD),
            ],
        ]
]
    return InlineKeyboardMarkup(keyboard)

def keyboard_callback_handler(bot: Bot, udate: Update):
    # оьработка всех кнопок

    query = update.callback_query
    data = query.data
    now = datetime.datetime.now()

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == CALLBBACK_BUTTON_DOC:
        text = "Ссылка на докумены"
        query.edit_message_text(
            text = text,

            )
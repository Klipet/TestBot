from telegram import KeyboardButton, ReplyKeyboardMarkup





BUTTON1_DOCUMENT = "Документы"
BUTTON2_SPRAVOCNIC = "Справочник"



def get_base_reply_keybord():
    keyboard = [
            [
             KeyboardButton(BUTTON1_DOCUMENT),
             KeyboardButton(BUTTON1_DOCUMENT), 
            ]
        ]
    return ReplyKeyboardMarkup(
            keyboard = keyboard,
            resize_keyboard = True,
        )


from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                            InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup( keyboard = [[KeyboardButton(text = 'Send a text to process')],
                                    [KeyboardButton(text = 'Process the current chat')]], 
                                    resize_keyboard = True,
                                    input_field_placeholder = 'Select an option')
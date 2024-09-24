from aiogram import types


# две клавиатуры которые имеются у пользователя

def rep_keb_n():
    buttons = [[types.KeyboardButton(text = '/start'), types.KeyboardButton(text='/help'), types.KeyboardButton(text='/addschedule'),types.KeyboardButton(text='/schedule')],
               [types.KeyboardButton(text='/allschedule'),types.KeyboardButton(text='/delschedule'), types.KeyboardButton(text='/addschedule+time')]]
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def key_day():
    butt = [[types.KeyboardButton(text = '/Monday'), types.KeyboardButton(text='/Tuesday'), types.KeyboardButton(text='/Wednesday')],
            [types.KeyboardButton(text = '/Thursday'), types.KeyboardButton(text='/Friday'), types.KeyboardButton(text='/Saturday')],
            [types.KeyboardButton(text = '/Sunday')]]
    return types.ReplyKeyboardMarkup(keyboard=butt, resize_keyboard= True)
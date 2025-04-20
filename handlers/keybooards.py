from aiogram import types


# две клавиатуры которые имеются у пользователя

# def rep_keb_n():
#     buttons = [[types.KeyboardButton(text = '/start'), types.KeyboardButton(text='/help'), types.KeyboardButton(text='/addschedule'),types.KeyboardButton(text='/schedule')],
#                [types.KeyboardButton(text='/allschedule'),types.KeyboardButton(text='/delschedule'), types.KeyboardButton(text='/addscheduletime'), types.KeyboardButton(text='/time_change')]]
#     return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def key_day_e():
    buttons = [[types.KeyboardButton(text = 'Monday'), types.KeyboardButton(text='Tuesday'), types.KeyboardButton(text='Wednesday')],
            [types.KeyboardButton(text = 'Thursday'), types.KeyboardButton(text='Friday'), types.KeyboardButton(text='Saturday')],
            [types.KeyboardButton(text = 'Sunday')]]
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard= True)

def kebn():
    butto = [[types.KeyboardButton(text = '/start'), types.KeyboardButton(text='/help')],
             [types.KeyboardButton(text='/work_schedule')],[types.KeyboardButton(text='/watch_schedule')], 
             [types.KeyboardButton(text='/Template')]]
    return types.ReplyKeyboardMarkup(keyboard=butto, resize_keyboard=True)


def kebad():
    butto = [[types.KeyboardButton(text='/add_schedule'),types.KeyboardButton(text='/add_schedule_file'),
              types.KeyboardButton(text='/add_time')],
              [ types.KeyboardButton(text='/time_change'), types.KeyboardButton(text='/change_train') ,types.KeyboardButton(text='/del_schedule')],
              [types.KeyboardButton(text='/back')]]
    return types.ReplyKeyboardMarkup(keyboard=butto, resize_keyboard=True)

def kebv():
    butto = [[types.KeyboardButton(text='/all_schedule'), types.KeyboardButton(text='/schedule_ned')],[types.KeyboardButton(text='/back')]]
    return types.ReplyKeyboardMarkup(keyboard=butto, resize_keyboard=True)
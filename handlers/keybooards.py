from aiogram import types

from .nazv_kom import *

# две клавиатуры которые имеются у пользователя

def rep_keb_n():
    buttons = [[types.KeyboardButton(text = '/start'), types.KeyboardButton(text='/help'), types.KeyboardButton(text='/addschedule'),types.KeyboardButton(text='/schedule')],
               [types.KeyboardButton(text='/allschedule'),types.KeyboardButton(text='/delschedule'), types.KeyboardButton(text='/addscheduletime'), types.KeyboardButton(text='/time_change')]]
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


def key_day_e():
    buttons = [[types.KeyboardButton(text = 'Monday'), types.KeyboardButton(text='Tuesday'), types.KeyboardButton(text='Wednesday')],
            [types.KeyboardButton(text = 'Thursday'), types.KeyboardButton(text='Friday'), types.KeyboardButton(text='Saturday')],
            [types.KeyboardButton(text = 'Sunday')]]
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard= True)

def kebn():
    butto = [[types.KeyboardButton(text = '/start'), types.KeyboardButton(text='/help')],
             [types.KeyboardButton(text='/work_schedule')],[types.KeyboardButton(text='/watch_schedule')], 
             [types.KeyboardButton(text='/Template')],[types.KeyboardButton(text='/raschot')],[types.KeyboardButton(text="/train")]]
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


# def key_day_e():
#     buttons = [[types.KeyboardButton(text = 'Monday'), types.KeyboardButton(text='Tuesday'), types.KeyboardButton(text='Wednesday')],
#             [types.KeyboardButton(text = 'Thursday'), types.KeyboardButton(text='Friday'), types.KeyboardButton(text='Saturday')],
#             [types.KeyboardButton(text = 'Sunday')]]
#     return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard= True)

# def kebn():
#     butto = [[types.KeyboardButton(text = '/start'), types.KeyboardButton(text=b_help)],
#              [types.KeyboardButton(text=b_change)],[types.KeyboardButton(text=b_watch)], 
#              [types.KeyboardButton(text=b_template)],[types.KeyboardButton(text=b_kallor)],[types.KeyboardButton(text=b_training)]]
#     return types.ReplyKeyboardMarkup(keyboard=butto, resize_keyboard=True)


# def kebad():
#     butto = [[types.KeyboardButton(text=b_sched_add),types.KeyboardButton(text=b_add_file),
#               types.KeyboardButton(text=b_time_add)],
#               [ types.KeyboardButton(text=b_time_change), types.KeyboardButton(text=b_change_train) ,types.KeyboardButton(text=b_del_week)],
#               [types.KeyboardButton(text=b_back)]]
#     return types.ReplyKeyboardMarkup(keyboard=butto, resize_keyboard=True)

# def kebv():
#     butto = [[types.KeyboardButton(text=b_all_sched), types.KeyboardButton(text=b_sched_ned)],[types.KeyboardButton(text='/back')]]
#     return types.ReplyKeyboardMarkup(keyboard=butto, resize_keyboard=True)
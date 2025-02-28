from fun_db import *
from datetime import datetime
import pytz


print(get_train_day('1120554354', 1, 1))
spis = [(0,0,0), (1,0,0),(6,0,0),(0,0,0),(6,0,0),(0,0,0)]
for j in spis:

    dday = j[0]# Порядковый номер дня недели для отправки
    
    chass = int(j[1])  # Часы

    minu = int(j[2])  # Минуты
        
        
    if chass == 0 and minu == 0:
        if dday == 0:
            obn_ned()
            obnul()
            
        else:
            obnul()
        print(get_data())
            
    else:
        data = get_data()
        
        for i in data:
            print(i)
            if i[-1] == 1 and i[2] != 0:
                vr = i[4 + dday].split(':')
                chass1 = int(vr[0])  # Часы и минуты для конкретного человека
                minu1 = int(vr[1])
                if chass1 == chass and minu1 == minu:
                    rasp = get_train_day(i[1], i[3], dday)
                    
                    ism_na_nul(str(i[1])) 



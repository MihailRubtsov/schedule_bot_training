import sqlite3 as sq
import datetime


#Функция добавление в БД
def add_sched(id, mo, tu, we, th, fr, sa, su):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched_2 (id_tel, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, prov)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (id, mo, tu, we, th, fr, sa, su, 1))


# добавление в БД с временем отправки в каждый день

def add_sched_time(id, mo, tu, we, th, fr, sa, su, mot, tut, wet, tht, frt, sat, sut):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched_2 (id_tel, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday_t, Tuesday_t, Wednesday_t, Thursday_t, Friday_t, Saturday_t, Sunday_t, prov)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (id, mo, tu, we, th, fr, sa, su, mot, tut, wet, tht, frt, sat, sut, 1))



#функция присылает что нужно делать в конкретный день для каждого пользователя
def dat_tren(day, day_t):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT id_tel, {day}, {day_t} FROM user_sched_2 WHERE prov == 1""")
        res = cur.fetchall()
        return res

# присылает недельный план для пользователя
def watc_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM user_sched_2 WHERE id_tel = {id}
""")
        res = cur.fetchone ()
        return res

#человек может посмотреть свое рассписание в конкретный день
def watc_sched_day(id, day):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT {day} FROM user_sched_2 WHERE id_tel = {id}
""")
        res = cur.fetchone()[0]
        return res

# удаление рассписания
def del_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""DELETE FROM user_sched_2 WHERE id_tel = {id}
""")
    
# проверка есть ли план тренировок у пользователя
def prov_in(id):
    pr = False
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT id_tel FROM user_sched_2
""")
        res = cur.fetchall()
    
    for i in res:
        if int(i[0]) == int(id):
            pr = True
    return pr



#  функция проверки времени у пользователя чтобы не было проблем при отправке
def prov_time(time):
    pr = True
    try:
        a = time.split(':')
        h = int(a[0])
        m = int(a[1])
        if h < 0 or h > 24:
            pr = False
        if m < 0 or m > 60:
            pr = False
    except:
        pr = False
    return pr

def prov_dayy(mess):
    dayss = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if mess in dayss: return True
    return False
    


#добавление времени пользователю
def add_time_user(id, ddaay, ttiime):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            UPDATE user_sched_2 
            SET {}_t = ? 
            WHERE id_tel = ?
        """.format(ddaay), (ttiime, id))


#замена рассписания пользователю
def che_rasp_user(id, ddaay, rasp):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            UPDATE user_sched_2 
            SET {} = ? 
            WHERE id_tel = ?
        """.format(ddaay), (rasp, id))
    

# команда админа позволяет у всех пользователей поменять значение было отправлено расписание или нет
def obnul():
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""UPDATE user_sched_2 SET prov = 1""")


# команда которая ровно в 00:00 обнуляет всем проверку
def ism_na_nul(id_p):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""UPDATE user_sched_2 SET prov = 0 WHERE id_tel = {id_p}""")





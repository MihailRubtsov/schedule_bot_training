import sqlite3 as sq
import datetime


#Функция добавление в БД
def sozd_prof(idd):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched_2 (id_tel, kol_ned, prov)
            VALUES (?, ?, ?)
        """, (idd,0, 2))


def prov_in(id):
    pr = False
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT id_tel FROM user_sched_2
""")
        res = cur.fetchall()
    
    for i in res:
        if str(i[0]) == str(id):
            pr = True
    return pr



def kol_nedel(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT kol_ned FROM user_sched_2 WHERE id_tel == {str(id)}
""")
        res = cur.fetchall()
    return int(res[0][0])


def nom_nedel(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT nom_ned FROM user_sched_2 WHERE id_tel == {str(id)}
""")
        res = cur.fetchall()
    
    return res[0]








def add_sched(idd, rasp):
    kol = int(kol_nedel(idd))
    if kol < 5:
    
        with sq.connect('user_train1.db') as con:
            cur = con.cursor()
            cur.execute(f"""
            UPDATE user_sched_2 SET kol_ned = {kol + 1} WHERE id_tel = {idd}
        """)
            
            cur.execute(f"""
            UPDATE user_sched_2 SET ned_{str(kol + 1)} = '{rasp}' WHERE id_tel = {idd}
        """)
            
            cur.execute(f"""
            UPDATE user_sched_2 SET nom_ned = {1} WHERE id_tel = {idd}
        """)
    else:
        return 'Error'

def kol_ned(idd):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""
            SELECT kol_ned FROM user_sched_2 WHERE id_tel = {idd}
           
        """)
        res = cur.fetchone()[0]
        return int(res)


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
    




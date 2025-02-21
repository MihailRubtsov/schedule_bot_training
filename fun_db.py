import sqlite3 as sq
import datetime


def sozd_prof(idd): # создает профиль пользователя
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched_2 (id_tel, kol_ned, nom_ned, prov)
            VALUES (?, ?, ?, ?)
        """, (idd,0, 1,2))


def prov_in(id): # проверка есть ли пользователь
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



def kol_nedel(id): #количество недель пользователя
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT kol_ned FROM user_sched_2 WHERE id_tel == {str(id)}
""")
        res = cur.fetchall()
    return int(res[0][0])


def nom_nedel(id): # присылает номер недели на которой сейчас пользователь
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT nom_ned FROM user_sched_2 WHERE id_tel == {str(id)}
""")
        res = cur.fetchall()
    
    return res[0]








def add_sched(idd, rasp): # добавление недели
    kol = int(kol_nedel(idd))
    if kol < 5:
        with sq.connect('user_train1.db') as con:
            cur = con.cursor()
            cur.execute(f"""
            INSERT INTO  user_training (id_tel, train, nom_ned) VALUES (?, ?, ?)
        """, (idd, rasp, kol_nedel(idd) + 1))
        
        with sq.connect('user_train1.db') as con:
            cur = con.cursor()
            cur.execute(f"""
            UPDATE user_sched_2 
            SET kol_ned= {kol_nedel(idd) + 1}
            WHERE id_tel = {idd}
        """)
    else:
        return 'Error'


def add_time_p(idd, mot, tut, wet, tht, frt, sat, sut): #добавление времени во сколько отправлять пользователю
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""
            UPDATE user_sched_2 SET Monday_t = ?, Tuesday_t = ?, Wednesday_t = ?, Thursday_t = ?, Friday_t = ?, Saturday_t = ?, Sunday_t = ? WHERE id_tel = {str(idd)}
        """, (mot, tut, wet, tht, frt, sat, sut))


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



def add_time_user(id, ddaay, ttiime):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            UPDATE user_sched_2 
            SET {}_t = ? 
            WHERE id_tel = ?
        """.format(ddaay), (ttiime, id))


def prov_dayy(mess):
    dayss = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if mess in dayss: return True
    return False
# добавление в БД с временем отправки в каждый день


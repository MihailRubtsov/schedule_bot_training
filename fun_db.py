import sqlite3 as sq
import datetime


#Функция добавление в БД
def sozd_prof(idd):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched_2 (id_tel, kol_ned, nom_ned, prov)
            VALUES (?, ?, ?, ?)
        """, (idd,0, 1,2))


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


def add_time(idd, mot, tut, wet, tht, frt, sat, sut):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""
            UPDATE user_sched_2 SET Monday_0 = ?, Tuesday_1 = ?, Wednesday_2 = ?, Thursday_3 = ?, Friday_4 = ?, Saturday_5 = ?, Sunday_6 = ? WHERE id_tel = {str(idd)}
        """, (mot, tut, wet, tht, frt, sat, sut))






# добавление в БД с временем отправки в каждый день


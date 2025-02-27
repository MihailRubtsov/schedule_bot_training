import sqlite3 as sq
import datetime


def sozd_prof(idd): # создает профиль пользователя
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched_2 (id_tel, kol_ned, nom_ned, prov)
            VALUES (?, ?, ?, ?)
        """, (idd,0, 1,2))


def prov_time(time):#проверка коректности времени
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


def kol_nedel(id): #количество недель пользователя
    try:
        with sq.connect('user_train1.db') as con:
            cur = con.cursor()
            cur.execute(f"""SELECT kol_ned FROM user_sched_2 WHERE id_tel == {str(id)}
""")
            res = cur.fetchall()
        return int(res[0][0])
    except:
        return 0



def prov_in(id): # проверка есть ли пользователь
    if kol_nedel(id) != 0:
        return True
    return False


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


def add_time_user(id, ddaay, ttiime): #замена времени в конкретный день
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""UPDATE user_sched_2 SET {}_t = ? WHERE id_tel = ? """.format(ddaay), (ttiime, id))


def che_rasp_user(id, ned, rasp): #замена рассписания пользователю
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""UPDATE user_training SET train = ? WHERE id_tel = ? AND nom_ned = {}""".format(ned), (rasp, id))


def prov_dayy(mess):
    dayss = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if mess in dayss: return True
    return False


def del_sched(id): # удаление последней тренировки
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""DELETE FROM user_training WHERE id_tel = {id} AND nom_ned = {kol_nedel(id)}
""")
    with sq.connect('user_train1.db') as con:
            cur = con.cursor()
            cur.execute(f"""
            UPDATE user_sched_2 
            SET kol_ned= {kol_nedel(id) - 1}
            WHERE id_tel = {id}
        """)


def watc_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM user_sched_2 WHERE id_tel = {id}
""")
        res = cur.fetchone ()
        return res


def watc_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM user_training WHERE id_tel = {id}
""")
        res = cur.fetchall()
        soob = f'кол-во недель - {len(res)}.'

        k = 1
        for i in res:
            dni = i[2].split('@#@')
            mn = f'\n\n№{k}\n\nMonday:{dni[0]}\n\nTuesday:{dni[1]}\n\nWednesday:{dni[2]}\n\nThursday:{dni[3]}\n\nFriday:{dni[4]}\n\nSaturday:{dni[5]}\n\nSanday:{dni[6]}'
            soob += mn
            k +=1
        return soob


def watch_ned(id, nom):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM user_training WHERE id_tel = {id} AND nom_ned = {int(nom)}""")
        res = cur.fetchone()
        dni = res[2].split('@#@')
        mn = f'Ваша тренировочная неделя.\nMonday:{dni[0]}\n\nTuesday:{dni[1]}\n\nWednesday:{dni[2]}\n\nThursday:{dni[3]}\n\nFriday:{dni[4]}\n\nSaturday:{dni[5]}\n\nSanday:{dni[6]}'
        return mn


def work_with_file(name):
    with open(name) as file:
        f = file.readlines()
    stro = ''.join(f[1:])
    stro = stro.replace('\n', '@')
    stro = stro[:-2]
    stro = stro[7:]
    spis = ['Monday(',')@Tuesday(',')@Wednesday(',')@Thursday(',')@Friday(',')@Saturday(',')@Sunday(']
    for i in spis:
        stro = stro.replace(i, '#')
    spis_rasp = stro.split('#')
    raspis = f'{spis_rasp[0]}@#@{spis_rasp[0]}@#@{spis_rasp[0]}@#@{spis_rasp[0]}@#@{spis_rasp[0]}@#@{spis_rasp[0]}@#@{spis_rasp[0]}'
    return raspis



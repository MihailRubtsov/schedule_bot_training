import sqlite3 as sq
import datetime


#Функция добавление в БД
def add_sched(id, mo, tu, we, th, fr, sa, su):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched (id_tel, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (id, mo, tu, we, th, fr, sa, su))



#функция присылает что нужно делать в конкретный день для каждого пользователя
def dat_tren(day):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT id_tel, {day} FROM user_sched""")
        res = cur.fetchall()
        return res

# присылает недельный план для пользователя
def watc_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM user_sched WHERE id_tel = {id}
""")
        res = cur.fetchone ()
        return res

#человек может посмотреть свое рассписание в конкретный день
def watc_sched_day(id, day):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT {day} FROM user_sched WHERE id_tel = {id}
""")
        res = cur.fetchone()[0]
        return res

# удаление рассписания
def del_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""DELETE FROM user_sched WHERE id_tel = {id}
""")
    
# проверка есть ли план тренировок у пользователя
def prov_in(id):
    pr = False
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT id_tel FROM user_sched
""")
        res = cur.fetchall()
    
    for i in res:
        if int(i[0]) == int(id):
            pr = True
    return pr
        

import sqlite3 as sq

# подключение к бд

# with sq.connect('user_train1.db') as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE user_sched(user_id INTEGER PRIMARY KEY AUTOINCREMENT, id_tel INTEGER, 
#                 Monday TEXT, 
#                 Tuesday TEXT,
#                 Wednesday TEXT,
#                 Thursday TEXT,
#                 Friday TEXT,
#                 Saturday TEXT,
#                 Sunday TEXT)
# """)

def add_sched(id, mo, tu, we, th, fr, sa, su):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            INSERT INTO user_sched (id_tel, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (id, mo, tu, we, th, fr, sa, su))

def watc_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM user_sched WHERE id_tel = {id}
""")
        res = cur.fetchone ()
        return res


def del_sched(id):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute(f"""DELETE FROM user_sched WHERE id_tel = {id}
""")
    


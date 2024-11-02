import sqlite3 as sq
with sq.connect('user_train1.db') as con:
   cur = con.cursor()
   cur.execute("""CREATE TABLE user_sched_2(user_id INTEGER PRIMARY KEY AUTOINCREMENT ,id_tel TEXT,
                Monday TEXT,
                Tuesday TEXT,
                Wednesday TEXT,
                Thursday TEXT,
                Friday TEXT,
                Saturday TEXT,
                Sunday TEXT,
                Monday_t TEXT,
                Tuesday_t TEXT,
                Wednesday_t TEXT,
                Thursday_t TEXT,
                Friday_t TEXT,
                Saturday_t TEXT,
                Sunday_t TEXT,
               prov INTEGER)""")

# with sq.connect('user_train1.db') as con:
#    cur = con.cursor()
#    cur.execute("""
#             INSERT INTO user_sched_2 (id_tel, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday_t, Tuesday_t, Wednesday_t, Thursday_t, Friday_t, Saturday_t, Sunday_t, prov)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#         """, ('1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',1))
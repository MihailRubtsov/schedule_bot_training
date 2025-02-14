import sqlite3 as sq
# with sq.connect('user_train1.db') as con:
#    cur = con.cursor()
#    cur.execute("""CREATE TABLE user_sched_2(user_id INTEGER PRIMARY KEY AUTOINCREMENT ,id_tel TEXT,
#                 kol_ned TEXT,
#                 nom_ned TEXT,
#                 ned_1 TEXT,
#                 ned_2 TEXT,
#                 ned_3 TEXT,
#                 ned_4 TEXT,
#                 ned_5 TEXT,
#                prov INTEGER)""")

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
#             INSERT INTO user_sched_2 (id_tel, kol_ned, nom_ned, ned_1, ned_2, ned_3, ned_4, ned_5, prov)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? )
#         """, ('1','1','1','1','1','1','1','1',1))
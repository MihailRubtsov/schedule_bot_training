import sqlite3 as sq
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


print(prov_in(1120554354))
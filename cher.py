import sqlite3 as sq

def add_time_user(id, ddaay, ttiime):
    with sq.connect('user_train1.db') as con:
        cur = con.cursor()
        cur.execute("""
            UPDATE user_sched_2 
            SET {}_t = ? 
            WHERE id_tel = ?
        """.format(ddaay), (ttiime, id))

add_time_user('1120554354', 'Monday', '12:30')
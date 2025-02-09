import sqlite3


def save_result(name, score):
    con = sqlite3.connect("rating_bd")
    cur = con.cursor()
    cur.execute("""SELECT EXISTS(
    SELECT *
    FROM rating
    WHERE name = ?
    LIMIT 1)""", (name,))
    flag = cur.fetchone()
    if flag[0]:
        cur.execute("""UPDATE rating SET score = ? WHERE name = ?""", (score, name))
    else:
        cur.execute("""INSERT INTO rating (name, score) VALUES (?, ?)""", (name, score))
    con.commit()
    con.close()

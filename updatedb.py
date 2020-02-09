def updater(uid, amount):
    import sqlite3
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    c.execute('UPDATE Users SET remaining=? WHERE userid=?',(amount, uid))
    conn.commit()
    conn.close()

def inserter(uid, amount):
    import sqlite3
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Users WHERE userid=?',(uid,))
    tmp = c.fetchall()
    if tmp==[]:
        c.execute('INSERT INTO Users VALUES(NULL, ?,?)',(uid,amount))
    else:
        c.execute('SELECT remaining FROM Users WHERE userid=?',(uid,))
        resp=int(c.fetchall()[0][0])
        ins = resp + amount
        c.execute('UPDATE Users SET remaining=? WHERE userid=?',(ins, uid))
    conn.commit()
    conn.close()

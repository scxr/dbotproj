def read(tbl,srchval, srchcon):
    import sqlite3
    statement = "SELECT * FROM %s WHERE %s = %s" % (tbl,srchcon,srchval)
    conn = sqlite3.connect('main.db')
    c= conn.cursor()
    c.execute(statement)
    resp = c.fetchall()
    conn.commit()
    conn.close()
    return resp
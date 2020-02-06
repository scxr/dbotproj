def delete(srchval):
    import sqlite3
    statement = "DELETE FROM Claimables WHERE CODE = %s" % (srchval)
    conn = sqlite3.connect('main.db')
    c= conn.cursor()
    c.execute(statement)
    conn.commit()
    conn.close()

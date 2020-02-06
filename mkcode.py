import sqlite3, os, random
def make(n):
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    for i in range(0,n):
        code = str(int.from_bytes(os.urandom(32), byteorder='big'))
        val = random.randint(0,100)
        print(code)
        c.execute('INSERT INTO Claimables VALUES(NULL, ?, ?)',(code,val))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    make(10)
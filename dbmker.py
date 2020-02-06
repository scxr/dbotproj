import sqlite3
def usermk():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Users (id integer PRIMARY KEY,userid integer, remaining integer)')
    conn.commit()
    conn.close()

def codemk():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Claimables(id integer PRIMARY KEY,CODE string)')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    todo = input()
    if todo == "1":
        usermk()
    else:
        codemk()
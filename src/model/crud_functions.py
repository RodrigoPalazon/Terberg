import sqlite3

def add_one(name, subcategory, price):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    c.execute("INSERT INTO listings VALUES (?,?,?)", (name, subcategory, price))
    conn.commit()
    conn.close()

def add_many(list):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    c.executemany("INSERT INTO listings VALUES (?,?,?)", (list))
    conn.commit()
    conn.close()

def delete_one(table, id):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    c.execute("DELETE FROM {} WHERE rowid={}".format(table,id))
    conn.commit()
    conn.close()

def email_lookup(email):
    conn = sqlite3.connect('terber.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM listings WHERE email={}".format(email))
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()

def print_table(table):
    conn = sqlite3.connect('terberg.db')
    c = conn.cursor()
    # Query the Database
    c.execute("SELECT rowid,* FROM {}".format(table))
    items =c.fetchall()
    # print(items)

    for item in items:
        # print(str(item[0]) + " " + item[1] + "| \t" + item[2] + " " + str(item[3]))
        print(item)
    # print(c.fetchone()[0])

    # Commit changes and close connection
    conn.commit()
    conn.close()

def join_table(table):
    conn = sqlite3.connect('..\..\database\terberg.db')
    c = conn.cursor()
    # Query the Database
    c.execute("SELECT rowid,* FROM {}".format(table))
    items =c.fetchall()
    # print(items)

    for item in items:
        # print(str(item[0]) + " " + item[1] + "| \t" + item[2] + " " + str(item[3]))
        print(item)
    # print(c.fetchone()[0])

    # Commit changes and close connection
    conn.commit()
    conn.close()
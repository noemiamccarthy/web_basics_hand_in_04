import sqlite3 as sql

def insertUser(username,password):
    con = sql.connect("accounts.db")
    cur = con.cursor()
    cur.execute("INSERT INTO accounts (username,password) VALUES (?,?)", (username,password))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("accounts.db")
	cur = con.cursor()
	cur.execute("SELECT username, password FROM accounts")
	users = cur.fetchall()
	con.close()
	return users
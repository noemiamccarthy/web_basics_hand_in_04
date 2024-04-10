# import sqlite3 as sql

# connection = sqlite3.connect('accounts.db')

# with open('schema.sql') as f:
#       connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO accounts (username, email,password) VALUES (?,?,?)", ('username', 'email', 'password'))

# connection.commit()
# connection.close()

# def insertUser(username,password):
#     con = sql.connect("accounts.db")
#     cur = con.cursor()
    
#     con.commit()
#     con.close()

# def retrieveUsers():
# 	con = sql.connect("accounts.db")
# 	cur = con.cursor()
# 	cur.execute("SELECT username, password FROM accounts")
# 	users = cur.fetchall()
# 	con.close()
# 	return users
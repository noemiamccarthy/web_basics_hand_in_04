from crypt import methods
from logging import Handler
import symtable
from flask import Flask, render_template, request
import sqlite3 
from sqlite3 import Error
import models as handler

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/trips')
def trips():
    return render_template('trips.html')

@app.route('/register', methods=['GET', 'POST'])  # Allow both GET and POST requests
def register():
    if request.method == 'POST':
        username = request.args.get('username')  # Access form data using request.form
        email = request.args.get('email')
        password = request.args.get('password')
        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO accounts (username, email, password) VALUES (?, ?, ?)", (username, email, password))
                con.commit()
                print("User registered successfully!")
                # return render_template('profile.html', username=username, email=email)  # Pass username and email for display (consider hiding password)
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error registering user: {error}")
            # Handle database error (e.g., display error message)
            pass
    else:
        return render_template('register.html')
    
def get_connection():
    """Establishes a connection to the database."""
    try:
        con = sqlite3.connect('accounts.db')
        return con
    except Error as error:
        print(f"Error connecting to database: {error}")
        return None

# @app.route('/templates/register.html', ['POST'])
# def register_user(con, username, email, password,*args):
#     if request.method=='POST':
#         username = request.args.get('username')
#         email= request.args.get('email')
#         password = request.args.get('password')
#         try:
#             cursorObj = con.cursor()
#             cursorObj.execute("CREATE TABLE IF NOT EXISTS accounts (id integer PRIMARY KEY, username text, email text, password text)")
#             cursorObj = con.commit()
#             return render_template('profile.html', username=username, email=email, password=password)
        
@app.route('/templates/profile.html', methods=['POST'])
def profile():
    if request.method=='POST':
        username = request.args.get('username')
        password = request.args.get('password')
        Handler.insertUser(username, password)
        users = Handler.retrieveUsers()
        return render_template('profile.html', users=users)
    else:
        return render_template('index.html')
        
def sql_connection():
    try:
        con = sqlite3.connect('accounts.db')
        return con
    except Error as error:
        print(f"Error connecting to database: {error}")
        return None


# con = sql_connection()
# if con:
#     symtable(con)

if __name__ == "__main__":
    app.run(debug=True)
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

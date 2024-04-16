from crypt import methods
from logging import Handler
import symtable
from flask import Flask, render_template, make_response, url_for, flash, request, redirect, Response
import sqlite3 
from sqlite3 import Error

app = Flask(__name__)

def get_connection():
    """Establishes a connection to the database."""
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error as error:
        print(f"Error connecting to database: {error}")
        return None

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#### html routes

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
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reviews')
    reviews = c.fetchall()
    conn.close()

    def int_to_stars(value):
        return '⭐' * int(value)

    return render_template('trips.html', reviews=reviews, int_to_stars=int_to_stars)




### logic routes

@app.route('/register', methods=['GET','POST'])  
def register():
    if request.method== "POST":
        username = request.form.get('username')  # Access form data using request.form
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO accounts (username, email, password) VALUES (?, ?, ?)", (username, email, password))
                con.commit()
                print("User (dummy) logged in successfully!")
                newid = cursor.lastrowid # the new number from insert, the database generates the new number automatically

                # How to do cookies in flask https://stackoverflow.com/questions/46661083/how-to-set-cookie-in-python-flask
                response = make_response(redirect("/profile"))
                response.set_cookie("profile", str(newid))
                
                return response
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass
    else:
        return render_template("register.html")

@app.route('/login', methods=['GET','POST'])  
def login():
    if request.method== "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("SELECT id FROM accounts WHERE email= (?) AND password= (?)", (email, password))
                con.commit()
                user=cursor.fetchone()
                print("User selected successfully")
                
                id=user[0]
                # How to do cookies in flask https://stackoverflow.com/questions/46661083/how-to-set-cookie-in-python-flask
                response = make_response(redirect("/profile"))
                response.set_cookie("profile", str(id))
                
                return response
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass
    else:
        return render_template("login.html")

@app.route('/profile', methods=['GET'])
def profile():
        profileid = request.cookies.get("profile")
        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("SELECT username FROM accounts WHERE id =" + profileid)
                con.commit()
                user=cursor.fetchone()
                print("User selected successfully")

                username=user[0]
                return render_template("profile.html", username=username)
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass

@app.route('/profile/<id>', methods=['GET'])
def profileid(id):
        profileid = id
        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("SELECT username FROM accounts WHERE id =" + profileid)
                con.commit()
                user=cursor.fetchone()
                print("User selected successfully")

                username=user[0]
                return render_template("profile.html", username=username)
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass
        
@app.route('/reviews', methods=['GET'])
def getreviews():
        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                reviews = cursor.execute("SELECT Name, Description, Rating FROM reviews")
                con.commit()
                print("Ratings selected successfully!")
                print(reviews)
                return reviews
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass

@app.route('/reviews', methods=['POST'])
def reviews():
    if request.method== "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        rating = request.form.get("rating")
        votes = 0

        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("INSERT INTO reviews (Name, Description, Rating, Votes) VALUES (?, ?, ?,?)", (name, description, rating, votes))
                con.commit()
                print("Rating created successfully!")
                return redirect('/trips') 
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass

@app.route('/reviews/<reviewid>/delete', methods=['POST']) # to delete or change a review I need the id
def deletereview(reviewid):
    if request.method== "POST":

        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("DELETE FROM reviews WHERE id = " + reviewid)
                con.commit()
                print("Rating deleted successfully!")
                return redirect("/trips")
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass

@app.route('/reviews/<reviewid>/upvote', methods=['POST']) # to delete or change a review I need the id
def upvotereview(reviewid):
    if request.method== "POST":

        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("UPDATE reviews SET votes = votes + 1 WHERE id = "+reviewid)
                con.commit()
                print("Rating upvoted successfully!")
                return redirect("/trips")
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass        

@app.route('/reviews/<reviewid>/downvote', methods=['POST']) 
def downvotereview(reviewid):
    if request.method== "POST":

        try:
            con = get_connection()
            if con:
                cursor = con.cursor()
                cursor.execute("UPDATE reviews SET votes = votes - 1 WHERE id = "+reviewid)
                con.commit()
                print("Rating downvoted successfully!")
                return redirect("/trips")
            else:
                # Handle connection error (e.g., display error message)
                pass
        except Error as error:
            print(f"Error logging user: {error}")
            # Handle database error (e.g., display error message)
            pass        

if __name__ == "__main__":
    # app.run(debug=True)
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")

from flask import Flask, render_template, request
import mysql, _mysql_connector
import cgi

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates/index.html')
def index():
    return render_template('index.html')

@app.route('/templates/about.html')
def about():
    return render_template('about.html')

@app.route('/templates/register.html')
def register():
    return render_template('register.html')
import mysql.connector

# Database connection details (replace with your own)
db_host = "Noemia-Lindiwes-MacBook-Pro.local"
db_user = "your_username"
db_password = "your_password"
db_name = "user.sql"

def connect_db():
  """Connects to the MySQL database"""
  try:
    mydb = mysql.connector.connect(
      host=db_host,
      user=db_user,
      password=db_password,
      database=db_name
    )
    return mydb
  except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    return None

@app.route('/register', method=['GET' , 'POST'])
def register_user(username, password, email):
  """Registers a new user in the database"""
  mydb = connect_db()
  if mydb:
    mycursor = mydb.cursor()
    sql = "INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'test', '0ef15de6149819f2d10fc25b8c994b574245f193', 'test@test.com');"
    val = (id, username, password)
    try:
      mycursor.execute(sql, val)
      mydb.commit()
      print("User registered successfully!")
    except mysql.connector.Error as err:
      print("Error registering user:", err)
    finally:
      mydb.close()
    return redirect(url_for('/profile.html'))
  

# @app.route('/profile', methods = ["GET"])
# def profile():
#     if request.method == "GET":
#         # getting input with name = fname in HTML form
#         first_name = request.args.get("fname")
#         # getting input with name = sname in HTML form 
#         sur_name = request.args.get("sname")

#         print(first_name)
#         print(sur_name)
 
#         return render_template('profile.html', fname=first_name, sname=sur_name)


if __name__ == "__main__":
    app.run(debug=True)
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
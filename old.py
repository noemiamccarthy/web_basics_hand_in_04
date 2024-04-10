# from crypt import methods
# from flask import Flask, render_template, request
# import sqlite3
# import pathlib

# app = Flask(__name__)

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/templates/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/templates/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/templates/register.html')
# def register():
#     return render_template('register.html')

  

# # @app.route('/profile', methods = ["GET"])
# # def profile():
# #     if request.method == "GET":
# #         # getting input with name = fname in HTML form
# #         first_name = request.args.get("fname")
# #         # getting input with name = sname in HTML form 
# #         sur_name = request.args.get("sname")

# #         print(first_name)
# #         print(sur_name)
 
# #         return render_template('profile.html', fname=first_name, sname=sur_name)


# if __name__ == "__main__":
#     app.run(debug=True)
    
# local_db_path = "./users.db"

# conn = methods(local_db_path)
# cursor = conn.cursor()

# cursor.execute("""SELECT * from ACCOUNTS""")
# result = cursor.fetchall()

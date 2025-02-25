from flask import Flask, render_template
app = Flask(__name__) # create the application instance :)

# @app.route('/') # decorator drfines the request routeset FLASK_APP=marketting.py
# def hello():
#     return "<h1>Hello World</h1>"

# @app.route('/about/<username>')
# def about_page(username):
#     return f'<h1>this is the page of {username}</h1>' 
@app.route('/') 
@app.route('/home')
def home_page():
    return render_template('home.html')


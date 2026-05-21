from database import db, Todo
from flask import Flask, render_template, request, redirect, url_for
# Flask: main class, render_template for HTML file in index file, request: lets you see the data from server, redirect: to a diff URL
# url_for: for redirect

app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///todos.db"  #retrieving the db file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False #Not needed as we never track if the object was modified or not and it's by default on (not of critical priority)
db.init_app(app)

with app.app_context():
    db.create_all()    #Step to give SQLAlchemy access to flask and this also checks if it has a db(if not, it creates one...)

@app.route("/")
def index():
    todos= Todo.query.order_by(Todo.created.desc()).all()
   return render_templates("index.html", todos= todos)
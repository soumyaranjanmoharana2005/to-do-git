from database import db, Todo
from flask import Flask, render_template, request, redirect, url_for
# Flask: main class, render_template for HTML file in index file, request: lets you see the data from server, redirect: to a diff URL
# url_for: for redirect

app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///todos.db"  #retrieving the db file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False #Desired as we never track if the object was modified or not and it's by default on (not of critical priority) 
db.init_app(app)

with app.app_context():
    db.create_all()    #Step to give SQLAlchemy access to flask and this also checks if it has a db(if not, it creates one...)

@app.route("/")
def index():
    todos= Todo.query.order_by(Todo.created.desc()).all()
    return render_template("index.html", todos= todos)

@app.route("/add", methods= ["POST"])
def add_todo():
    user_input= request.form.get("task")
    if bool(user_input)== True:
        todo= Todo(task=user_input)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/toggle/<int:id>", methods= ["POST"])
def toggle_todo(id):
    todo=Todo.query.get(id)
    if bool(todo)==True:
        todo.done= 1- todo.done
        db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods= ["POST"])
def delete_todo(id):
    todo= Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__== "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
# Flask: main class, render_template for HTML file in index file, request: que te dejá ver the data from server, redirect: to a diff URL
# url_for: for redirect

from database import get_connection, init_db#database_fn

app= Flask(__name__)  #app object

@app.before_request
def initialize():
    init_db()

@app.route("/")  #Database import to index.html initialization
def index():
    conn= get_connection()
    todos= conn.execute("SELECT * FROM todos ORDER BY created DESC").fetchall()  #Cuidado! the string in Parentheses is SQL
    conn.close()  #closing it 
    return render_template("index.html", todos= todos)

@app.route("/add", methods= ["POST"])
def add_todo():
    task= request.form.get("task") #getting the task from the post, j'crois
    if bool(task)== True:
        conn= get_connection()
        conn.execute("INSERT INTO todos(task) VALUES (?)", (task,))  # (task,) is a single tuple and «?» is there for SQL to treat it as string...(j'crois)
        conn.commit()
        conn.close()
    return redirect(url_for("index"))

@app.route("/toggle/<int:id>", methods= ["POST"])
def toggle_todo(id):   #É the toggle
    conn= get_connection()
    conn.execute("UPDATE todos SET done = 1 - done WHERE id = ?", (id,)) # without WHERE, all would have toggled
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>", methods= ["POST"])
def delete_todo(id):
    conn= get_connection()
    conn.execute("DELETE FROM todos where id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

if __name__== "__main__":
    app.run(debug=True)




import sqlite3

def get_connection():
    conn=sqlite3.connect(todos.db)    #N'oublie pas, it's for connection
    conn.row_factory= sqlite3.Row     #row_factory is an attribute and we are setting that attributes to a value


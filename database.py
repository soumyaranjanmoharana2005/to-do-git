import sqlite3

def get_connection():
    conn=sqlite3.connect("todos.db")    #N'oublie pas, it's for connection
    conn.row_factory= sqlite3.Row      #row_factory is an attribute and we are setting that attributes to a value
    return conn
def init_db():
    conn= get_connection()
    conn.execute("""
         CREATE TABLE IF NOT EXISTS todos (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            task    TEXT NOT NULL,
            done    INTEGER DEFAULT 0,
            created TEXT DEFAULT (datetime('now'))
           )
        """)
    conn.commit()
    conn.close()
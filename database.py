from flask_sqalchemy import SQLAlchemy
from datetime import datetime
    
db =SQLAlchemy()

class Todo(db.model):
    __tablename__= "Todos"
    id = db.Column(db.integer, primary_key= True, autoincrement=True)
    task= db.Column(db.String, nullable=False) #to avoid blank tasks
    done= db.Column(db.Integer, default=0)
    created= db.Column(db.DateTime, default= datetime.timezone.utc) #datetime.utcnow is deprecated and now has been replaced by datetime.timezone.utc
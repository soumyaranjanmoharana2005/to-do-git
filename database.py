from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
    
db =SQLAlchemy()

class Todo(db.Model):
    __tablename__= "Todos"
    id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    task= db.Column(db.String, nullable=False) #to avoid blank tasks
    done= db.Column(db.Integer, default=0)
    created= db.Column(db.DateTime, default= lambda:datetime.now(timezone.utc)) #datetime.utcnow is deprecated and now has been replaced by datetime.timezone.utc
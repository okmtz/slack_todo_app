from datetime import datetime
from app.database import db


class Task(db.Model):

    __tablename__ = 'tasks'

    def serialize(self):
        return {
            'id': self.id, 
            'title': self.title,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
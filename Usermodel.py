from __init__ import *


class flaskapiuser(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(50),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120),  nullable=False)

    def __repr__(self):
        return f"user('{self.user_name}','{self.email}')"



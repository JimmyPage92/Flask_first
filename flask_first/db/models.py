from . import DB


class Users(DB.Model):
    id_ = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(20))
    surname = DB.Column(DB.String(20))
    sex = DB.Column(DB.String(6))  # pole płeć
    age = DB.Column(DB.Integer())
    position = DB.Column(DB.String())



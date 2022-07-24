from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
#formularz

class UserForm(FlaskForm):
    name = StringField(label="User Name", validators=[DataRequired(), Length(min=3)])
    surname = StringField(label="Surname", validators=[DataRequired(), Length(min=3)])
    sex = StringField(label="Sex",validators=[DataRequired(), Length(min=4, max=6)])#male or female
    age = IntegerField(label="Age",validators=[DataRequired(),Length(min=1, max=3)])
    position = StringField(label= "Position",validators=[DataRequired(),Length(min=1, max=40)])
    submit = SubmitField("Create new user!") #przycisk do potwierdzenia

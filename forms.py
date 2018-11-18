from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class Addform(FlaskForm):
    name=StringField("enter name of Puppy")
    submit=SubmitField("Submit")
class Delform(FlaskForm):
    id=StringField("Enter id which you want to delete")
    submit=SubmitField("Submit")

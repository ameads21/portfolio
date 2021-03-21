from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
    firstname = StringField("First Name", validators=[
                            InputRequired(message="This input is required!")])

    lastname = StringField("Last Name", validators=[
        InputRequired(message="This input is required!")])

    email = EmailField("Email", validators=[
                       InputRequired("This input is required!"), Email("This field requires a valid email address!")])

    position = StringField("Position Title", validators=[
        InputRequired(message="This input is required!")])

    comments = TextAreaField("Comments")

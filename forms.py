from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class ProfileForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    age = StringField("Age", validators=[DataRequired()])
    gender = SelectField("Gender", choices=["Male", "Female"])
    hobby = StringField("Hobbies", validators=[DataRequired()])
    submit = SubmitField("save")

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Repeat password", validators=[DataRequired(), EqualTo(password)])
    role = SelectField("Role ", choices=["Student", "Teacher"])
    grade = SelectField("Grade ", choices=["1", "2", "3", "4", "5", "6"])
    submit = SubmitField("Register")

class SearchForm(FlaskForm):
    search = StringField( render_kw={"placeholder":"Search name/email"})
    submit = SubmitField("Search", render_kw={"style":"display:none;"})

class DeleteForm(FlaskForm):
    delete = SubmitField("Delete", render_kw={"class":"btn btn-outline-danger"})
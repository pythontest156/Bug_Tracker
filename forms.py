# imports

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, TextField, SelectField
from wtforms.validators import DataRequired, Email
from flask_ckeditor import CKEditorField


# WTForm linked to Bug database
class AddBugForm(FlaskForm):
    bug_name = StringField("Project Name", validators=[DataRequired()])
    brief_desc = StringField("Brief Description", validators=[DataRequired()])
    full_desc = CKEditorField("Full Description", validators=[DataRequired()])

    choices = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    severity = SelectField("Severity (10 being very severe)", choices=choices, validators=[DataRequired()])
    time_to_fix = SelectField("Estimated Time to fix (10 being very quick)", choices=choices, validators=[DataRequired()])
    submit = SubmitField("Submit", render_kw={"class": "d-none d-sm-inline-block btn btn-sm btn-primary shadow-sm fas fa-sm text-white-50", "style": "width:100%;"})


# WTForm linked to User database
class RegisterForm(FlaskForm):
    name = StringField("", validators=[DataRequired()], render_kw={"placeholder": "Full Name", "class": "form-control"})
    email = StringField("", validators=[DataRequired(), Email()], render_kw={"placeholder": "Email Address", "class": "form-control"})
    password = PasswordField("", validators=[DataRequired()], render_kw={"placeholder": "Password", "class": "form-control"})
    submit = SubmitField("Register", render_kw={"class": "btn form-control btn-primary rounded submit px-3"})


# WTForm linked to User database
class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(), Email()], render_kw={"placeholder": "Email Address", "class": "form-control"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Password", "class": "form-control"})
    submit = SubmitField("Login", render_kw={"class": "btn form-control btn-primary rounded submit px-3"})


# WTForm linked to Comments database
class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

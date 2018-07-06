from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, Email, EqualTo, DataRequired, Length
from app.models import User # necessary for validators

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username): #if validate_THIS BIT matches a field, WTForms automatically uses it as an extra validator!
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# most flask extensions use a flask_<name> convention for their top level import symbol

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0,max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('That username is already taken')
                # THIS FUCKER AIN'T SHOWIN FIX THAT - fixed, secret key authenticator was outside the form iirc

class PostForm(FlaskForm):
    post = TextAreaField("What's on your mind?", validators=[DataRequired(),Length(min=1, max=140)])
    submit = SubmitField('Submit')
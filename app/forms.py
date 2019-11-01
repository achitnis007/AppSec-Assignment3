from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, UserLoginHistory, UserServiceHistory
import phonenumbers

class RegistrationForm(FlaskForm):
    username = StringField('Username', id='uname', validators=[DataRequired(), Length(min=2, max=20)])
    phone = StringField('Phone', id='2fa', validators=[DataRequired()])    
    password = PasswordField('Password', id='pword', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Entered user name is not available. Please choose a different name!')
    
    def validate_phone(form, field):
        if len(field.data) > 16:
            raise ValidationError('error - Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not phonenumbers.is_valid_number(input_number):
                raise ValidationError('error - Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1"+field.data)
            if not phonenumbers.is_valid_number(input_number):
                raise ValidationError('error - Invalid phone number.')
                
class LoginForm(FlaskForm):
    username = StringField('Username', id='uname', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', id='pword', validators=[DataRequired(), Length(min=8, max=20)])
    phone = StringField('Phone', id='2fa', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
    def validate_phone(form, field):
        if len(field.data) > 16:
            raise ValidationError('error - Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not phonenumbers.is_valid_number(input_number):
                raise ValidationError('error - Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+1"+field.data)
            if not phonenumbers.is_valid_number(input_number):
                raise ValidationError('error - Invalid phone number.')

class SpellCheckerForm(FlaskForm):
    input_content = TextAreaField('Input Text to Spellchecker Web App', id='inputtext', validators=[DataRequired()])
    output_content = TextAreaField('Output Text to Spellchecker Service', id='textout', render_kw={'readonly': True})
    misspelled_content = TextAreaField('Misspelled Words from Spellchecker Service', id='misspelled', render_kw={'readonly': True})    
    submit = SubmitField('Spell Check')
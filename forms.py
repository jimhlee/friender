"""Forms for Friender."""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length, InputRequired, Regexp, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PhotoForm(FlaskForm):
    ''' Form for uploading image file '''
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(["heic", "png", "jpg", "jpeg", "webp"], 'Images only!')
    ])


class CSRFProtection(FlaskForm):
    """CSRFProtection form, intentionally has no fields."""


class SignupForm(FlaskForm):
    """Form for adding users on signup."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    first_name = StringField(
        'First Name',
        validators=[DataRequired()],
    )

    last_name = StringField(
        'Last Name',
        validators=[DataRequired()],
    )

    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
    )

    zip_code = StringField(
        "ZIP Code",
        validators=[
            DataRequired(),
            Regexp(r'^\d{5}$', message="Invalid ZIP code. Must be 5 digits.")
        ]
    )

    password = PasswordField(
        'Password',
        validators=[Length(min=6)],
    )

    interests = TextAreaField(
        'Interests',
        validators=[DataRequired()]
    )

    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(["heic", "png", "jpg", "jpeg", "webp"], 'Images only!')
    ])

    friend_radius = IntegerField(
        "Friend Radius",
        validators=[
            DataRequired(),
            NumberRange(min=1, max=25,
                        message="Value must be between 1 and 25")
        ])

class ProfileEditForm(FlaskForm):
    """Form for editing a user profile."""

    first_name = StringField(
        'First Name',
        validators=[DataRequired()],
    )

    last_name = StringField(
        'First Name',
        validators=[DataRequired()],
    )

    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
    )

    image_url = StringField(
        '(Optional) Image URL',
    )

    zipcode = StringField(
        'Zipcode',
        validators=[DataRequired(), Length(min=5)]
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        'Username',
        validators=[DataRequired()],
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired()],
    )


class SwipeForm(FlaskForm):
    """Form for swiping"""

    left = SubmitField("Do not wish to Friend")
    right = SubmitField("Send Friend Request!")


class NewMessageForm(FlaskForm):
    """Form for adding new message"""

    content = TextAreaField(
        "Send a message!",
        validators=[DataRequired()]
    )

class ProfileEditForm(FlaskForm):
    """Form for editing a user profile."""

    first_name = StringField(
        'First Name',
        validators=[DataRequired()],
    )

    last_name = StringField(
        'First Name',
        validators=[DataRequired()],
    )

    email = StringField(
        'Email',
        validators=[DataRequired(), Email()],
    )

    interests = TextAreaField(
        'Interests',
        validators=[DataRequired()]
    )

    friend_radius = IntegerField(
        "Friend Radius"
    )
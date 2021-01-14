from flask_wtf import FlaskForm
from map.map import map
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class Shipping_Form(FlaskForm):
    sender = StringField('Sender', validators=[DataRequired()])
    recipient = StringField('Recipient', validators=[DataRequired()])
    origin = SelectField('Origin', choices=[tuple(
        (key, key)) for key in map.keys()], validators=[DataRequired()])
    destination = SelectField('Destination', choices=[tuple(
        (key, key)) for key in map.keys()], validators=[DataRequired()])
    express_shipping = BooleanField('Express Shipping' default=False)
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')

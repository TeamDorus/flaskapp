from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired, NumberRange



class NordvpnCountryForm(FlaskForm):
  country = SelectField('Country', validators=[DataRequired()])
  num = IntegerField('Aantal servers', default=10, validators=[DataRequired(), NumberRange(min=1)])
  show = SubmitField('Toon servers')


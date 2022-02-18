from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, SubmitField, ValidationError
from wtforms.validators import DataRequired



class GpxExportForm(FlaskForm):
  device = SelectField('Device', validators=[DataRequired()])
  startdate = DateField('Begin datum', format='%Y-%m-%d', validators=[DataRequired()])
  enddate = DateField('Eind datum', format='%Y-%m-%d', validators=[DataRequired()])
  show = SubmitField('Toon tracks')
  download = SubmitField('Download GPX')

  def validate_enddate(form, field):
    if field.data < form.startdate.data:
      raise ValidationError('Ligt voor de begin datum')




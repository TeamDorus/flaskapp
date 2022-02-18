from flask_wtf import FlaskForm
from wtforms import SubmitField



class ConfigGeneralForm(FlaskForm):
  test = SubmitField('Test')


class ConfigReceiverForm(FlaskForm):
  deviceOnline_Aan = SubmitField('Zet uit')
  deviceOffline_Aan = SubmitField('Zet uit')
  deviceUnknown_Aan = SubmitField('Zet uit')
  deviceMoving_Aan = SubmitField('Zet uit')
  deviceStopped_Aan = SubmitField('Zet uit')
  geofenceEnter_Aan = SubmitField('Zet uit')
  geofenceExit_Aan = SubmitField('Zet uit')
  deviceOnline_Uit = SubmitField('Zet aan')
  deviceOffline_Uit = SubmitField('Zet aan')
  deviceUnknown_Uit = SubmitField('Zet aan')
  deviceMoving_Uit = SubmitField('Zet aan')
  deviceStopped_Uit = SubmitField('Zet aan')
  geofenceEnter_Uit = SubmitField('Zet aan')
  geofenceExit_Uit = SubmitField('Zet aan')








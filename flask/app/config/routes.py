from flask import Blueprint, render_template, request, Response, flash
from sqlalchemy import exc
from app.config.forms import ConfigGeneralForm, ConfigReceiverForm
from app.tools.functions import send_telegram
from app import app, db
from app.config.models import TraccarEvent

config = Blueprint('config', __name__)



@config.route("/config/", methods=['GET','POST'])
def config_general():

    form = ConfigGeneralForm()

    if request.method == 'POST':
        send_telegram("WebApp: config test")
        flash('WebApp testbericht is verstuurd.', 'success')

    return render_template("config-general.html", active="Instellingen", active2="Algemeen", form=form, token=app.config['TELEGRAM_API_TOKEN'], chat=app.config['TELEGRAM_CHAT_ID'])



@config.route("/config/traccar/", methods=['GET','POST'])
def config_traccar():

    events = TraccarEvent.query.all()
    form = ConfigReceiverForm()

    if request.method == 'POST':

        for button in form.data:
            if form.data[button] == True:
                event_type = button[:-4]
                if button[-3:] == 'Aan':
                    optstr = 'de'
                    new_state = 'Uit'
                else:
                    optstr = ''
                    new_state = 'Aan'
                event = TraccarEvent.query.filter_by(type=event_type).first()
                event.status = new_state
                db.session.commit()
#                flash(f"Event receiver voor '{ event_type }' ge{ optstr }activeerd.", 'success')

    return render_template("config-traccar.html", active="Instellingen", active2="Traccar", events=events, form=form)






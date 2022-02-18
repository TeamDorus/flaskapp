from flask import Blueprint, render_template, request, Response
from app.traccar.forms import GpxExportForm
from app.traccar.functions import get_devices, get_track, generate_pointlist, generate_gpx
from app.config.models import TraccarEvent
from app.tools.functions import send_telegram
import folium
import pprint


traccar = Blueprint('traccar', __name__)


@traccar.route("/traccar/", methods=['GET','POST'])
def traccar_route():
    form = GpxExportForm()
    filename = ""
    device_list = get_devices()
    form.device.choices = device_list
    if request.method == 'POST':
      if form.validate_on_submit():
        # get track from Traccar server
        track = get_track(form.device.data, form.startdate.data, form.enddate.data)

        if form.show.data:
          # Toon track knop ingedrukt
          # show folium map met track
          point_list, centerpoint = generate_pointlist(track)
          f = folium.Figure(width=600, height=600)
          if len(point_list) == 0:
            centerpoint = (52.5 , 5.5)
          track_map = folium.Map(location=centerpoint, zoom_start=8).add_to(f)
          if len(point_list) > 0:
            folium.PolyLine(point_list, color='red', weight=5).add_to(track_map)
          return render_template("traccar.html", active="Traccar", form=form, map=track_map._repr_html_())

        else:
          # Download GPX knop ingedrukt
          # genereer gpx file van de track
          device_dict = dict(device_list)
          filename = f"{device_dict[int(form.device.data)]}_{form.startdate.data}_{form.enddate.data}.gpx"
          gpx_content = generate_gpx(track, device_dict[int(form.device.data)], form.startdate.data, form.enddate.data)
          return Response(gpx_content,
                       mimetype="text/gpx",
                       headers={"Content-Disposition":f"attachment;filename={filename}"})

    return render_template("traccar.html", active="Traccar", form=form)



@traccar.route("/traccar/event_recv/", methods=['GET','POST'])
def traccar_event_recv():

    event = request.json
    # pprint.pprint(event)
    event_type = event.get('event').get('type')
    device_name = event.get('device').get('name')
    event_config = TraccarEvent.query.filter_by(type=event_type).first()

    if event_config.status == 'Aan':
        if event_type == 'geofenceEnter':
            msg = f"Traccar: {device_name} entered zone {event.get('geofence').get('name')}"
        else:
            if event_type == 'geofenceExit':
                msg = f"Traccar: {device_name} left zone {event.get('geofence').get('name')}"
            else:
               msg = f"Traccar: {device_name} - {event_type}"
    else:
        if not event_config_state == 'Uit':
            msg = f"Traccar: {device_name} - unknown event: {event_type}"

    send_telegram(msg)

    return "OK"



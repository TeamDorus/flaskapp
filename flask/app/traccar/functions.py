import urllib.request, base64
import json
from datetime import datetime
from app import app


def get_devices():
  # api call
  userpass = f"{app.config['TRACCAR_API_USER']}:{app.config['TRACCAR_API_PASS']}"
  request_url = f"{app.config['TRACCAR_BASE_URL']}/api/devices"
  b64auth = base64.b64encode(userpass.encode()).decode()
  request = urllib.request.Request(request_url)
  request.add_header("Authorization", "Basic %s" % b64auth)
  result = urllib.request.urlopen(request)
  device_info = json.loads(result.read())
  # maak een lijst met voor ieder device een tuple (id, naam)
  device_list = []
  for dev in device_info:
    device_list.append( (dev['id'], dev['name']) )
  return device_list


def get_track(device_id, startdate, enddate):
  # api call
  userpass = f"{app.config['TRACCAR_API_USER']}:{app.config['TRACCAR_API_PASS']}"
  request_url = f"{app.config['TRACCAR_BASE_URL']}/api/reports/route?_dc=1619800977916&deviceId={device_id}&type=allEvents&from={startdate}T00%3A00%3A00%2B02%3A00&to={enddate}T23%3A59%3A59%2B02%3A00&daily=false&mail=false"
  b64auth = base64.b64encode(userpass.encode()).decode()
  request = urllib.request.Request(request_url)
  request.add_header("Authorization", "Basic %s" % b64auth)
  request.add_header("Accept", "application/json")
  result = urllib.request.urlopen(request)
  return json.loads(result.read())


def generate_pointlist(jsontrack):
  point_list = []
  minlat = 90
  maxlat = 0
  minlon = 180
  maxlon = -180
  for trackpoint in jsontrack:
    if trackpoint["valid"]:
      lat = trackpoint["latitude"]
      lon = trackpoint["longitude"]
      if lat > maxlat:
        maxlat = lat
      if lat < minlat:
        minlat = lat
      if lon > maxlon:
        maxlon = lon
      if lon < minlon:
        minlon = lon
      point_list.append( (lat, lon) )
  center = ( (minlat+maxlat)/2 , (minlon+maxlon)/2 )
  return point_list, center


def generate_gpx(points, devicename, startdate, enddate):
  # gpx generation

  # header
  gpx = '<?xml version="1.0" encoding="UTF-8" ?>' + "\n"
  gpx = gpx + '<gpx version="1.1" creator="Traccar exporter" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.topografix.com/GPX/1/1" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">' + "\n\n"

  # metadata
  gpx = gpx + "<metadata>\n"
  gpx = gpx + f'    <name>Traccar - {devicename}: {startdate} - {enddate}</name>\n'
  gpx = gpx + "</metadata>\n\n"

  # track
  gpx = gpx + f'<trk>\n<name>{devicename}: {startdate} - {enddate}</name>\n<trkseg>\n\n'
  for point in points:
    if point["valid"]:
      gpx = gpx + f'<trkpt lat="{point["latitude"]}" lon="{point["longitude"]}">\n'
      gpx = gpx + f'    <time>{point["deviceTime"].replace("+00:00", "")}Z</time>\n'
      gpx = gpx + '</trkpt>\n\n'

  # end
  gpx = gpx + '</trkseg>\n</trk>\n'
  gpx = gpx + '</gpx>\n'

  return gpx





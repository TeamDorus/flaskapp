import urllib.request
import json
from app import app


def get_country_dict():
	SERVER_JSON_URL = "https://api.nordvpn.com/v1/servers?limit=9999999"

	resp = urllib.request.urlopen(SERVER_JSON_URL)
	data = json.loads(resp.read().decode())

	country_dict = { d['locations'][0]['country']['name']:d['locations'][0]['country']['id'] for d in data }
	return country_dict


def get_server_info(country_id, num_servers):
	SERVER_JSON_URL = f"https://api.nordvpn.com/v1/servers/recommendations?&filters[servers_technologies][identifier]=wireguard_udp&filters[country_id]={country_id}&limit={num_servers}"

	resp = urllib.request.urlopen(SERVER_JSON_URL)
	data = json.loads(resp.read().decode())

	server_list = []
	for d in data:
		for t in d['technologies']:
			if t['metadata']:
				server_list.append ( {  'hostname': d['hostname'],
										'ipv4': d['station'],
										'pubkey': (t['metadata'][0]['value']),
										'city': d['locations'][0]['country']['city']['name'],
										'load': d['load']
									} )
	return server_list

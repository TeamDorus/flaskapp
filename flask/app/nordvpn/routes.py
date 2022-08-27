from flask import Blueprint, render_template, request, Response
from app.nordvpn.forms import NordvpnCountryForm
from app.nordvpn.functions import get_country_dict, get_server_info
#import pprint


nordvpn = Blueprint('nordvpn', __name__)


@nordvpn.route("/nordvpn/", methods=['GET','POST'])
def nordvpn_route():
    form = NordvpnCountryForm()
    country_dict = get_country_dict()
    countries = list(country_dict.keys())
    countries.sort()

    form.country.choices = countries
    if request.method == 'POST':
        if form.validate_on_submit():
            # get server info from NordVPN
            server_info = get_server_info(country_dict[form.country.data], form.num.data)

            return render_template("nordvpn.html", active="NordVPN", form=form, server_info=server_info)


    return render_template("nordvpn.html", active="NordVPN", form=form)

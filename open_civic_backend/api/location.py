import frappe
import requests
from frappe.utils import now
from open_civic_backend.api.common import custom_response

GIS_API = "https://locate.solveninja.org/api/gis-info"


@frappe.whitelist()
def new(latitude, longitude):
    """
    If lat & long already exist returns the existing location
    else create a new location and returns it
    """
    try:
        loc_data = new_location(latitude, longitude)
        return custom_response("", loc_data, 200)
    except Exception as e:
        frappe.db.rollback()
        return custom_response(str(e), None, 500, True)


def new_location(latitude, longitude):
    loc_name = frappe.db.exists(
        "Locations",
        {
            "latitude": latitude,
            "longitude": longitude,
        },
    )
    if loc_name:
        location = frappe.get_doc("Locations", loc_name)
    else:
        location = frappe.get_doc(
            {
                "doctype": "Locations",
                "latitude": latitude,
                "longitude": longitude
            }
        )
        get_gis_data(location)
        location.insert()
    return {
        "id": location.name,
        "timestamp": location.timestamp,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "address": location.address,
        "landmark": location.landmark,
        "pin_code": location.pin,
        "city": location.city,
        "state": location.state,
        "district": location.district,
        "ward": location.ward,
        "ward_no": location.ward_no,
        "assembly_constituency": location.assembly_constituency,
        "loksabha_constituency": location.loksabha_constituency,
        "village_name": location.village_name,
        "village_number": location.village_number,
        "hobli_name": location.hobli_name,
        "hobli_number": location.hobli_number,
        "taluka": location.taluka,
        "polzone": location.polzone,
        "grama_panchayath": location.grama_panchayath,
        "taluk_panchayath": location.taluk_panchayath,
        "rwa": location.rwa,
    }


def get_gis_data(self):
    """
    Get GIS data from the API
    """
    def clean_data(data):
        """Remove unwanted characters from data"""
        if data == "<Null>" or data.lower() == "null":
            return None
        return data

    self.timestamp = now()
    if not self.latitude or not self.longitude:
        return

    try:
        float(self.latitude)
        float(self.longitude)
    except ValueError:
        return

    data = {"lat": self.latitude, "lang": self.longitude}

    gis_keys = [
        "ward",
        "grama_panchayath",
        "assembly_constituency",
        "taluk_panchayath",
        "loksabha_constituency",
        "district",
        "ward_no",
        "polzonename",
        "village_name",
        "village_number",
        "rwa",
        "hobli_number",
        "hobli_name",
        "u_district",
        "u_state",
        "u_city",
    ]
    doctype_field_gis_key_map = {
        "u_district": "district",
        "u_state": "state",
        "u_city": "city",
        "polzonename": "polzone",
    }

    response = requests.post(url=GIS_API, data=data)
    response = response.json()
    for key in gis_keys:
        if key in response:
            data = clean_data(response[key])
            if key in doctype_field_gis_key_map:
                self.set(doctype_field_gis_key_map[key], data)
            else:
                self.set(key, data)

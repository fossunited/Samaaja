import frappe
import json
from open_civic_backend.api.common import custom_response

@frappe.whitelist()
def new():
    """
    If lat & long already exists returns the existing location
    else creates a new location and returns it
    """
    location_data = json.loads(frappe.request.data)
    try:
        loc_data = new_location(location_data)
        return custom_response(loc_data, 200)
    except Exception as e:
        frappe.db.rollback()
        return custom_response(str(e), None, 500, True)


def new_location(location_data):
    loc_name = None
    latitude = str(location_data.get("latitude"))
    longitude = str(location_data.get("longitude"))
    if latitude and longitude:
        loc_name = frappe.db.exists(
            "Locations",
            {
                "latitude": latitude,
                "longitude": longitude,
            },
        )
    if loc_name:
        location = frappe.get_doc("Locations", loc_name)
        location = location.as_dict()

        # Field to identify if the location is already created
        location["is_new"] = False
    else:
        location = frappe.get_doc(
            {
                "doctype": "Locations",
                **location_data,
            }
        )
        location.insert(ignore_permissions=True)
        location = location.as_dict()
        location["is_new"] = True
    return location

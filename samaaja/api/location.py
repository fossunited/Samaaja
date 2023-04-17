import frappe
import json
from samaaja.api.common import custom_response
from frappe.utils import flt


@frappe.whitelist()
def new():
    """
    If lat & long already exists returns the existing location
    else creates a new location and returns it
    TODO:: have a deduplicate logic.
    """
    location_data = json.loads(frappe.request.data)
    try:
        loc_data = new_location(location_data)
        return custom_response(loc_data, 200)
    except Exception as e:
        frappe.db.rollback()
        return custom_response(str(e), None, 500, True)


def new_location(location_data):
    """Common function to create new location"""

    # Set precision
    precision = 9
    latitude = flt(location_data.get("latitude"), precision)
    longitude = flt(location_data.get("longitude"), precision)

    loc_name = None
    if latitude and longitude:
        loc_name = frappe.db.exists(
            "Location",
            {
                "latitude": latitude,
                "longitude": longitude,
            },
        )
    if loc_name:
        location = frappe.get_doc("Location", loc_name)
        location = location.as_dict()

        # Field to identify if the location is already created
        location["is_new"] = False
    else:
        location = frappe.get_doc(
            {
                "doctype": "Location",
                **location_data,
            }
        )
        location.insert(ignore_permissions=True)
        location = location.as_dict()
        location["is_new"] = True
    return location

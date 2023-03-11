# Copyright (c) 2022, FOSSUnited and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from samaaja.api.location import new_location


class Events(Document):
    def before_insert(self):
        # if location is not available and lat long exists create new location
        if not self.location and self.latitude and self.longitude:
            location = new_location({"latitude": self.latitude, "longitude": self.longitude})
            self.location = location.get("name")

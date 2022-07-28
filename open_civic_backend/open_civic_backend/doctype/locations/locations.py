# Copyright (c) 2022, FOSSUnited and contributors
# For license information, please see license.txt
import json
from frappe.model.document import Document
from frappe.utils import now


class Locations(Document):

    # Empty geolocation with a Point
    geolocation_dict = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {"type": "Point", "coordinates": []},
            }
        ],
    }

    def before_save(self):
        self.timestamp = now()

        has_geolocation = False
        if self.geolocation:
            try:
                if len(json.loads(self.geolocation)["features"]) > 0:
                    has_geolocation = True
            except Exception:
                pass

        if has_geolocation:
            # Pick the first Geometry of type POINT
            # And use its latitude and longitude if form does not have them
            geolocation_data = json.loads(self.geolocation)
            for feature in geolocation_data["features"]:
                geometry = feature["geometry"]
                if "type" in geometry and geometry["type"] == "Point":
                    coordinates = geometry["coordinates"]
                    new_latitude = coordinates[1]
                    new_longitude = coordinates[0]
                    if not self.latitude or not self.longitude:
                        self.latitude = new_latitude
                        self.longitude = new_longitude

        elif self.latitude and self.longitude:
            # Only latitude and longitude are provided
            # Create a new Geometry with type Point
            self.geolocation_dict["features"][0]["geometry"]["coordinates"] = [
                self.longitude,
                self.latitude,
            ]
            self.geolocation = json.dumps(self.geolocation_dict)

# Add location


### POST [/api/method/samaaja.api.location.new](http://localfrappe.test:8000/api/method/samaaja.api.location.new)

* If latitude and longitude already exists, it will return the existing location data.

#### Request
```bash
curl -X POST -H "Content-Type: application/json" \
 -d '{"latitude":"12.233","longitude":"17.02323",
 "address": "JP Nagar 5th phase, Bengaluru",
 "city": "Bengaluru", "state": "Karnataka"}' \
 'http://localhost:8000/api/method/samaaja.api.location.new'
```

#### Response

```json
{
	"message": "",
	"status": "success",
	"data": {
		"name": "c8491aeee0",
		"owner": "Guest",
		"creation": "2022-07-28 23:10:06.489092",
		"modified": "2022-07-28 23:10:06.489092",
		"modified_by": "Guest",
		"parent": null,
		"parentfield": null,
		"parenttype": null,
		"idx": 0,
		"docstatus": 0,
		"geolocation": "{\"type\": \"FeatureCollection\", \"features\": [{\"type\": \"Feature\", \"properties\": {}, \"geometry\": {\"type\": \"Point\", \"coordinates\": [60, 23.232]}}]}",
		"latitude": 23.232,
		"longitude": 60,
		"description": null,
		"address": "JP Nagar 5th phase, Bengaluru",
		"landmark": null,
		"pin": null,
		"city": "Bengaluru",
		"locality": null,
		"state": "Karnataka",
		"district": null,
		"ward_name": null,
		"ward_no": null,
		"assembly_constituency": null,
		"loksabha_constituency": null,
		"village_name": null,
		"village_number": null,
		"hobli_name": null,
		"hobli_number": null,
		"taluka": null,
		"polzone": null,
		"grama_panchayath": null,
		"taluk_panchayath": null,
		"rwa": null,
		"doctype": "Locations",
		"is_new": true // This is a new location
	}
}
```
# Add location


### POST /api/method/civic_backend.civic_backend.api.location.new
* Add a new location with latitude and longitude (required).
* Other fields are automatically filled in by an external GIS service.
* If latitude and longitude already exists, it will return the existing location data.

#### Request
```bash
curl -X POST -H "Content-Type: application/json" \
 -d '{"latitude":"12.233","longitude":"17.02323"}' \
 'http://localhost:8000/api/method/civic_backend.civic_backend.api.location.new'
```

#### Response

```json
{
  "message": "",
  "status": "success",
  "data": {
    "id": "d6c1fd1bea",
    "timestamp": "2022-07-17 15:22:49.523191",
    "latitude": "12.9728341",
    "longitude": "77.6619917",
    "address": null,
    "landmark": null,
    "pin_code": null,
    "city": null,
    "state": "Karnataka",
    "district": "Bengaluru (Urban)",
    "ward": "New Tippasandra",
    "ward_no": "58",
    "assembly_constituency": "C.V. RamannNagar",
    "loksabha_constituency": "Bangalore Central",
    "village_name": "K.G.Byrasandra",
    "village_number": "2004090010",
    "hobli_name": "Marathahalli",
    "hobli_number": "200409",
    "taluka": null,
    "polzone": null,
    "grama_panchayath": null,
    "taluk_panchayath": "Bangalore-East",
    "rwa": null
  }
}

```
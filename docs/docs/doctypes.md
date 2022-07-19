# Available Doctypes / Tables


### Locations

| Frappe field     | Field type|                                                                                                                                     |
|-----------|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `latitude`    | `Data`     | Latitude of location |
| `longitude` | `Data`     | Longitude of location                                                                      |
| `address` | `Long text`     | Address of location|
| `landmark`  | `Data`      | Lankmark nearby                                                                                  |
| `pin`  | `Data` | Pincode |
| `city`   | `Data`   |  City / Town |
| `state`    | `Select`   | Drop down with all Indian states |
| `district`  | `Data`   | District            |
| `ward`   | `Data`     | Ward name                                                                                                                 |
| `ward_no`  | `Data`     | Ward number|
| `assembly_constituency`  | `Data`     | Assembly constituency |
| `loksabha_constituency`  | `Data`     | Loksabha constituency |
| `village_name`  | `Data`     | Village name|
| `village_number`  | `Data`     | Village number |
| `hobli_name`  | `Data`     | Hobli name |
| `hobli_number`  | `Data`     | Hobli number |
| `taluka`  | `Data`     | Taluka |
| `polzone`  | `Data`     | Polzone |
| `grama_panchayath`  | `Data`     | Gram panchayath |
| `taluk_panchayath`  | `Data`     | Taluk Panchayath |
| `rwa`  | `Data`     | Resident Welfare Association |


### Events
* Events represent any kind of event that can happen in the civic space.

  
| Frappe field     | Field type |                                                                                                                                     |
|--------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `title`    | `Data`     | Name of event |
| `event_type` | `Link`     | ID of event stored in `Event Types` doctype |
| `event_status`  | `Link` | ID of event status stored in `Event Status` doctype |
| `category`   | `Link`   | ID of event category stored in `Event Categories` doctype |
| `location`    | `Link`   | ID of location stored in `Locations` doctype |
| `source`  | `Link`     | ID of event source stored in `Event Source` doctype |
| `session_type` | `Select`     | Session type be either `Online` or `Offline` |
| `user`  | `Data`      | Email address of User who created the event |
| `description`  | `Long Text`   | Description of the event            |
| `file`   | `Attach`     | File / Image attachment                                                                                                                 |
| `url`  | `Data`     | Any relevant URL to the event |
| `authority`  | `Data`     | Name of authority involved |
| `engaged_govt`  | `Check`     | Government was involved or not |
| `impacted_people`  | `Data`     | Number of people impacted |
| `impacted_resources`  | `Data`     | Resources impacted |
| `times_follow_up`  | `Data`     | Times follow up was required |
| `feedback`  | `Long Text`     | Feedback on the event |
| `time_invested`  | `Data`     | Time invested for the event |


### Event Status

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `event_status`    | `Data`     | Status of event |


### Event Source

  
| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `event_source`    | `Data`     | Source of event |


### Event Types

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `event_type`    | `Data`     | Type of event |


### Event Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `category_name`    | `Data`     | Category of event |


### Event Sub Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `sub_category_name`    | `Data`     | Sub Category of event |


### Assets
* Assets are any kind of asset in the civic space.

| Frappe field     | Field type|                                                                                                                                     |
|--------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `asset_name`    | `Long Text`     | Name of asset |
| `user` | `Data`     | Email of user who reported the asset |
| `location` | `Link`     | ID of location stored in `Locations` doctype |
| `category`  | `Link`     | ID of asset category stored in `Asset Categories` doctype |
| `sub_category`  | `Link`     | ID of asset category stored in `Asset Sub Categories` doctype |
| `description`  | `Long Text`   | Description of the Asset            |
| `file`   | `Attach`     | File / Image attachment                                                                                                                 |
| `url`  | `Data`     | Any relevant URL to the event |
| `open_time`  | `Data`     | Opening time of the asset |
| `close_time`  | `Data`     | Close time of the asset |
| `rating`  | `Rating`     | Rating of the asset |
| `phone_number`  | `Data`     | Phone number of the asset |


### Asset Type

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `asset_type`    | `Data`     | Type of asset |


### Asset Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `category_name`    | `Data`     | Category of asset |


### Asset Sub Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `sub_category_name`    | `Data`     | Sub Category of asset |
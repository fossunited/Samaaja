# Available Doctypes / Tables


### Location

| Frappe field     | Field type|                                                                                                                                     |
|-----------|---------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `geolocation`    | `Geolocation`     | Map to select a point on map |
| `latitude`    | `Data`     | Latitude of location |
| `longitude` | `Data`     | Longitude of location                                                                      |
| `description` | `Long text`     | Description of the location |
| `address` | `Long text`     | Address of location|
| `landmark`  | `Data`      | Lankmark nearby                                                                                  |
| `pin`  | `Data` | Pincode |
| `city`   | `Data`   |  City / Town |
| `state`    | `Select`   | Drop down with all Indian states |
| `district`  | `Data`   | District            |
| `ward_name`   | `Data`     | Ward name                                                                                                                 |
| `ward_number`  | `Data`     | Ward number|
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
|-----------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `title`    | `Data`     | Name of event |
| `type` | `Link`     | ID of event stored in `Event Types` doctype |
| `status`  | `Link` | ID of event status stored in `Event Status` doctype |
| `category`   | `Link`   | ID of event category stored in `Event Categories` doctype |
| `subcategory`   | `Link`   | ID of event category stored in `Event Sub Categories` doctype |
| `attachment`  | `Attach`     | File attachment |
| `source`  | `Link`     | ID of event source stored in `Event Source` doctype |
| `user`  | `Data`      | Email address of User reporting the event |
| `location`    | `Link`   | ID of location stored in `Locations` doctype |
| `description`  | `Long Text`   | Description of the event            |
| `url`  | `Data`     | Any relevant URL to the event |
| `authority`  | `Data`     | Name of authority involved |
| `has_govt_engagement`  | `Check`     | Government was engaged or not |
| `impacted_entity_count` | `Data`     | Number of entities impacted |
| `impacted_entity_unit`  | `Data`     | ID stored in `Impacted Entity Units` doctype |
| `followup_count`  | `Data`     | Times follow up was required |
| `feedback`  | `Long Text`     | Feedback on the event |
| `rating`  | `Rating`     | Rating for the event |
| `time_invested`  | `Data`     | Time invested in the event |



### Event Status

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `status`    | `Data`     | Status of an event |


### Event Source

  
| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `source`    | `Data`     | Source of an event |


### Event Types

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `type`    | `Data`     | Type of an event |


### Event Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `category`    | `Data`     | Category of an event |


### Event Sub Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `subcategory`    | `Data`     | Sub Category of an event |


### Impacted Entity Units

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `unit`    | `Data`     | Units for impacted entity in an event |


### Assets
* Assets are any kind of asset in the civic space.

| Frappe field     | Field type|                                                                                                                                     |
|--------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| `title`    | `Long Text`     | Name of asset |
| `type` | `Link` | ID of asset status stored in `Asset Status` doctype |
| `status` | `Link` | ID of asset status stored in `Asset Status` doctype |
| `category`  | `Link`     | ID of asset category stored in `Asset Categories` doctype |
| `subcategory`  | `Link`     | ID of asset category stored in `Asset Sub Categories` doctype |
| `description`  | `Long Text`   | Description of the Asset            |
| `user` | `Data`     | Email of user who reported the asset |
| `phone_number`  | `Data`     | Phone number of the asset |
| `location` | `Link`     | ID of location stored in `Locations` doctype |
| `url`  | `Data`     | Any relevant URL to the event |
| `open_time`  | `Data`     | Opening time of the asset |
| `close_time`  | `Data`     | Close time of the asset |
| `rating`  | `Rating`     | Rating of the asset |


### Asset Status

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `status`    | `Data`     | Status of an asset |


### Asset Type

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `type`    | `Data`     | Type of an asset |


### Asset Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `category`    | `Data`     | Category of  an asset |


### Asset Sub Categories

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `subcategory`    | `Data`     | Sub Category of an asset |

### User Organizations

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `org_name`    | `Data`     | Name of the organization |
| `location`    | `Link`     | ID of location stored in `Locations` doctype |
| `user`    | `Data`     | Email address of user belonging to this organization |



### Flag
- Flag doctype stores all the Flagged/Reported doctypes.

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `title`    | `Data`     | Title for the flag |
| `flag_type`    | `Link`     | ID of flag type in `Flag Type` doctype |
| `status`    | `Link`     | ID of flag status in `Flag status` doctype |
| `flagged_by`    | `Data`     | Email address of user who created this flag |
| `flagged_doctype`    | `Data`     | The doctype being flagged |
| `flagged_document`    | `Data`     | Document id of doctype being flagged |
| `attachment`    | `Attach`     | Any file attachment |
| `description`    | `Long Text`     | Description of the flag / report |


### Flag Type

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `title`    | `Data`     | Name of flag type, example- Spam |


### Flag Status

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `title`    | `Data`     | Name of flag status, Example- Created, Approved|


### Badge
- Badge doctype stores all the badges
  
| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `title`    | `Data`     | Name of the badge |
| `icon`    | `Attach`     | Icon for the badge |
| `query`    | `code`     | SQL query which returns all the applications `User` for the badge |
| `active`    | `check`     | Check to disable/activate a badge |


### User Badge
- User Badge doctype stores all the badges assigned to Users

| Frappe field     | Field type|                                                                                                                                     |
|---------------|--------------------------|------------------------|
| `user`    | `Data`     | Email address of User |
| `badge`    | `Link`     | Badge assigned to User |
| `active`    | `check`     | Check to disable/activate this assigned badge |
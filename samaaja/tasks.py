"""All scheduled tasks for samaaja"""

import frappe
import requests
from frappe.utils.safe_exec import check_safe_sql_query

def badge_update1():
    logger = frappe.logger("samaaja", allow_site=True, file_count=5)
    logger.info('usernames update started')
    users = frappe.db.get_all('User',filters={'username':''})
    size = 6
    for user in users:
        doc = frappe.get_doc('User',user.name)
        prefix = doc.first_name
        if doc.last_name:
            prefix += "-" + doc.last_name
        prefix = prefix.lower()

        username = prefix + "-" + random_string(size)
        while frappe.db.get_value("User", {"username": username}, "name"):
            username = prefix + random_string(size)

        doc.username = username.lower().replace(".", "").replace(" ", "")
        doc.save()
        frappe.db.commit()
        logger.info(f"username created for  {doc.email}")
        break








def location_update():
    logger = frappe.logger("samaaja", allow_site=True, file_count=5)
    locations = frappe.get_all("Location", filters={"location_updated": False})
    geolocation_api_url = frappe.db.get_single_value("Samaaja Settings", "geolocation_api_url")
    if not geolocation_api_url:
        logger.warning(f"invalid geolocation api url {geolocation_api_url}")
        return
    for location in locations:
        doc = frappe.get_doc("Location", location.name)
        data = {
            "lat": doc.latitude,
            "lang": doc.longitude,
        }
        try:
            response = requests.post(geolocation_api_url, data=data, timeout=15)
            if response.status_code == 200:
                response = response.json()
                if len(response) > 0:
                    response["state"] = response.pop("u_state", None)
                    response["district"] = response.pop("u_district", None)
                    response["ward_name"] = response.pop("ward", None)
                    response["ward_number"] = response.pop("ward_no", None)
                    response["polzone"] = response("polzonename", None)
                    response["formatted_address"] = response("formatted_address", None)
                    response["pin"] = response("postalcode", None)
                    response["location_updated"] = 1
                    doc.update(response)
                    doc.save()
                    frappe.db.commit()
        except Exception as e:
            logger.error(f"could not update location for {doc.name} {str(e)}")

def badge_update():
    """Assigns and removes badges for all samaaja users."""
    logger = frappe.logger("samaaja", allow_site=True, file_count=5)
    logger.info("user badge assignment job started")
    # Get all active badges
    badges = frappe.db.get_list(
        "Badge",
        filters={"active": True},
        fields=["name", "query"],
    )

    for badge in badges:
        # Skip badges without SQL query
        if not badge.query:
            logger.error(f"sql query not found for badge {badge.name}")
            continue

        # Check if SQL query is safe for running.
        if not check_safe_sql_query(badge.query, throw=False):
            logger.error(f"query must be of SELECT or read-only WITH type for badge {badge.name}")
            continue

        try:
            all_users = frappe.db.sql(badge.query, as_dict=True)
        except Exception as e:
            logger.error(f"error while running {badge.name} badge sql query {str(e)}")
            continue

        # Disable this badge for other users
        if len(all_users) > 0:
            user_ids = [user.name for user in all_users]
            update_sql = """
                update `tabUser badge` set active = 0
                where badge = %s and user not in ({0})
            """.format(",".join(["%s"] * len(user_ids)))
            user_ids.insert(0, badge.name)
            frappe.db.sql(update_sql, user_ids)

        for user in all_users:
            # Check if an inactive badge exists for the user.
            exists = frappe.db.exists(
                "User badge",
                {
                    "user": user.name,
                    "badge": badge.name,
                    "active": 0,
                },
            )
            if exists:
                # Set badge as active
                frappe.db.set_value("User badge", exists, "active", 1)
                continue

            # If badge doesn't exist, create it
            doc = frappe.new_doc("User badge")
            doc.user = user.name
            doc.badge = badge.name
            doc.active = 1
            doc.insert()
        frappe.db.commit()

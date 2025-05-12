import frappe

def execute():
    custom_fields = ["headline", "profile_badges", "city", "state", "age", "org_id", "verified_by"]

    users = frappe.get_all("User", pluck="name")

    for user_name in users:
        if user_name == "Administrator":
            continue

        user_doc = frappe.get_doc("User", user_name)

        if not frappe.db.exists("User Metadata", {"user": user_name}):
            metadata = frappe.get_doc({
                "doctype": "User Metadata",
                "user": user_name
            })

            for field in custom_fields:
                value = user_doc.get(field)
                if value is not None:
                    metadata.set(field, value)

            metadata.insert(ignore_permissions=True)

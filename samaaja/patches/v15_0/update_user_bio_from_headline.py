# patch to update empty 'bio' with 'headline' if available
import frappe

def execute():
    # Check if 'headline' field exists in User DocType
    if not frappe.db.has_column("User", "headline"):
        return

    # Get users where bio is empty or null and headline is not null/empty
    users = frappe.get_all("User",
        filters={"bio": ["in", [None, ""]]},
        fields=["name", "headline"]
    )

    for user in users:
        if user.headline:
            frappe.db.set_value("User", user.name, "bio", user.headline)

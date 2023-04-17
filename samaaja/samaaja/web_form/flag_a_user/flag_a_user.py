import frappe

def get_context(context):
    # Check if user with this username exists
    username = frappe.form_dict.get("flagged_document")

    if not username:
        frappe.throw("Check if you have the correct URL from profile page", frappe.PermissionError)

    user_id = frappe.db.exists("User", {
        "username": username
    })

    if not user_id:
        frappe.throw("User not found", frappe.PermissionError)
    full_name = frappe.get_value("User", user_id, "full_name")
    context.introduction_text = f"""You're about to report <b>{full_name}</b>."""

import frappe

def get_context(context):
    doc_id = frappe.form_dict.get("flagged_document")

    if not doc_id:
        frappe.throw("Check if you have the correct URL", frappe.PermissionError)
    user_id = frappe.get_value("Events", doc_id, "user")
    full_name = frappe.get_value("User", user_id, "full_name")
    context.introduction_text = f"""You're about to report <b>{full_name}'s</b> action."""


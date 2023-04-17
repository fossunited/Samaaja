import frappe
from samaaja.page_renderers import get_profile_url_prefix

def get_context(context):
    context.no_cache = 1
    try:
        username = frappe.form_dict["username"].lower()
    except KeyError:
        username = frappe.db.get_value("User", frappe.session.user, ["username"])
        if username:
            frappe.local.flags.redirect_location = get_profile_url_prefix() + username
            raise frappe.Redirect

    context.title = username.title() + "'s profile page"
    try:
        context.current_user = frappe.get_doc("User", {"username": username})
        approved_report_exists = frappe.db.exists("Flag", {
            "flagged_doctype": context.current_user.doctype,
            "flagged_document": context.current_user.name,
            "status": "Approved"
        })
        if approved_report_exists:
            # raise exception so the page returns 404.
            raise Exception("profile not found")
    except Exception:
        context.template = "www/404.html"
        return


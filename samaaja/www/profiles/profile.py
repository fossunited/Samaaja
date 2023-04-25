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

    try:
        context.current_user = frappe.get_doc("User", {"username": username})
        approved_report_exists = frappe.db.exists(
            "Flag",
            {
                "flagged_doctype": context.current_user.doctype,
                "flagged_document": context.current_user.name,
                "status": "Approved",
            },
        )
        if approved_report_exists:
            context.flag_type = frappe.get_value("Flag", approved_report_exists, "flag_type")
            context.template = "www/reported-profile.html"
            return
        if context.current_user.full_name:
            context.title = context.current_user.full_name.title() + " Profile"
    except Exception:
        context.template = "www/404.html"
        return

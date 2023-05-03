import frappe
from http import HTTPStatus
from samaaja.api.common import custom_response


@frappe.whitelist(methods=["DELETE"])
def delete(doc_name):

    if frappe.session.user != frappe.get_value("Events", doc_name, "user"):
        return custom_response("Forbidden", status_code=HTTPStatus.FORBIDDEN)

    frappe.delete_doc("Events", doc_name)
    return custom_response("OK", status_code=HTTPStatus.OK)

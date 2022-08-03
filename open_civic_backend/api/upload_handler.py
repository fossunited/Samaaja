import frappe
from frappe.handler import upload_file


@frappe.whitelist(allow_guest=True)
def handler(doctype=None, filters=None, debug=False, cache=False):
    files = frappe.request.files
    filename_hash = None
    filename_ext = None
    if "file" in files:
        file = files["file"]
        filename = file.filename
        filename_ext = filename.rsplit(".", 1)[1]
        filename_hash = frappe.generate_hash(filename, 15)
        frappe.request.files["file"].filename = f"{filename_hash}.{filename_ext}"

    if filename_hash and filename_ext:
        frappe.form_dict.file_url = f"/files/{filename_hash}.{filename_ext}"
    frappe.form_dict.is_private = "0"
    res = upload_file()
    return res

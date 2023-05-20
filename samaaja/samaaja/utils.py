import frappe

def make_image_public(path):
    if path and "/private" in path:
        file = frappe.get_doc("File", {"file_url": path})
        file.is_private = 0
        file.save(ignore_permissions=True)
        return file.file_url
    return path

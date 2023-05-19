# Copyright (c) 2022, FOSSUnited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from samaaja.api.location import new_location
from frappe.utils import validate_email_address, random_string


class Events(Document):
    def before_insert(self):
        roles = frappe.get_roles()

        # Only system manager is allowed to insert documents on behalf of other users.
        if "System Manager" not in roles:
            if frappe.session.user != "Guest" and frappe.session.user != self.user:
                frappe.throw("Not allowed", frappe.PermissionError)

        # check if user with this email exists or not,
        # if user exists and current user is guest throw error.
        if frappe.session.user == "Guest" and self.user:
            self.user = self.user.strip()
            exists = frappe.db.exists("User", self.user.lower())
            if exists:
                frappe.throw(
                    f"Looks like you already have an account with email {self.user},\
                    Please <a href='/login'>login</a>",
                    title="Account already exists",
                )
            else:
                # create new user with this email if email is valid.
                valid_email = validate_email_address(self.user)
                if valid_email:
                    user = frappe.new_doc("User")
                    first_name = (
                        self.user.split("@")[0].replace(".", "").replace("+", "")
                    )
                    username = random_string(8)
                    user.update(
                        {
                            "first_name": first_name,
                            "email": self.user,
                            "enabled": 1,
                            "new_password": frappe.generate_hash(),
                            "user_type": "Website User",
                            "username": username,
                        }
                    )
                    user.save(ignore_permissions=1)

        if self.latitude and self.longitude:
            location = new_location(
                {"latitude": self.latitude, "longitude": self.longitude}
            )
            self.location = location.get("name")


def has_website_permission(doc, ptype, user, verbose=False):
    if doc.user == frappe.session.user:
        return True
    return False

# Copyright (c) 2022, FOSSUnited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from samaaja.api.location import new_location


class Events(Document):
    def before_insert(self):

        roles = frappe.get_roles()

        if "System Manager" not in roles:
            if frappe.session.user != "Guest" and frappe.session.user != self.user:
                frappe.throw("Not allowed", frappe.PermissionError)

        # check if user with this email exists or not,
        # if user exists and current user is guest throw error.
        if frappe.session.user == "Guest":
            exists = frappe.db.exists("User", self.user.lower())
            if exists:
                frappe.throw(
                    f"Looks like you already have an account with email {self.user},\
                    Please login and try again.",
                    title="Account already exists",
                )

        if self.latitude and self.longitude:
            location = new_location(
                {"latitude": self.latitude, "longitude": self.longitude}
            )
            self.location = location.get("name")


def has_website_permission(doc, ptype, user, verbose=False):
    if doc.user == frappe.session.user:
        return True
    return False

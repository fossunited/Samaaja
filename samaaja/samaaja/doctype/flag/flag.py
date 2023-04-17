# Copyright (c) 2022, FOSS United and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import validate_email_address


class Flag(Document):
    def before_save(self):
        # if flagged doctype is User & frappe document is username set the User ID (email) as flagged document.
        if self.flagged_doctype == "User" and not validate_email_address(
            self.flagged_document
        ):
            # Search for user with this username
            try:
                user = frappe.db.exists("User", {"username": self.flagged_document})
            except frappe.DoesNotExistError:
                pass
            else:
                self.flagged_document = user

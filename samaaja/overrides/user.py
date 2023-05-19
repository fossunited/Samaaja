"""Overrides for User doctype"""

import frappe
from frappe.utils import random_string


def before_save(doc, _):
    """
    Number of new lines check for profile headline
    """
    if doc.headline:
        doc.headline = doc.headline.strip("\n")
        nlines = doc.headline.count("\n")
        if nlines > 5:
            frappe.throw(
                "Please make sure your profile headline is fewer than 7 lines long and try again.",
                title="Could not save profile headline",
            )


def username(doc, _):
    """Generate random username from first & last name"""
    if not doc.username:
        size = 6

        prefix = doc.first_name
        if doc.last_name:
            prefix += "-" + doc.last_name
        prefix = prefix.lower()

        username = prefix + "-" + random_string(size)
        while frappe.db.get_value("User", {"username": username}, "name"):
            username = prefix + random_string(size)

        doc.username = username.lower().replace(".", "").replace(" ", "")

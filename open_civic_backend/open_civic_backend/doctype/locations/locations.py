# Copyright (c) 2022, FOSSUnited and contributors
# For license information, please see license.txt

from frappe.model.document import Document
from frappe.utils import now


class Locations(Document):

    def before_save(self):
        self.timestamp = now()

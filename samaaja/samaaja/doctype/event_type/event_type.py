# Copyright (c) 2022, FOSSUnited and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class EventType(Document):
	pass

@frappe.whitelist()
def add_node():
	from frappe.desk.treeview import make_tree_args

	args = frappe.form_dict
	args = make_tree_args(**args)

	if args.parent_event_type == "Event Type":
		args.parent_event_type = None

	frappe.get_doc(args).insert()
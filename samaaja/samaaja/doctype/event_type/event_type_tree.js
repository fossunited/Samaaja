frappe.treeview_settings['Event Type'] = {
    breadcrumb: 'Samaaja',
    title: __('Event Type'),
    get_tree_nodes: 'frappe.desk.treeview.get_children',
    root_label: 'All Event Types',
    ignore_fields: ['parent_event_type'],
    filters: [
        {
            fieldname: 'type',
            label: __('Type'),
            fieldtype: 'Data'
        }
    ],
    fields: [
        {
            fieldtype: 'Data',
            fieldname: 'type',
            label: __('New Event Type Name'),
            reqd: true
        },
        {
            fieldtype: 'Check',
            fieldname: 'is_group',
            label: __('Is Group'),
            description: __('Further cost centers can be made under Groups but entries can be made against non-Groups')
        }
    ],
    add_tree_node: 'samaaja.samaaja.doctype.event_type.event_type.add_node'
};

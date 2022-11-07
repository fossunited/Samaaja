import frappe
from frappe.utils.safe_exec import check_safe_sql_query


def update():
    # Update badge mapping for all users

    # Get all active badges
    badges = frappe.db.get_list(
        "Badge",
        filters={"active": True},
        fields=["name", "query"],
    )

    for badge in badges:
        if not badge.query:
            continue

        check_safe_sql_query(badge.query)

        all_users = frappe.db.sql(badge.query, as_dict=True)

        # Disable this badge for other users
        if len(all_users) > 0:
            user_ids = [user.name for user in all_users]
            update_sql = """
                update `tabUser badge` set active = 0
                where badge = %s and user not in ({0})
            """.format(",".join(["%s"] * len(user_ids)))
            user_ids.insert(0, badge.name)
            frappe.db.sql(update_sql, user_ids)

        for user in all_users:
            # Check if badge already exists for user
            exists = frappe.db.exists(
                "User badge",
                {
                    "user": user.name,
                    "badge": badge.name,
                },
            )
            if exists:
                # Set badge as active
                frappe.db.set_value("User badge", exists, "active", 1)
                continue

            # If badge doesn't exist, create it
            doc = frappe.new_doc("User badge")
            doc.user = user.name
            doc.badge = badge.name
            doc.active = 1
            doc.insert()

    frappe.db.commit()

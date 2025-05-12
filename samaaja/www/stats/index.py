import frappe
from frappe.utils import add_days, nowdate
from frappe.utils.safe_exec import check_safe_sql_query
from frappe.query_builder import Field
from frappe.query_builder import functions as fn
from frappe.query_builder import DocType

def get_context(context):
    logger = frappe.logger("samaaja", allow_site=True, file_count=5)

    context.no_cache = 1
    
    samaaja_settings = frappe.get_cached_doc("Samaaja Settings")
    
    context.samaaja_settings = samaaja_settings

    # Tables
    User = DocType("User")
    Events = DocType("Events")
    Location = DocType("Location")

    # Users with most actions
    leaderboard_query = (
        frappe.qb.from_(User)
        .join(Events)
        .on(Events.user == User.name)
        .select(
            User.name,
            User.username,
            User.first_name,
            User.user_image,
            User.location.as_("location"),
            fn.Sum(Events.hours_invested).as_("hours_invested"),
            fn.Count("*").as_("total_actions"),
        )
        .where(
            (User.enabled == 1)
            & (Events.creation >= add_days(nowdate(), -(samaaja_settings.leaderboard_max_days or 60)))
        )
        .groupby(User.name)
        .orderby(fn.Count("*"), order=frappe.qb.desc)
        .limit(samaaja_settings.leaderboard_page_size or 15)
    )
    context.leaderboard_data = leaderboard_query.run(as_dict=1, debug=True)

    # Top cities with most check-ins
    top_cities_query = (
        frappe.qb.from_(Location)
        .join(Events)
        .on(Events.location == Location.name)
        .select(
            Location.city,
            fn.Count("*").as_("count"),
        )
        .where(
            (Events.creation >= add_days(nowdate(), -(samaaja_settings.top_cities_max_days or 60)))
            & (Location.city.isnotnull())
        )
        .groupby(Location.city)
        .orderby(fn.Count("*"), order=frappe.qb.desc)
        .limit(samaaja_settings.top_cities_max_cities or 10)
    )
    context.top_cities = top_cities_query.run(as_dict=1)
    context.first_city_action_count = context.top_cities[0]["count"] if len(context.top_cities) else 0

    # Recent actions with images
    recent_actions_query = (
        frappe.qb.from_(Events)
        .join(Location)
        .on(Location.name == Events.location)
        .select(
            Events.name,
            Events.creation,
            frappe.qb.terms.Case()
            .when((Events.attachment1.isnotnull()) & (Events.attachment1 != ""), Events.attachment1)
            .else_(Events.attachment2)
            .as_("image"),
            Location.district,
            Location.city,
        )
        .where(
            (Events.attachment1.isnotnull() & (Events.attachment1 != ""))
            | (Events.attachment2.isnotnull() & (Events.attachment2 != ""))
        )
        .orderby(Events.creation, order=frappe.qb.desc)
        .limit(10)
    )
    context.recent_actions_with_images = recent_actions_query.run(as_dict=1)

    # Map points
    context.map_points = []
    map_points_query = frappe.db.get_single_value("Samaaja Settings", "map_stats_query")
    if map_points_query and check_safe_sql_query(map_points_query, throw=False):
        try:
            context.map_points = frappe.db.sql(map_points_query, as_dict=1)
        except Exception as e:
            logger.error("Invalid map points sql {0}".format(e))
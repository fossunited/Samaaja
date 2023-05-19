def get_context(context):
    # add leaflet to webform
    context.web_include_css.append("/assets/samaaja/css/leaflet.css")
    context.web_include_js.append("/assets/samaaja/js/leaflet.js")

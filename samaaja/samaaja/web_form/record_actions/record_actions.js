frappe.ready(function () {
  // Load top-level event types
  frappe.call({
    method: "frappe.client.get_list",
    args: {
      doctype: "Event Type",
      filters: {
        is_group: 1
      },
      fields: ["name"]
    },
    callback: function (r) {
      if (r.message) {
        const options = r.message.map(row => row.name);
        frappe.web_form.fields_dict.type.df.options = options;
        frappe.web_form.fields_dict.type.refresh();
      }
    }
  });

  // Load subtypes when type is selected
  frappe.web_form.on('type', function (value) {
    if (!value) return;

    frappe.call({
      method: "frappe.client.get_list",
      args: {
        doctype: "Event Type",
        filters: {
          parent_event_type: value.value,
          is_group: 0
        },
        fields: ["name"]
      },
      callback: function (r) {
        const subOptions = r.message.map(row => row.name);
        frappe.web_form.fields_dict.sub_type.df.options = subOptions;
        frappe.web_form.fields_dict.sub_type.refresh();
        frappe.web_form.set_value("sub_type", "");
      }
    });
  });

  // Validation before form submission
  frappe.web_form.validate = () => {
    let data = frappe.web_form.get_values();
    if (data.title.length > 70) {
      frappe.msgprint("Please restrict title to max 70 characters.");
      return false;
    }
    if (
      frappe.web_form.get_value("user") &&
      frappe.web_form.get_value("user") !== "Administrator" &&
      !frappe.utils.validate_type(frappe.web_form.get_value("user"), "email")
    ) {
      frappe.msgprint('Invalid email address');
      return false;
    }
  };

  // Title input live validation
  frappe.web_form.on("title", (field, value) => {
    if (value.length > 70) {
      frappe.msgprint(
        `Please restrict the title to max 70 characters, <br> You've entered ${value.length} characters in the title`
      );
    }
  });

  // Set max length for title input
  $('*[data-fieldname="title"]').attr("maxlength", "70");

  // Show/hide fields based on user login
  if (frappe.session.user && frappe.session.user != "Guest") {
    frappe.web_form.set_value(["user"], frappe.session.user);
    frappe.web_form.set_df_property("user", "hidden", 1);
    frappe.web_form.set_df_property("anonymous", "hidden", 1);
  } else {
    frappe.web_form.set_df_property("user", "reqd", 1);
    frappe.web_form.on("anonymous", (field, checked) => {
      if (!checked) {
        frappe.web_form.set_value(["user"], "");
        frappe.web_form.set_df_property("user", "hidden", 0);
        frappe.web_form.set_df_property("user", "reqd", 1);
      } else {
        frappe.web_form.set_value(["user"], "");
        frappe.web_form.set_df_property("user", "hidden", 1);
        frappe.web_form.set_df_property("user", "reqd", 0);
      }
    });
    frappe.web_form.set_df_property("user", "hidden", 0);
  }

  // Default map position
  let defaultPosition = [22.1458, 80.0882];

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showMap, showMap);
  } else {
    showMap(null);
  }

  function showMap(position) {
    if (position && position.coords) {
      let lat = position.coords.longitude;
      let long = position.coords.latitude;
      defaultPosition = [lat, long];
    }

    const container = document.getElementById("map");
    if (container) {
      const screenWidth = window.screen.width;
      let mapZoom = screenWidth < 700 ? 4 : 5.4;

      let map = L.map("map").setView(defaultPosition, mapZoom);

      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
          '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map);

      let allMarkers = [];

      map.locate({
        setView: true,
      }).on("locationerror", function (e) {
        console.log(e);
      });

      function onMapClick(e) {
        allMarkers.forEach(marker => map.removeLayer(marker));
        const latlng = e.latlng;

        frappe.web_form.set_value(["latitude"], latlng.lat);
        frappe.web_form.set_value(["longitude"], latlng.lng);

        let marker = L.marker([latlng.lat, latlng.lng]).addTo(map);
        allMarkers.push(marker);
      }

      map.on("click", onMapClick);
    }
  }
});
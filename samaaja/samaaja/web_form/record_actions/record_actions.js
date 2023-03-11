frappe.ready(function () {
  // hide / show fields based on user login information
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
        frappe.web_form.set_value(["user"], "anonymous@samaaja.org");
        frappe.web_form.set_df_property("user", "hidden", 1);
      }
    });
    frappe.web_form.set_df_property("user", "hidden", 0);
  }

  // appned map div element to the form
  $("div.form-page").append(
    '<div id ="map" style ="position:relative;width:100%; height:400px;"></div>'
  );

  // default starting position for map
  let defaultPosition = [13.199379, 77.710136];

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showMap, showMap);
  } else {
    showMap(null);
  }

  function showMap(position) {
    if (position) {
      if (position.coords) {
        let lat = position.coords.longitude;
        let long = position.coords.latitude;
        defaultPosition = [];
        defaultPosition.push(lat);
        defaultPosition.push(long);
      }
    }
    const container = document.getElementById("map");
    if (container) {
      let map = L.map("map").setView(defaultPosition, 13);

      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
          '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map);
      let allMarkers = [];
      map
        .locate({
          setView: true,
        })
        .on("locationerror", function (e) {
          console.log(e);
        });

      function onMapClick(e) {
        for (let step = 0; step < allMarkers.length; step++) {
          map.removeLayer(allMarkers[step]);
        }
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

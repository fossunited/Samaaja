// Copyright (c) 2022, FOSSUnited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Location', {
	before_save: function(frm) {
		let geolocation_data = frm.doc.geolocation
		if (geolocation_data) {
			geolocation_data = JSON.parse(geolocation_data)
			let features = geolocation_data.features
			if (features) {
				for (let i = 0; i < features.length; i++) {
					let feature = features[i]
					if (feature.geometry.type === 'Point') {
						let coordinates = feature.geometry.coordinates
						if (!frm.doc.latitude || ! frm.doc.longitude) {
							return
						}
						let geolocationLatitude = coordinates[1]
						let geolocationLongitude = coordinates[0]

						// Compare the coordinates to the current values
						if (frm.doc.latitude != geolocationLatitude || frm.doc.longitude != geolocationLongitude) {
							if (!frm.doc.allow_geolocation_override) {
								frappe.confirm(
									__('Entered coordinates are different than the coordinates of the <b>Point</b> in geolocation map data. Are you sure you want to save?'),
									function() {
										frm.doc.allow_geolocation_override = true
										frm.save()
									}
								);
								// Prevent the save
								throw new Error('Cannot save')
							}
						}
						// Compare only the first Point
						break
					}
				}
			}
		}
	}
});

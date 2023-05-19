frappe.ready(function () {
  if (window.location.href.indexOf(`${frappe.session.user}`) == -1) {
  	window.location.href = `/edit-profile/${frappe.session.user}/edit`;
  }
});

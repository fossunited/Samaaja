frappe.ready(function () {
	// bind events here
	$('*[data-fieldname="title"]').attr("maxlength", "70");

	this.$delete_button = $(`<button class="btn btn-danger btn-delete btn-sm mr-2 ">
		${__("Delete this action")}
	</button>`);

	$(".web-form-head .web-form-actions").prepend(this.$delete_button);
	this.$delete_button.on("click", () => {
		frappe.confirm(
			"Are you sure you want to delete this action?",
			function () {
				frappe.call({
					method: 'samaaja.api.action.delete',
					args: {
						doc_name: frappe.web_form.doc.name
					},
					type: "DELETE",
					success: function (r) {
						show_alert('Action deleted successfully! <br> Redirecting to your profile.');
						setTimeout(() => {
							window.location.href = `/profiles/profile`;
						}, 2200)
					},
					error: function (r) {
						show_alert('Unexpected error!');
					},
					always: function (r) {}
				});
			},
		)
	});
})
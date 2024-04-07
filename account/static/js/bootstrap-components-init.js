/* -----------------------------
     * Bootstrap components init
     * Script file: theme-plugins.js, tether.min.js
     * Documentation about used plugin:
     * https://v4-alpha.getbootstrap.com/getting-started/introduction/
     * ---------------------------*/


CRUMINA.Bootstrap = function () {
	//  Activate the Tooltips
	$('[data-toggle="tooltip"], [rel="tooltip"]').tooltip();

	// And Popovers
	$('[data-toggle="popover"]').popover();

	/* -----------------------------
	   * Replace select tags with bootstrap dropdowns
	   * Script file: theme-plugins.js
	   * Documentation about used plugin:
	   * https://silviomoreto.github.io/bootstrap-select/
	   * ---------------------------*/
	$('.selectpicker').selectpicker();

	/* -----------------------------
	 * Date time picker input field
	 * Script file: daterangepicker.min.js, moment.min.js
	 * Documentation about used plugin:
	 * https://v4-alpha.getbootstrap.com/getting-started/introduction/
	 * ---------------------------*/
	var date_select_field = $('input[name="datetimepicker"]');
	if (date_select_field.length) {
		var start = moment().subtract(29, 'days');

		date_select_field.daterangepicker({
			startDate: start,
			autoUpdateInput: false,
			singleDatePicker: true,
			showDropdowns: true,
			locale: {
				format: 'DD/MM/YYYY'
			}
		});
		date_select_field.on('focus', function () {
			$(this).closest('.form-group').addClass('is-focused');
		});
		date_select_field.on('apply.daterangepicker', function (ev, picker) {
			$(this).val(picker.startDate.format('DD/MM/YYYY'));
			$(this).closest('.form-group').addClass('is-focused');
		});
		date_select_field.on('hide.daterangepicker', function () {
			if ('' === $(this).val()){
				$(this).closest('.form-group').removeClass('is-focused');
			}
		});

	}
};

$(document).ready(function () {
	CRUMINA.Bootstrap();
});
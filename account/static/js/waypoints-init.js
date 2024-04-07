/* -----------------------
 * COUNTER NUMBERS
 * --------------------- */


$(document).ready(function () {
	var $counter = $('.counter');

	if ($counter.length) {
		$counter.each(function () {
			jQuery(this).waypoint(function () {
				$(this.element).find('span').countTo();
				this.destroy();
			}, {offset: '95%'});
		});
	}
});
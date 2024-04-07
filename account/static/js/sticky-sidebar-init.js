
CRUMINA.StickySidebar = function () {
	var $header = $('#site-header');

	$('.crumina-sticky-sidebar').each(function () {

	var sidebar = new StickySidebar (this, {
		topSpacing: $header.height(),
		bottomSpacing: 0,
		containerSelector: false,
		innerWrapperSelector: '.sidebar__inner',
		resizeSensor: true,
		stickyClass: 'is-affixed',
		minWidth: 0
		})
	});
};

$(document).ready(function () {
	CRUMINA.StickySidebar();
});
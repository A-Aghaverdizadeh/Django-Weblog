/* -----------------------------
     * Equal height elements
     * Script file: theme-plugins.js
     * Documentation about used plugin:
     * http://brm.io/jquery-match-height/
     * ---------------------------*/

CRUMINA.equalHeight = function () {
	$('.js-equal-child').find('.theme-module').matchHeight({
		property: 'min-height'
	});
};


$(document).ready(function () {
	if (typeof $.fn.matchHeight !== 'undefined'){
		CRUMINA.equalHeight();
	}
});
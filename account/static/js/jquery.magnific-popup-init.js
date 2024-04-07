/* -----------------------------
	* Lightbox popups for media
	* Script file: jquery.magnific-popup.min.js
	* Documentation about used plugin:
	* http://dimsemenov.com/plugins/magnific-popup/documentation.html
	* ---------------------------*/


CRUMINA.mediaPopups = function () {
	$('.play-video').magnificPopup({
		disableOn: 700,
		type: 'iframe',
		mainClass: 'mfp-fade',
		removalDelay: 160,
		preloader: false,
		fixedContentPos: false
	});
	$('.js-zoom-image').magnificPopup({
		type: 'image',
		removalDelay: 500, //delay removal by X to allow out-animation
		callbacks: {
			beforeOpen: function () {
				// just a hack that adds mfp-anim class to markup
				this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
				this.st.mainClass = 'mfp-zoom-in';
			}
		},
		closeOnContentClick: true,
		midClick: true
	});
	$('.js-zoom-gallery').each(function () {
		$(this).magnificPopup({
			delegate: 'a',
			type: 'image',
			gallery: {
				enabled: true
			},
			removalDelay: 500, //delay removal by X to allow out-animation
			callbacks: {
				beforeOpen: function () {
					// just a hack that adds mfp-anim class to markup
					this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');
					this.st.mainClass = 'mfp-zoom-in';
				}
			},
			closeOnContentClick: true,
			midClick: true
		});
	});
};

$(document).ready(function () {

	if (typeof $.fn.magnificPopup !== 'undefined'){
		CRUMINA.mediaPopups();
	}
});
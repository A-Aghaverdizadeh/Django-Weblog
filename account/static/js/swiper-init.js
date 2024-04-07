/* -----------------------------
     * Sliders and Carousels
     * Script file: swiper.jquery.min.js
     * Documentation about used plugin:
     * http://idangero.us/swiper/api/
     * ---------------------------*/


var swipers = {};

$(document).ready(function () {
	var initIterator = 0;
	var $breakPoints = false;
	$('.swiper-container').each(function () {

		var $t = $(this);
		var index = 'swiper-unique-id-' + initIterator;

		$t.addClass('swiper-' + index + ' initialized').attr('id', index);
		$t.find('.swiper-pagination').addClass('pagination-' + index);

		var $effect = ($t.data('effect')) ? $t.data('effect') : 'slide',
			$crossfade = ($t.data('crossfade')) ? $t.data('crossfade') : true,
			$loop = ($t.data('loop') == false) ? $t.data('loop') : true,
			$showItems = ($t.data('show-items')) ? $t.data('show-items') : 1,
			$scrollItems = ($t.data('scroll-items')) ? $t.data('scroll-items') : 1,
			$scrollDirection = ($t.data('direction')) ? $t.data('direction') : 'horizontal',
			$mouseScroll = ($t.data('mouse-scroll')) ? $t.data('mouse-scroll') : false,
			$autoplay = ($t.data('autoplay')) ? parseInt($t.data('autoplay'), 10) : 0,
			$autoheight = ($t.hasClass('auto-height')) ? true: false,
			$slidesSpace = ($showItems > 1) ? 20 : 0;

		if ($showItems > 1) {
			$breakPoints = {
				480: {
					slidesPerView: 1,
					slidesPerGroup: 1
				},
				768: {
					slidesPerView: 2,
					slidesPerGroup: 2
				}
			}
		}

		swipers['swiper-' + index] = new Swiper('.swiper-' + index, {
			pagination: '.pagination-' + index,
			paginationClickable: true,
			direction: $scrollDirection,
			mousewheelControl: $mouseScroll,
			mousewheelReleaseOnEdges: $mouseScroll,
			slidesPerView: $showItems,
			slidesPerGroup: $scrollItems,
			spaceBetween: $slidesSpace,
			keyboardControl: true,
			setWrapperSize: true,
			preloadImages: true,
			updateOnImagesReady: true,
			autoplay: $autoplay,
			autoHeight: $autoheight,
			loop: $loop,
			breakpoints: $breakPoints,
			effect: $effect,
			fade: {
				crossFade: $crossfade
			},
			parallax: true,
			onSlideChangeStart: function (swiper) {
				var sliderThumbs = $t.siblings('.slider-slides');
				if (sliderThumbs.length) {
					sliderThumbs.find('.slide-active').removeClass('slide-active');
					var realIndex = swiper.slides.eq(swiper.activeIndex).attr('data-swiper-slide-index');
					sliderThumbs.find('.slides-item').eq(realIndex).addClass('slide-active');
				}
			}
		});
		initIterator++;
	});


	//swiper arrows
	$('.btn-prev').on('click', function () {
		var sliderID = $(this).closest('.slider-slides').siblings('.swiper-container').attr('id');
		swipers['swiper-' + sliderID].slidePrev();
	});

	$('.btn-next').on('click', function () {
		var sliderID = $(this).closest('.slider-slides').siblings('.swiper-container').attr('id');
		swipers['swiper-' + sliderID].slideNext();
	});

	//swiper arrows
	$('.btn-prev-without').on('click', function () {
		var sliderID = $(this).closest('.swiper-container').attr('id');
		swipers['swiper-' + sliderID].slidePrev();
	});

	$('.btn-next-without').on('click', function () {
		var sliderID = $(this).closest('.swiper-container').attr('id');
		swipers['swiper-' + sliderID].slideNext();
	});


	// Click on thumbs
	$('.slider-slides .slides-item').on('click', function () {
		if ($(this).hasClass('slide-active')) return false;
		var activeIndex = $(this).parent().find('.slides-item').index(this);
		var sliderID = $(this).closest('.slider-slides').siblings('.swiper-container').attr('id');
		swipers['swiper-' + sliderID].slideTo(activeIndex + 1);
		$(this).parent().find('.slide-active').removeClass('slide-active');
		$(this).addClass('slide-active');

		return false;
	});

});

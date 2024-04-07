var calendar = {

    init: function() {

        /**
         * Get current date
         */
        var d = new Date();
        var strDate = d.getFullYear() + "/" + (d.getMonth() + 1) + "/" + d.getDate();

        /**
         * Get current month and set as '.current-month' in title
         */
        var monthNumber = d.getMonth() + 1;

        function GetMonthName(monthNumber) {
            var months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
            return months[monthNumber - 1];
        }

        $('.month').text(GetMonthName(monthNumber));

        /**
         * Get current day and set as '.current-day'
         */
        $('tbody td[data-day="' + d.getDate() + '"]').addClass('current-day');

        /**
         * Add class '.active' on calendar date
         */
        $('tbody td').on('click', function(e) {
            if ($(this).hasClass('event')) {
                $('tbody td').removeClass('active');
                $(this).addClass('active');
            } else {
                $('tbody td').removeClass('active');
            };
        });

        /**
         * Add '.event' class to all days that has an event
         */
        $('.day-event').each(function(i) {
            var eventMonth = $(this).data('month');
            var eventDay = $(this).data('day');
            $('tbody tr td[data-month="' + eventMonth + '"][data-day="' + eventDay + '"]').addClass('event');
        });

        /**
         * Get current day on click in calendar
         * and find day-event to display
         */
        $('tbody td').on('click', function(e) {
            $('.day-event').slideUp('fast');
            var monthEvent = $(this).data('month');
            var dayEvent = $(this).text();
            $('.day-event[data-month="' + monthEvent + '"][data-day="' + dayEvent + '"]').slideDown('fast');
        });

        /**
         * Close day-event
         */
        $('.close').on('click', function(e) {
            $(this).parent().slideUp('fast');
        });

        /**
         * Save & Remove to/from personal list
         */
        $('.save').click(function() {
            if (this.checked) {
                $(this).next().text('Remove from personal list');
                var eventHtml = $(this).closest('.day-event').html();
                var eventMonth = $(this).closest('.day-event').data('month');
                var eventDay = $(this).closest('.day-event').data('day');
                var eventNumber = $(this).closest('.day-event').data('number');
                $('.person-list').append('<div class="day" data-month="' + eventMonth + '" data-day="' + eventDay + '" data-number="' + eventNumber + '" style="display:none;">' + eventHtml + '</div>');
                $('.day[data-month="' + eventMonth + '"][data-day="' + eventDay + '"]').slideDown('fast');
                $('.day').find('.close').remove();
                $('.day').find('.save').removeClass('save').addClass('remove');
                $('.day').find('.remove').next().addClass('hidden-print');
                remove();
                sortlist();
            } else {
                $(this).next().text('Save to personal list');
                var eventMonth = $(this).closest('.day-event').data('month');
                var eventDay = $(this).closest('.day-event').data('day');
                var eventNumber = $(this).closest('.day-event').data('number');
                $('.day[data-month="' + eventMonth + '"][data-day="' + eventDay + '"][data-number="' + eventNumber + '"]').slideUp('slow');
                setTimeout(function() {
                    $('.day[data-month="' + eventMonth + '"][data-day="' + eventDay + '"][data-number="' + eventNumber + '"]').remove();
                }, 1500);
            }
        });

        function remove() {
            $('.remove').click(function() {
                if (this.checked) {
                    $(this).next().text('Remove from personal list');
                    var eventMonth = $(this).closest('.day').data('month');
                    var eventDay = $(this).closest('.day').data('day');
                    var eventNumber = $(this).closest('.day').data('number');
                    $('.day[data-month="' + eventMonth + '"][data-day="' + eventDay + '"][data-number="' + eventNumber + '"]').slideUp('slow');
                    $('.day-event[data-month="' + eventMonth + '"][data-day="' + eventDay + '"][data-number="' + eventNumber + '"]').find('.save').data('checked', false);
                    $('.day-event[data-month="' + eventMonth + '"][data-day="' + eventDay + '"][data-number="' + eventNumber + '"]').find('span').text('Save to personal list');
                    setTimeout(function() {
                        $('.day[data-month="' + eventMonth + '"][data-day="' + eventDay + '"][data-number="' + eventNumber + '"]').remove();
                    }, 1500);
                }
            });
        }

        /**
         * Sort personal list
         */
        function sortlist() {
            var personList = $('.person-list');

            personList.find('.day').sort(function(a, b) {
                return +a.getAttribute('day') - +b.getAttribute('day');
            }).appendTo(personList);
        }

        /**
         * Print button
         */
        $('.print-btn').click(function() {
            window.print();
        });

    },
};

$(document).ready(function() {

    calendar.init();

});
$(document).ready(function () {
    var btn = $('#back-to-top-button');
    var bannerTop= $("#banner").offset().top;
    var aboutMeTop = $('#about_me').offset().top

    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll >= aboutMeTop) {
            var delay = 0;
            $('#about_me  .large-text').each($).wait(200, function() {
                $(this).css({'color':'#13134f','top':'0'});
            });
        }
    });

    // $('.project-card').mouseenter(function () {
    //     $(this).animate('height','10em');
    // });

});


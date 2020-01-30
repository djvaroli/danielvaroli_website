$(document).ready(function () {
    var btn = $('#back-to-top-button');
    var banner = $("#banner");
    var bannerTop= banner.offset().top;

    var aboutMe = $('#about_me');
    var aboutMeTop = aboutMe.offset().top;
    var aboutMeFirstTextTop = aboutMe.find('.large-text:first-child').offset().top;

    var largeText = $('.large-text');

    var projectCard = $('.project-card-wrapper');
    // var normalText = $('.normal-text');

    $(window).scroll(function () {
        var viewportHeight = $(window).height();
        var scroll = $(window).scrollTop();


        largeText.each($).wait(150, function () {
             if (0.98*(scroll + viewportHeight) >= $(this).offset().top) {
                $(this).css({'color': '#13134f', 'top': '0'});
             }
        });
    });

    // function callback() {
    //   setTimeout(function() {
    //     $( "#effect:visible" ).removeAttr( "style" ).fadeOut();
    //   }, 1000 );
    // };

});
            // var delay = 0;
            // $('#about_me  .large-text').each($).wait(200, function() {
            // });
            // }
            // });
            // if (1.05*(scroll + viewportHeight) >= aboutMeFirstTextTop) {
            //     var delay = 0;
            //     $('#about_me  .large-text').each($).wait(200, function() {
            //         $(this).css({'color':'#13134f','top':'0'});
            //     });
            // }
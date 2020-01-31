$(document).ready(function () {
    var btn = $('#back-to-top-button');
    var banner = $("#banner");
    var bannerTop= banner.offset().top;

    var aboutMe = $('#about_me');

    var largeText = $('.large-text');

    var projectCard = $('.project-card-wrapper');
    // var normalText = $('.normal-text');

    var cvDownload = $('#cv-download');

    $(window).scroll(function () {
        var viewportHeight = $(window).height();
        var scroll = $(window).scrollTop();


        largeText.each($).wait(50, function () {
             if (scroll + viewportHeight + 50 >= $(this).offset().top) {
                $(this).css({'color': '#13134f', 'top': '0'});
             }
        });

        cvDownload.wait(500, function () {
            if ((scroll + viewportHeight + 50) >= $(this).offset().top) {
                $(this).show('fade',500);
             }
        })
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
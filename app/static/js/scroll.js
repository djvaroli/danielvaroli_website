$(document).ready(function () {
    var btn = $('#back-to-top-button');

    btn.click(function () {
        $("html, body").animate({scrollTop: "0px"}, 50);
    });

    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        if (scroll >= 320) {
            btn.css({'bottom':'2rem'});
        } else {
            btn.css({'bottom':'-5rem'});
        }
    });
});


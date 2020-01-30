var section = $('.section-content');
var menuLink = $('#header-menu > a');


menuLink.click(function () {
    var href = $(this).attr('for');
    var elementTop = $(document).find('#' + href).offset().top;
    $("html, body").animate({scrollTop: elementTop}, 100, );
});
$(document).ready(function () {
    var btn = $('#back-to-top-button');

    btn.click(function () {
        $("html, body").animate({scrollTop: "0px"}, 100);
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


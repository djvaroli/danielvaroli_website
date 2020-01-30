var menuLinks = $('#header-menu > a');

$(document).ready(function () {
    setTimeout(function (){
        $('.alert, .alert-inof').css('right','1em');
    },150);

    setTimeout(function () {
        $('.alert, .alert-inof').css('right','-50%');
    },3000);

    menuLinks.each($).wait(100, function () {
        $(this).css('top','0');
    });

});
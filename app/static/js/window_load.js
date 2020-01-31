var menuLinks = $('#header-menu > a');
var icons = $('#icons > a');
var menuLinksDelay = 100;
var iconsEffect = 'clip';


function showIcons(effect) {
    icons.each($).wait(100, function () {
        $(this).show( effect, 800);
    });
}

$(document).ready(function () {
    setTimeout(function (){
        $('.alert, .alert-inof').css('right','1em');
    },150);

    setTimeout(function () {
        $('.alert, .alert-info').css('right','-100%');
    },3000);

    menuLinks.each($).wait(menuLinksDelay, function () {
        $(this).css('top','0');
    });

    setTimeout(function () {
        showIcons(iconsEffect);
    },menuLinks.length*menuLinksDelay + 800)
});
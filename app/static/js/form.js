var sendFormButton =  $('#submit');
var emailField = $('#email');
var isValidEmail = false;
var buttonDeactivated = true;

function areInputsValid() {
    return grecaptcha.getResponse() && isValidEmail && buttonDeactivated;
}

$(document).ready(function () {
    if(buttonDeactivated) sendFormButton.addClass('deactivated');
    var inputEmail  = emailField.val();
    isValidEmail = isEmail(inputEmail);

});

function isEmail(string) {
    return string.indexOf("@") >= 0;
}

emailField.keyup(function () {
    var inputEmail  = emailField.val();
    isValidEmail = isEmail(inputEmail);
});


setInterval(function () {
    if(grecaptcha.getResponse() && isValidEmail && buttonDeactivated){
        sendFormButton.removeClass('deactivated');
        buttonDeactivated = false;
    }
}, 50);

// sendFormButton.submit(function () {
//     alert('Running');
//
//     formData = $('form').serializeArray();
//     formDataString = '';
//     $.each(formData, function(i, field) {
//                     formDataString += field.value + "&&";
//                 });
//
//     $.ajax({
//         url: "/send_form",
//         type: 'get',
//         data: {formData:formDataString},
//         success: function (response) {
//             alert(response);
//             $('#alerts').css('top','1em');
//             // setTimeout(function () {
//             //     window.location.replace(response)
//             // },500);
//         }, fail: function (response) {
//             // window.location.replace(response)
//             alert('Failed')
//         }
//     });
//
// });
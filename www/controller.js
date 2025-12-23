$(document).ready(function () {


    //Display Speak message

    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $('.siri-message').text(message);
        $('.siri-message').textillate('start');
    }

});
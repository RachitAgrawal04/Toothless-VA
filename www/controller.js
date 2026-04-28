$(document).ready(function () {


    //Display Speak message — must match the name used in Python: eel.displayMessage()

    eel.expose(displayMessage)
    function displayMessage(message) {

        $('.siri-message').text(message);
        $('.siri-message').textillate('start');
    }

});
$(document).ready(function () {

    // Initialize Eel if available
    if (typeof eel !== 'undefined' && typeof eel.init === 'function') {
        eel.init();
    }

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = null;

    function getSiriWidth() {
        var maxWidth = 800;
        var padding = 100;
        return Math.max(200, Math.min(maxWidth, window.innerWidth - padding));
    }

    function initSiriWave() {
        if (siriWave) {
            siriWave.stop();
            $("#siri-container").empty();
        }
        siriWave = new SiriWave({
            container: document.getElementById("siri-container"),
            width: getSiriWidth(),
            height: 200,
            style: "ios9",
            amplitude: "1",
            speed: "0.30",
            autostart: true
        });
    }

    initSiriWave();

    $(window).on('resize', function () {
        initSiriWave();
    });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // Mic Button Click Event

    $('#MicBtn').click(function () {
        eel.play_assistant_sound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        $('.siri-message').text('Listening...');
        // Call Python, then handle the recognized text
        eel.takecommand()(function(response) {
            if (response && response !== "None") {
                $('.siri-message').text(response);
            }
            // Return to main screen after handling
            $("#Oval").attr("hidden", false);
            $("#SiriWave").attr("hidden", true);
        });
    });

    // Back button to return to main screen
    $('#BackBtn').click(function () {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    });
});
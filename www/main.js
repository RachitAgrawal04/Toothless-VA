$(document).ready(function () {

    // Initialize Eel if available
    if (typeof eel !== 'undefined') {
        eel.init()()
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
});
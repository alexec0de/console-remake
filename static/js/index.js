$(window).load(function() {
    $('#load-display').fadeOut();
});

function setCookie(name, value) {
    document.cookie = name + "=" + (value || "") + "; path=/";
}

function getCookie(name, default_value=null) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return default_value;
}

$(document).ready(function() {
    darkMode = getCookie("dark", "0")

    if(darkMode == "1")
    {
        $("body").toggleClass("dark", true);
        $("#darkmode").text("light_mode");
    }

    $("#darkmode").on({'click': function() {
        if(darkMode == "1") {
            setCookie("dark", "0");
            $("body").toggleClass("dark", false);
            $("#darkmode").text("dark_mode");
            darkMode = "0";
        }
        else {
            setCookie("dark", "1");
            $("body").toggleClass("dark", true);
            $("#darkmode").text("light_mode");
            darkMode = "1";
        }
    }})
});
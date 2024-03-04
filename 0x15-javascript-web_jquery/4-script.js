// Changes script when clicked
$(function() {
    $("#toggle_header").click(function() {
        $("header").toggleClass("red green");
    });
});
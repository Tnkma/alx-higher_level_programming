// Fetches the URL and displays the value of hello from that URL
$(function() {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
        $("#hello").text(data.hello);
    });
});
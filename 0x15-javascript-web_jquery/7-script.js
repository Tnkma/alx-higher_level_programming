// Fetches the character name from a URL
$(function() {
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
        $("#character").text(data.name);
    });
});
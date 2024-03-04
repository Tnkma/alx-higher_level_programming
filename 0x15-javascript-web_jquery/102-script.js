// fetches and prints how to say “Hello” depending on the language
$(function() {
    $("btn_translate").click(function() {
        $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
            $("#language_code").val(date.code);
            $("#hello").text(data.hello);
        });
    });
});
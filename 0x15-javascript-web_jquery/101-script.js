// List, Add, Remove
$(function() {
    $("#add_item").click(function() {
        $("ul.my_list").append("<li>Item</li>")
    });
    $("#remove_item").remove(function() {
        $("ul.my_list").remove("<li>Item</li>")
    });
    $("#clear_list").click(function() {
        $("ul.my_list").empty()
    });
});

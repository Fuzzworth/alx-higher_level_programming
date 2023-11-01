$(document).ready(function () {
  // Add a new <li> element when the user clicks on DIV#add_item
  $("#add_item").click(function () {
    var newItem = $("<li>Item</li>");
    $("ul.my_list").append(newItem);
  });

  // Remove the last <li> element when the user clicks on DIV#remove_item
  $("#remove_item").click(function () {
    $("ul.my_list li:last").remove();
  });

  // Clear all <li> elements when the user clicks on DIV#clear_list
  $("#clear_list").click(function () {
    $("ul.my_list").empty();
  });
});

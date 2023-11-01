$(document).ready(function () {
  // Add a click event handler to the div with the id 'add_item'
  $("#add_item").click(function () {
    // Create a new <li> element with the text "Item"
    var newListItem = $("<li>Item</li>");
    // Append the new <li> element to the UL.my_list
    $("ul.my_list").append(newListItem);
  });
});

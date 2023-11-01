$(document).ready(function () {
  // Add a click event handler to the div with the id 'update_header'
  $("#update_header").click(function () {
    // Select the 'header' element and update its text
    $("header").text("New Header!!!");
  });
});


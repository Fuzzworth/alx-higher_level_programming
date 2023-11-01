$(document).ready(function () {
  // Add a click event handler to the div with the id 'red_header'
  $("#red_header").click(function () {
    // Select the 'header' element and update its text color to red
    $("header").css("color", "#FF0000");
  });
});

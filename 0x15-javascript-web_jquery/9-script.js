$(document).ready(function () {
  // Make an AJAX GET request to the URL
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    // Display the translation of "hello" in the div with the id 'hello'
    $("#hello").text(data.hello);
  });
});

$(document).ready(function () {
  // Function to fetch and display the translation
  function fetchAndDisplayTranslation() {
    // Get the language code from the input with id 'language_code'
    var languageCode = $("#language_code").val();

    // Make an AJAX GET request to the API with the language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      // Display the translation of "Hello" in the div with id 'hello'
      $("#hello").text(data.hello);
    });
  }

  // Add a click event handler to the button with id 'btn_translate'
  $("#btn_translate").click(fetchAndDisplayTranslation);

  // Add a keypress event handler to the input with id 'language_code'
  $("#language_code").keypress(function (e) {
    if (e.which === 13) {
      // If the user presses ENTER, fetch and display the translation
      fetchAndDisplayTranslation();
    }
  });
});

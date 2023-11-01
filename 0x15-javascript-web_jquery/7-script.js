$(document).ready(function () {
  // Make an AJAX GET request to the URL
  $.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function (data) {
    // Extract the character name from the response data
    var characterName = data.name;

    // Update the text of the div with the id 'character' with the character name
    $("#character").text(characterName);
  });
});

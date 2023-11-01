$(document).ready(function () {
  // Make an AJAX GET request to the URL
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
    // Get the movies from the response data
    var movies = data.results;

    // Select the ul element with the id 'list_movies'
    var listMovies = $("#list_movies");

    // Iterate through the movies and create list items for each
    $.each(movies, function (index, movie) {
      var movieTitle = movie.title;
      var listItem = $("<li>").text(movieTitle);
      listMovies.append(listItem);
    });
  });
});

$(document).ready(function() {
  // Define the URL to fetch data from
  const url = 'https://swapi.dev/api/films/?format=json';

  // Fetch data from the URL
  $.get(url, function(data) {
    const films = data.results;
    // Loop through each film and append its title to the UL#list_movies element
    for (const film of films) {
      $('ul#list_movies').append(`<li>${film.title}</li>`);
    }
  });
});

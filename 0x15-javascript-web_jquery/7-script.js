$(document).ready(function() {
  // Define the URL to fetch data from
  const url = 'https://swapi.dev/api/people/5/?format=json';

  // Fetch data from the URL
  $.get(url, function(data, status) {
    // Replace the text of the DIV#character element with the fetched name
    $('#character').text(data.name);
  });
});

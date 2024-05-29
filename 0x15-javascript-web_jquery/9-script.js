$(document).ready(function() {
  // Define the URL to fetch data from
  const url = 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22San%20Francisco%2C%20CA%22)&format=json';

  // Fetch data from the URL
  $.get(url, function(data) {
    const wind = data.query.results.channel.wind.speed;
    // Replace the text of the div#sf_wind_speed element with the wind speed
    $('#sf_wind_speed').text(wind);
  });
});


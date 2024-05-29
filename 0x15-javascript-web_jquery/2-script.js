$(document).ready(function() {
  // Add click event listener to div#red_header
  $('div#red_header').on('click', function() {
    // Change the color of the <header> element to red
    $('header').css('color', '#FF0000');
  });
});

$(document).ready(function() {
  // Add click event listener to div#red_header
  $('div#red_header').on('click', function() {
    // Add 'red' class to the <header> element
    $('header').addClass('red');
  });
});

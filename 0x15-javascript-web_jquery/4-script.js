$(document).ready(function() {
  // Add click event listener to div#toggle_header
  $('div#toggle_header').on('click', function() {
    // Toggle the 'red' class on the <header> element
    $('header').toggleClass('red');
  });
});

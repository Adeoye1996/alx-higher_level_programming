$(document).ready(function() {
  // Add click event listener to div#update_header
  $('div#update_header').on('click', function() {
    // Update the text of the <header> element
    $('header').text('New Header!!!');
  });
});

$(document).ready(function() {
  // Add click event listener to div#add_item
  $('div#add_item').on('click', function() {
    // Create a new <li> element
    const element = '<li>Item</li>';
    // Append the new element to the <ul> with class 'my_list'
    $('ul.my_list').append(element);
  });
});

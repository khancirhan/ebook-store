/* 
  Adds the active class and changes the fontawesome book icon of the <subjects> sidebar.
*/

// Split the URL at '/' and save different parts in an array
let urlArr = document.URL.split("/");

// Get the last element of the array (last element corresponds to the unique id of the subject)
let subjID = urlArr[urlArr.length - 1];

// Get the DOM element with the specified id
var el = document.getElementById("subject" + subjID);   // subject0, subject1, ...

// Add active class
el.classList.toggle("active");

// Change book icon
el.firstElementChild.classList.remove("fa-book");
el.firstElementChild.classList.add("fa-book-open");

/*
  Displays the current year in the footer.
*/

const year = new Date().getFullYear();    // Get current year
document.querySelector("footer .year").textContent = year;

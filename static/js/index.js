document.addEventListener("DOMContentLoaded", function() {
    // Get current URL
    const currentUrl = window.location.href;
  
    // Get all navbar links
    const navLinks = document.querySelectorAll('.navbar a');
  
    // Loop through links and mark the active one
    navLinks.forEach(link => {
      if (link.href === currentUrl) {
        link.classList.add('active');
      }
    });
  });
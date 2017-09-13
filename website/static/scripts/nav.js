var mainMenu = document.querySelector(".ddNavbar");
function setMenuOpen (showMenu) {
    showMenu ? mainMenu.classList.add("mobile-open") : mainMenu.classList.remove("mobile-open");
}

var navToggle = document.querySelector(".nav-toggle");
navToggle.addEventListener("click", function() {
    if(navToggle.classList.contains("open")) {
        // Close up
        navToggle.classList.remove("open");
        setMenuOpen(false);
    } else {
        // Show it all
        navToggle.classList.add("open");
        setMenuOpen(true);
    }
}, true);

/* See https://codepen.io/parrotmac/pen/eEajYz for demo */
// const dropDownListLinks = document.querySelectorAll("li.dropdown>a");
//
// for(let i = 0; i < dropDownListLinks.length; i++) {
//   dropDownListLinks[i].addEventListener("click", event => {
//     const _li = event.target.parentElement;
//     if(_li.classList.contains("open")) {
//       _li.classList.remove("open")
//     } else {
//       const _allDropdowns = _li.parentElement.querySelectorAll(".dropdown");
//       for(let j = 0; j < _allDropdowns.length; j++) {
//         _allDropdowns[j].classList.remove("open")
//       }
//       _li.classList.add("open")
//     }
//   }, false)
// }

var mainMenu = document.querySelector(".hoverDropdownNavbar");
function setMenuOpen (showMenu) {
    showMenu ? mainMenu.classList.add("mobile-open") : mainMenu.classList.remove("mobile-open");
}

document.getElementById("nav-toggle").addEventListener("click", function(event) {
    var toggleBtn = event.target;
    if(toggleBtn.classList.contains("open")) {
        // Close up
        toggleBtn.classList.remove("open");
        setMenuOpen(false);
    } else {

        toggleBtn.classList.add("open");
        setMenuOpen(true);
    }
}, false);

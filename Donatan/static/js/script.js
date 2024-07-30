
// ------------ Mobile Black Icon Phone ------------ >
// JS goes here
document.getElementById("contactBtn").addEventListener("click", function () {
  const menu = document.getElementById("contactMenu");
  menu.classList.toggle("show");
});

document.getElementById("closeBtn").addEventListener("click", function () {
  const menu = document.getElementById("contactMenu");
  menu.classList.remove("show");
});

document.addEventListener("click", function (event) {
  const menu = document.getElementById("contactMenu");
  const btn = document.getElementById("contactBtn");
  if (!menu.contains(event.target) && !btn.contains(event.target)) {
      menu.classList.remove("show");
  }
});

// ------------ End Mobile Black Icon Phone ------------ >


document.addEventListener('DOMContentLoaded', function () {
  const mobileNavButton = document.querySelector('.btn-mobile-nav');
  const header = document.querySelector('.header');

  mobileNavButton.addEventListener('click', function () {
      header.classList.toggle('nav-open');
  });
});




// ------------------------------------------------- >



// --------------- Mobile Version Galley --------------------------- >
var swiper = new Swiper(".swiper-container", {
  pagination: {
      el: ".swiper-pagination",
      clickable: true,
  },
  loop: true,

});
// --------------- End Mobile Version Galley --------------------------- >














// ------------ Testimonials ------------ >

var cards = $('#card-slider .slider-item').toArray();

startAnim(cards);

function startAnim(array){
    if(array.length >= 4 ) {
        TweenMax.fromTo(array[0], 0.5, {x:0, y: 0, opacity:0.75}, {x:0, y: -120, opacity:0, zIndex: 0, delay:0.03, ease: Cubic.easeInOut, onComplete: sortArray(array)});

        TweenMax.fromTo(array[1], 0.5, {x:79, y: 125, opacity:1, zIndex: 1}, {x:0, y: 0, opacity:0.75, zIndex: 0, boxShadow: '-5px 8px 8px 0 rgba(82,89,129,0.05)', ease: Cubic.easeInOut});

        TweenMax.to(array[2], 0.5, {bezier:[{x:0, y:250}, {x:65, y:200}, {x:79, y:125}], boxShadow: '-5px 8px 8px 0 rgba(82,89,129,0.05)', zIndex: 1, opacity: 1, ease: Cubic.easeInOut});

        TweenMax.fromTo(array[3], 0.5, {x:0, y:400, opacity: 0, zIndex: 0}, {x:0, y:250, opacity: 0.75, zIndex: 0, ease: Cubic.easeInOut}, );
    } else {
        $('#card-slider').append('<p>Sorry, carousel should contain more than 3 slides</p>')
    }
}

function sortArray(array) {
    clearTimeout(delay);
    var delay = setTimeout(function(){
        var firstElem = array.shift();
        array.push(firstElem);
        return startAnim(array);
    },3000)
}



// ------------ End Testimonials ------------ >










// Current year

const yearEl = document.querySelector(".year");
const currentYear = new Date().getFullYear();
yearEl.textContent = currentYear;

//////////////////////////////////////////////

// Make mobile navigation work

const btnNavEl = document.querySelector(".btn-mobile-nav");
const headerEl = document.querySelector(".header");

btnNavEl.addEventListener("click", function () {
    headerEl.classList.toggle("nav-open");
});

///////////////////////////////////////////////

// Smooth scrolling animation

const allLinks = document.querySelectorAll("a:link");

allLinks.forEach(function (link) {
    link.addEventListener("click", function (e) {
        e.preventDefault();
        const href = link.getAttribute("href");

        // Scroll bakc to top
        if (href == "#")
            window.scrollTo({
                top: 0,
                behavior: "smooth",
            });

        // Scroll to other links
        if (href !== "#" && href.startsWith("#")) {
            const sectionEl = document.querySelector(href);
            sectionEl.scrollIntoView({ behavior: "smooth" });
        }

        // Close mobile navigation
        if (link.classList.contains("main-nav-link"))
            headerEl.classList.toggle("nav-open");
    });
});
////////////////////////////////////////////////////

// Sticky navigation
const sectionHeroEl = document.querySelector(".section-hero");

const obs = new IntersectionObserver(
    function (entries) {
        const ent = entries[0];
        console.log(ent);

        if (ent.isIntersecting === false) {
            document.body.classList.add("sticky");
        }

        if (ent.isIntersecting) {
            document.body.classList.remove("sticky");
        }
    },
    {
        // In the viewport
        root: null,
        threshold: 0,
        rootMargin: "-80px",
    }
);
obs.observe(sectionHeroEl);

///////////////////////////////////////////////////////////
// Fixing flexbox gap property missing in some Safari versions
function checkFlexGap() {
    var flex = document.createElement("div");
    flex.style.display = "flex";
    flex.style.flexDirection = "column";
    flex.style.rowGap = "1px";

    flex.appendChild(document.createElement("div"));
    flex.appendChild(document.createElement("div"));

    document.body.appendChild(flex);
    var isSupported = flex.scrollHeight === 1;
    flex.parentNode.removeChild(flex);
    console.log(isSupported);

    if (!isSupported) document.body.classList.add("no-flexbox-gap");
}
checkFlexGap();


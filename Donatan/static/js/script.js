
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

// --------------- Animation ------------ >
    document.addEventListener('DOMContentLoaded', () => {
        const elements = document.querySelectorAll(
            '.grid--2-cols, .grid--2-cols-reverse, .hero-title, .hero-button, .carousel-container, .grid-item, .product-container'
        );

        elements.forEach(element => {
            if (element.classList.contains('grid--2-cols') || element.classList.contains('grid--2-cols-reverse')) {
                element.classList.add('hidden');
            }
        });

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (entry.target.classList.contains('grid--2-cols-reverse')) {
                        entry.target.classList.add('slide-in-right');
                    } else if (entry.target.classList.contains('grid--2-cols')) {
                        entry.target.classList.add('slide-in-left');
                    } else {
                        entry.target.classList.add('slide-in');
                    }
                    entry.target.classList.remove('hidden');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        elements.forEach(element => {
            observer.observe(element);
        });

        const loadingScreen = document.getElementById('loading-screen');
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 2000);
    });    document.addEventListener('DOMContentLoaded', () => {
        const elements = document.querySelectorAll(
            '.grid--2-cols, .grid--2-cols-reverse, .hero-title, .hero-button, .carousel-container, .grid-item, .product-container'
        );

        elements.forEach(element => {
            if (element.classList.contains('grid--2-cols') || element.classList.contains('grid--2-cols-reverse')) {
                element.classList.add('hidden');
            }
        });

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (entry.target.classList.contains('grid--2-cols-reverse')) {
                        entry.target.classList.add('slide-in-right');
                    } else if (entry.target.classList.contains('grid--2-cols')) {
                        entry.target.classList.add('slide-in-left');
                    } else {
                        entry.target.classList.add('slide-in');
                    }
                    entry.target.classList.remove('hidden');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        elements.forEach(element => {
            observer.observe(element);
        });

        const loadingScreen = document.getElementById('loading-screen');
        setTimeout(() => {
            loadingScreen.style.display = 'none';
        }, 2000);
    });

//  ------------- End Animation ------------ >

// --------------- Mobile Version Galley --------------------------- >
var swiper = new Swiper(".swiper-container", {
  pagination: {
      el: ".swiper-pagination",
      clickable: true,
  },
  loop: true,

});
// --------------- End Mobile Version Galley --------------------------- >

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





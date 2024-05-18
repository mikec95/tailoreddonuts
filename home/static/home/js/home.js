document.addEventListener("DOMContentLoaded", function () {
  const fadeElements = document.querySelectorAll(".fade-in");
  function checkFade() {
    fadeElements.forEach((element) => {
      const elementTop = element.getBoundingClientRect().top;
      const elementBottom = element.getBoundingClientRect().bottom;

      const isVisible =
        (elementTop >= 0 && elementTop <= window.innerHeight) ||
        (elementBottom >= 0 && elementBottom <= window.innerHeight);

      if (isVisible) {
        element.classList.add("visible");
      } else {
        element.classList.remove("visible");
      }
    });
  }
  window.addEventListener("scroll", checkFade);
  checkFade();
});

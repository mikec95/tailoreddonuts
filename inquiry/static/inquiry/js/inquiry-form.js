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

  document
    .getElementById("phone-number")
    .addEventListener("input", function (e) {
      let inputValue = e.target.value.replace(/[^\d]/g, "");

      if (inputValue.length === 11) {
        inputValue = inputValue.replace(
          /^(\d)(\d{3})(\d{3})(\d{4})$/,
          "$1-$2-$3-$4"
        );
      } else if (inputValue.length === 10) {
        inputValue = inputValue.replace(/^(\d{3})(\d{3})(\d{4})$/, "$1-$2-$3");
      }

      e.target.value = inputValue;
    });

  const successMessage = document.querySelector(".success-message");
  setTimeout(() => {
    successMessage.classList.remove("show");
  }, 3000);
});

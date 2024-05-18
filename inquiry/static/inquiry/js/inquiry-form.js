document.addEventListener("DOMContentLoaded", function () {
  // Phone number input formatting
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

  // Hide success message after a delay
  const successMessage = document.querySelector(".success-message");
  if (successMessage) {
    setTimeout(() => {
      successMessage.classList.remove("show");
    }, 3000);
  }

  // Disable submit button while form is submitting
  document
    .getElementById("contact-form")
    .addEventListener("submit", function () {
      const submitButton = document.querySelector(".submit-button");
      submitButton.disabled = true; // Disable the submit button
      submitButton.textContent = "Sending..."; // Change button text
    });
});

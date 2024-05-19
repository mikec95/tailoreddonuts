// Get references to modal elements and fade-in elements
const modal = document.getElementById("modal");
const fullImage = document.getElementById("fullImage");
const modalCaption = document.getElementById("modalCaption");
const modalDescription = document.getElementById("modalDescription");
const closeModalButton = document.getElementById("closeModalButton");
const fadeElements = document.querySelectorAll(".fade-in");
const modalContainer = document.querySelector(".modal-container");

// Function to close and reset the modal state.
// Reason being that after the image was closed,
// we were not able to re-open the image without refreshing
// so we have to reset the css here.
function closeAndResetModal() {
  modal.classList.remove("active");
  modal.classList.add("inactive");
  document.body.style.overflow = "visible";
  fullImage.src = "";
  modalCaption.textContent = "";
  modalDescription.textContent = "";
}

/**
 * Opens the modal with the specified image and details.
 * @param {HTMLElement} element - The element that was clicked to open the modal.
 */
function openModal(element) {
  // Set the full image, caption, and description from the clicked element's data attributes
  fullImage.src = element.dataset.fullImage;
  //   modalCaption.textContent = element.dataset.title;
  //   modalDescription.textContent = element.dataset.description;

  // Remove the 'inactive' class and add the 'active' class to activate the modal
  modal.classList.remove("inactive");
  modal.classList.add("active");
  document.body.style.overflow = "hidden";
}

/**
 * Checks if fade-in elements are within the viewport and toggles the 'visible' class.
 */
function checkFade() {
  fadeElements.forEach((element) => {
    const elementTop = element.getBoundingClientRect().top;
    const elementBottom = element.getBoundingClientRect().bottom;
    const isVisible =
      (elementTop >= 0 && elementTop <= window.innerHeight) ||
      (elementBottom >= 0 && elementBottom <= window.innerHeight);

    // Toggle the 'visible' class based on the element's visibility
    element.classList.toggle("visible", isVisible);
  });
}

// Set up event listeners once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Close the modal when the close button is clicked
  closeModalButton.addEventListener("click", closeAndResetModal);
  modalContainer.addEventListener("click", closeAndResetModal);

  // Check fade-in elements' visibility on scroll
  window.addEventListener("scroll", checkFade);

  // Initial check for fade-in elements' visibility
  checkFade();
});

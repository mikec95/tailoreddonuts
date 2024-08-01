$(document).ready(function () {
  $(".navbar-toggler").click(function () {
    var $this = $(this);

    // Reset the animation
    $this.find(".navbar-toggler-icon").removeClass("animate");

    // Force reflow to restart animation
    void $this.find(".navbar-toggler-icon")[0].offsetWidth;

    // Add the animation class
    $this.find(".navbar-toggler-icon").addClass("animate");

    // Toggle the 'open' class and the 'collapsed' class
    $this.toggleClass("open");
    $this.toggleClass("collapsed");
  });

  // Close the navbar when clicking outside of it
  $(document).click(function (event) {
    if (!$(event.target).closest(".navbar-toggler, .navbar-collapse").length) {
      if ($(".navbar-toggler").hasClass("open")) {
        $(".navbar-toggler").removeClass("open");
        $(".navbar-toggler-icon").removeClass("animate");
        $("#navbarContent").removeClass("show");
        $(".navbar-toggler").addClass("collapsed");
      }
    }
  });
});

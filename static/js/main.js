document.addEventListener("DOMContentLoaded", () => {

  /* ============================
     AUTO REVIEWS (Every 5 sec)
  ============================ */

  const slider = document.getElementById("reviewsSlider");
  if (!slider) return;

  const reviews = Array.from(slider.querySelectorAll(".review"));
  if (reviews.length <= 1) return;

  let current = reviews.findIndex(r => r.classList.contains("is-active"));
  if (current < 0) current = 0;

  function show(index) {
    reviews[current].classList.remove("is-active");
    current = index;
    reviews[current].classList.add("is-active");
  }

  setInterval(() => {
    show((current + 1) % reviews.length);
  }, 5000);

});


document.addEventListener("DOMContentLoaded", () => {

  /* ============================
     AUTO REVIEWS (Every 5 sec)
  ============================ */

  const slider = document.getElementById("reviewsSlider");
  if (!slider) return;

  const reviews = Array.from(slider.querySelectorAll(".review"));
  if (reviews.length <= 1) return;

  let current = reviews.findIndex(r => r.classList.contains("is-active"));
  if (current < 0) current = 0;

  function show(index) {
    reviews[current].classList.remove("is-active");
    current = index;
    reviews[current].classList.add("is-active");
  }

  setInterval(() => {
    show((current + 1) % reviews.length);
  }, 5000);

});

document.addEventListener("DOMContentLoaded", function (event) {
    const slides = document.querySelectorAll(".slide");
    const slides_pagination = document.getElementsByClassName("slider-pagination-page");
    const prevButton = document.getElementsByClassName("slider-prev");
    const nextButton = document.getElementsByClassName("slider-next");

    slides.forEach((slide, indx) => {
        slide.style.transform = `translateX(${indx * 100}%)`;
    });
    let curSlide = 0;
    let maxSlide = slides.length - 1;

    nextButton[0].addEventListener("click", (event) => {
        if (curSlide === maxSlide) {
            curSlide = 0;
        } else {
            curSlide++;
        }
        slides.forEach((slide, indx) => {
            slide.style.transform = `translateX(${100 * (indx - curSlide)}%)`;
        });
    });

    prevButton[0].addEventListener("click", () => {
        if (curSlide === 0) {
            curSlide = maxSlide;
        } else {
            curSlide--;
        }
        //   move slide by 100%
        slides.forEach((slide, indx) => {
            slide.style.transform = `translateX(${100 * (indx - curSlide)}%)`;
        });
    });

    // Pagination function
    for (var i = 0; i < slides_pagination.length; i++) {
        var self = slides_pagination[i];

        self.addEventListener('click', function (event) {
            // get slide number
            let clickedSlide = event.target.innerHTML - 1
            curSlide = clickedSlide;

            slides.forEach((slide, indx) => {
                slide.style.transform = `translateX(${100 * (indx - curSlide)}%)`;
            });
        }, false);
    }
});


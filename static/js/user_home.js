let slideIndex = 1;
const slides = document.getElementsByClassName("mySlides");

showSlidesAuto();

function plusSlides(n) {
  showSlidesManual(slideIndex += n);
}

function showSlidesAuto() {
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) { slideIndex = 1; }
  slides[slideIndex - 1].style.display = "block";  
  setTimeout(showSlidesAuto, 5000);
}

function showSlidesManual(n) {
  if (n > slides.length) { slideIndex = 1; }
  if (n < 1) { slideIndex = slides.length; }
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slides[slideIndex - 1].style.display = "block";
}

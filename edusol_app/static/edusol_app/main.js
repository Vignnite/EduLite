window.addEventListener("scroll", function () {
  const header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 0);
});

var sub = document.getElementsByClassName("logo_pic");
if (document.querySelector("header").classList.contains("sticky")) {
  var img = document.getElementById("edulog");
  img.src = "Img/Logos/logo-black.png";
}

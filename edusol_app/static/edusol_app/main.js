window.addEventListener("scroll", function () {
  const header = document.querySelector("header");
  header.classList.toggle("sticky", window.scrollY > 0);
});

// var sub = document.getElementsByClassName("logo_pic");
// if (document.querySelector("header").classList.contains("sticky")) {
//   var img = document.getElementById("edulog");
//   img.src = "Img/Logos/logo-black.png";
// }


function cutoff_calc(){
  var m = document.querySelector('[name= "Maths"]').value;
  var p = document.querySelector('[name="Physics"]').value;
  var c = document.querySelector('[name="Chemistry"]').value;
  var fin = (float(m) + (float(p)/2) + (float(c)/2));
  document.getElementById("cut").innerHTML = float(fin)/2;
  console.log(fin/2)
  alert(fin/2);
  // +" "+p+""+c+""+fin);
}


// document.addEventListener('DOMContentLoaded', function () {
//   var checkbox = document.querySelector('input[type="checkbox"]');

//   checkbox.addEventListener('change', function () {
//     if (checkbox.checked) {
//       console.log('Checked');
//     } else {
//       console.log('Not checked');
//     }
//   });
// });

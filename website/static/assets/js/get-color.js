// console.log("Hello World!");
// const img = document.querySelectorAll("img.card-img-top");
// console.log(img);
// const colorThief = new ColorThief();
// img.forEach((img) => {
//   console.log(img);
//   console.log(img.complete);
//   if (img.complete) {
//     colorThief.getColor(img);
//   } else {
//     img.addEventListener("load", function () {
//       colorThief.getColor(img);
//     });
//   }
// });

console.log("get-color.js");
const colorThief = new ColorThief();
const img = document.querySelectorAll("img.card-img-top");
const background = document.querySelectorAll(".card");

img.forEach((img, index) => {
  console.log(img.complete, index, img);
  let color;
  if (img.complete) {
    color = colorThief.getColor(img);
    setBackgroundColor(background[index], color);
  } else {
    img.addEventListener("load", function () {
      color = colorThief.getColor(img);
      console.log(color);
      setBackgroundColor(background[index], color);
    });
  }
});

function setBackgroundColor(element, color) {
  element.style.backgroundColor = `rgb(${color[0]}, ${color[1]}, ${color[2]}, 0.6)`;
}

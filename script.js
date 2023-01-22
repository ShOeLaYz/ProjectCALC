const userInput = document.getElementById('userInput')
let expression = ''

function press(num) {
  expression += num
  userInput.value = expression
}

function erase() {
  expression = ''
  userInput.value = expression
}

function equal() {
  userInput.value = eval(expression)
  expression = ''
}
function ca() {
  var x = document.getElementById("cookie");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function cd() {
  location.replace("about:blank")
}
function cooki() {
  location.assign("/cookiepolicy.html")
}
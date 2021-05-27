let newgame = document.querySelector("#newgame");
let roll = document.querySelector("#roll");
let out = document.querySelector("#out");
let score = document.querySelector("#score");

newgame.addEventListener("click", newgameclbk);
roll.addEventListener("click", rollclbk);
out.addEventListener("click", outclbk);

function newgameclbk(e) {}

function rollclbk(e) {}

function outclbk(e) {
  window.location = "/logout";
}

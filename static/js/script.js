let newgame = document.querySelector("#newgame");
let roll = document.querySelector("#roll");
let out = document.querySelector("#out");
let scoretxt = document.querySelector("#score");
let dice = document.querySelector("#dice");
let listscors = document.querySelector("#listscors");

newgame.addEventListener("click", newgameclbk);
roll.addEventListener("click", rollclbk);
out.addEventListener("click", outclbk);
dice.src = `/static/imgs/dice-0.png`;
console.log("starting ..............");
let score = 0;
let scores = [];

function newgameclbk(e) {
  roll.addEventListener("click", rollclbk);
  dice.src = `/static/imgs/dice-0.png`;
  score = 0;
}

function rollclbk(e) {
  let n = Math.floor(Math.random() * 6) + 1;
  dice.src = `/static/imgs/dice-${n}.png`;
  if (n != 1) {
    score += n;
    scoretxt.innerHTML = `score: ${score}`;
  } else {
    scores.push(score);
    let p = document.createElement("p");
    p.innerText = score;
    listscors.appendChild(p);

    scoretxt.innerHTML = `GAME OVER`;
    roll.removeEventListener("click", rollclbk);
    score = 0;
  }
}

function outclbk(e) {
  console.log(scores);

  // ajax post scores as json

  window.location = "/logout";
}

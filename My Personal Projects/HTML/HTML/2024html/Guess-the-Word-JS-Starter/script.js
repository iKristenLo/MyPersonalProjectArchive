/* ~~~~ Constants ~~~~ */
const wordList = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree", "Weedle", "Kakuna", "Beedrill", "Pidgey", "Pidgeotto", "Pidgeot", "Rattata", "Raticate", "Spearow", "Fearow", "Ekans", "Arbok", "Pikachu", "Raichu", "Sandshrew", "Sandslash", "Nidoran", "Nidorina", "Nidoqueen", "Nidoran", "Nidorino", "Nidoking", "Clefairy", "Clefable", "Vulpix", "Ninetales", "Jigglypuff", "Wigglytuff", "Zubat", "Golbat", "Oddish", "Gloom", "Vileplume", "Paras", "Parasect", "Venonat", "Venomoth", "Diglett", "Dugtrio", "Meowth", "Persian", "Psyduck", "Golduck", "Mankey", "Primeape", "Growlithe", "Arcanine", "Poliwag", "Poliwhirl", "Poliwrath", "Abra", "Kadabra", "Alakazam", "Machop", "Machoke", "Machamp", "Bellsprout", "Weepinbell", "Victreebel", "Tentacool", "Tentacruel", "Geodude", "Graveler", "Golem", "Ponyta", "Rapidash", "Slowpoke", "Slowbro", "Magnemite", "Magneton", "Farfetch'd", "Doduo", "Dodrio", "Seel", "Dewgong", "Grimer", "Muk", "Shellder", "Cloyster", "Gastly", "Haunter", "Gengar", "Onix", "Drowzee", "Hypno", "Krabby", "Kingler", "Voltorb", "Electrode", "Exeggcute", "Exeggutor", "Cubone", "Marowak", "Hitmonlee", "Hitmonchan", "Lickitung", "Koffing", "Weezing", "Rhyhorn", "Rhydon", "Chansey", "Tangela", "Kangaskhan", "Horsea", "Seadra", "Goldeen", "Seaking", "Staryu", "Starmie", "Mr. Mime", "Scyther", "Jynx", "Electabuzz", "Magmar", "Pinsir", "Tauros", "Magikarp", "Gyarados", "Lapras", "Ditto", "Eevee", "Vaporeon", "Jolteon", "Flareon", "Porygon", "Omanyte", "Omastar", "Kabuto", "Kabutops", "Aerodactyl", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dratini", "Dragonair", "Dragonite", "Mewtwo", "Mew"]

/* ~~~~ Variables ~~~~ */
let word
let clue
let message
let lives

/* ~~~~ DOM Elements ~~~~ */
// Store the following HTML elements in variables:
const resetBtn = document.querySelector("#reset-btn")
const hintBtn = document.querySelector("#hint-btn")
const clueEl = document.querySelector("#clue")
const messageEl = document.querySelector("#message")
const livesEl = document.querySelector("#lives")
const textFieldEl = document.querySelector("#text-field")
const submitButton = document.querySelector("#submit-btn")

/* ~~~~ Event Listeners ~~~~ */
// add an event listener to the submit button
// when clicked, it should call a handleSubmit function
submitButton.addEventListener("click",handleSubmit)
resetBtn.addEventListener("click",handleReset)
hintBtn.addEventListener("click",handleHint)

/* ~~~~ Functions ~~~~ */
init()

function init() {
  // set the number of lives for the player
  lives = 5
  // set the game's starting prompt message
  message = "Type A Letter And Press Submit!"
  word = getRandomWord()
  clue = createClue(word)
  render()
}

function getRandomWord() {
  const idx = Math.floor(Math.random()*wordList.length)
  return wordList[idx].toUpperCase()
}

function createClue(str) {
  let output = ""
  for (let i = 0; i < str.length; i++){
    output += "_"
  }
  return output
}

function render() {
  renderClue()
  renderMsg()
  renderLives()
}

function renderClue() {
  const arr = clue.split("")
  clueEl.innerText = arr.join(" ")
}

function renderMsg() {
  messageEl.innerText = message
  
}

function renderLives() {
  livesEl.innerText = "You Still Have " + lives + " lives Left"
}

function handleSubmit(evt) {
  // prevent the page from automatically refreshing
  evt.preventDefault()
  // store the player's input in a variable
  let input = textFieldEl.value.toUpperCase()
  //console.log(input)
  checkLetter(input)
  // after checking the player's input, reset the text field
  textFieldEl.value = ""
  // check if a new round needs to be started
  if (word === clue){
    message = "You Win"
    setTimeout(init,5000)
  }
  if (lives === 0){
    message = "You Lost! The Word Was: " + word
    setTimeout(init,2000)
  }
  
  // render the updated game status
  render()
}

function handleReset(evt){
  evt.preventDefault()
  message = "You Have Just Reset The Game! The Word Was: " + word
  renderMsg()
  setTimeout(init,3000)
}

function handleHint(evt){
  evt.preventDefault()
  updatefll()
  
}
function updatefll(){
  let newClue = ""
  let firstltr = word[0]
  let lastltr = word.at(-1)
}
function checkLetter(ltr) {
  if (ltr === word){
    clue = word
    return
  }
  // update the clue with any newly revealed letters
  let found = false
  for (let i = 0; i < word.length; i++){
    if (word[i] ===ltr){
      found = true
    }
  }
  if (found === false){
    lives -= 1
    message = "Not In Word!"
  }
  let newClue = ""
  
  for (let i = 0; i < word.length; i++){
     if (word[i] === ltr){
       newClue += ltr
     } 
    else{
      newClue += clue[i]
    }
  }
  clue = newClue
  // if the letter wasn't in the word, 
    // deduct a life 
    // notify the player their submission was incorrect
}
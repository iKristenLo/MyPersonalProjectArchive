console.log("Hello")
function capsF(word){
  output = word[0].toUpperCase()
  for (let i = 1;i < word.length;i++){
    output += word[i].toLowerCase()
  }
  return output
}
const eeveeData = {
  id: 133,
  primaryImage:  "https://static.wikia.nocookie.net/pokemon/images/8/88/Char-Eevee.png",
  secoundaryImage: "https://www.serebii.net/pokemonsleep/pokemon/133.png",
  name: "Eevee"
}

function addPokemon(){
  const idx = Math.floor(Math.random()*280)+1
  console.log(idx)
  fetch(`https://pokeapi.co/api/v2/pokemon/${idx}`)
  .then(res => res.json())
  .then(data => {
    console.log(data)
    const cardSection = document.querySelector("#pokemon-dex")
    const newCard = document.createElement("div")
    const newName = document.createElement("p")
    newName.textContent = capsF(data.name)
    const newImage = document.createElement("img")
    newImage.src = data.sprites.front_shiny
    // console.log(data.name,data.sprites.front_default)
    newCard.append(newName)
    newCard.append(newImage)
    cardSection.append(newCard)
  })
    
        
}


function addCustomPkm(evt){
  evt.preventDefault()
  const textField = document.querySelector("#PokiSearch")
  console.log(textField.value)
  const userSelection = textField.value.toLowerCase()
  fetch(`https://pokeapi.co/api/v2/pokemon/${userSelection}`)
  .then(res => res.json())
  .then(data => {
    console.log(data)
    const cardSection = document.querySelector("#pokemon-dex")
    const newCard = document.createElement("div")
    const newName = document.createElement("p")
    const newImage = document.createElement("img")

    const randomNum = Math.random()
    if(randomNum > 0.1){
      newImage.src = data.sprites.front_default
      newName.textContent = capsF(data.name)
    }
    else{
       newImage.src = data.sprites.front_shiny
      newName.textContent = capsF(data.name) + " Shiny"
    }
    // console.log(data.name,data.sprites.front_default)
    newCard.append(newName)
    newCard.append(newImage)
    cardSection.append(newCard)
    const invalidMsg = document.querySelector("#invalid-msg")
    invalidMsg.style.visibility = "hidden"
  })
  .catch(err => {
    console.log(err)
    //textField.value = "Not Valid Pokemon"
    const invalidMsg = document.querySelector("#invalid-msg")
    invalidMsg.style.visibility = "visible"
  })
  textField.value = ""

}






const name = document.querySelector(".name")
name.textContent = eeveeData.name

const picdex = document.querySelector(".picdex")
picdex.src = eeveeData.primaryImage

const genbt = document.querySelector("#genbt")
genbt.addEventListener("click", addPokemon )

const addbt = document.querySelector("#addbt")
addbt.addEventListener("click", addCustomPkm)



  // console.log("Click Found!")
  // picdex.src = eeveeData.secoundaryImage
// })
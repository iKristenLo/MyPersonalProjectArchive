let gameOverMsg = document.querySelector("#game-over")



let player
let img
let floor
let platforms
let score = 0
let display
let platidx = 0
let gamePlaying = true
let gameOverSc

function preload(){
  img = loadImage("./Pics/chick-a.png")
}


function setup() {
  createCanvas(400, 400);
  world.gravity.y = 10
  player = new Sprite()
  player.x = 200
  player.y = 100
  player.image = img
  player.scale = 0.5
  player.w = 70
  player.h = 70
  player.debug = true
  
  floor = new Sprite()
  floor.y = 390
  floor.x = 200
  floor.w = 800
  floor.collider = "static"
  
  platforms = new Group()
  platforms.color = "red"
  platforms.collider = "static"
  platforms.width = 100
  platforms.height = 100
  //let p1 = new platforms.Sprite()
  player.collides(platforms,updScore)

  //p1.y = 100
  //p1.x = 100
  //p1.idx = platidx
  platidx += 1
  for(let i = 0; i < 5; i++){
    let nP = new platforms.Sprite()
    nP.y = 100 - (300*i)
    nP.x = Math.random()*(400-100)+100
    nP.idx = platidx
    platidx += 1
  }
  display = new Sprite()
  display.collider = "none"
  display.x = 350
  display.y = 300
  display.text = 0
  display.textSize = 40

  gameOverSc = new Sprite()
  gameOverSc.collider = "none"
  gameOverSc.textSize = 80
  gameOverSc.visible = false
  gameOverSc.text = "Game Over!"
  gameOverSc.width = 0
  gameOverSc.height = 0

  
}

function draw() {
  background(220);
  if(kb.pressing("a")){
    player.x -= 5
    player.mirror.x = true
  }
  if(kb.pressing("d")){
    player.x += 5
    player.mirror.x = false
    
  }
  if (kb.pressed(" ") && player.colliding(floor)||
      kb.pressed(" ") && player.colliding(platforms)){
    player.vel.y -= 10
  }
  if (player.x > 450){
    player.x = 0
  }
  if (player.x < -50){
    player.x = 400
  }
  camera.y = player.y
  const lastPlatform = platforms[platforms.length - 1]
  if (lastPlatform && lastPlatform.y > player.y){
    let nP = new platforms.Sprite()
    nP.y = lastPlatform.y - 300
    nP.x = Math.random()*(400-100)+100
    nP.idx = platidx
    platidx += 1
  }
  display.text = score
  display.y = camera.y + 170
  gameOverSc.y = camera.y
}
function updScore(player,platform){
  let newScore = platform.idx
  if (newScore < score){
    console.log("Game_Over!")
    gameOverSc.visible = true
    //floor = null
    platforms.removeAll()
    floor.collider = "none"
    gameOverMsg.style.visibility = "visible"
    
  }
  score = platform.idx
  console.log("Running!")
}
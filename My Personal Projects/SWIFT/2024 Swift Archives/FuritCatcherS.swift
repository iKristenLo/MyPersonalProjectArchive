// Fruit Catcher Game
//HW Enhance The Game



import Foundation

// define the basket size and init Pos.

let basketWidth = 3
var basketPosition = 5

// define the game area width
let gameAreaWidth = 10

// init score and timer
var score = 0
var timer = 30

// Func to print the game area

func printGameArea(fruitPostiton: Int){
  for i in 1...gameAreaWidth{
    if i == fruitPostiton{
      print("F", terminator: "")
    } else if i >= basketPosition && i < basketPosition + basketWidth{
      print("B", terminator: "")
    }else{
      print("-", terminator: "")
    }
    
  }
  print()
}

// Function to move basket

func moveBasket(direction: String){
  if direction == "left" && basketPosition > 1{
    basketPosition -= 1
  } else if direction == "right" && basketPosition + basketWidth <= gameAreaWidth {
      basketPosition += 1
  }
}

// Bonus Scoring System(Every 3inRow +5 Points)
  
  func Bonus(){
    if score > 1{
      print("Bonus")
    }
  }


// Main game loop

while timer > 0{
  //gen a random fruit pos.
  let fruitPosition = Int.random(in:1...gameAreaWidth)

  //print the game area
  printGameArea(fruitPostiton: fruitPosition)

  //check if the fruit is caught
  if fruitPosition >= basketPosition && fruitPosition < basketPosition + basketWidth{
    score += 1
    print("You Have Caught a fruit! Score: \(score)*")
  }else{
      print("Missed Fruit")
  }

  
  // Move the basket on user input
    print("Movebasket (left/right): ", terminator:"")
    if let input = readLine(),(input == "left" || input == "right") {
  } else {
      print("Invalid Input")
  }

  // Decrease the timer
  timer -= 1
  print("Time Remaining : \(timer) secounds")
  print()

  //bonus
  print(Bonus)
}

// Game Over 
print("Game Over Your Score Is \(score).")
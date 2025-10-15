//HW Expand On Game
//QNA Why Is It That Even if The Response Is Correct The Game Reports That Its Incorrect

import Foundation //Imports Foundation

func generateRandomNumber() -> Int {//Generates A # From 1-100
  return Int.random(in: 1...100)//(in: 1...100) Picks A # Between 1-100
}

func startGame(){ //Makes A Func That Holds MainGame "Area"
  var currentNumber = generateRandomNumber() //Makes CurrentNum 
  var score = 0 //The Score Is Originally Set At 0

  print("Welcome To Higher Or Lower") //print 
  print("Try To Guess If The Number Will Be Higher/Lower") //print
  print("Type Higher or Lower Now!") //print

  while true{ //While Loop
    print("The Current Number Is \(currentNumber)). Will The Number Be Higher Or Lower?") //Printing Current Number
   let guess = readLine()?.lowercased() //readLine Is Input in swift
    let nextNumber = generateRandomNumber() //Makes The "nextNumber" 
    print("Next Number Is \(nextNumber).") //Prints The Next Number Lined Up
    if (guess == "higher" && nextNumber > currentNumber) || (guess == "lower" && nextNumber < currentNumber){
      print("You Guessed Right") //24-26 If Response Is Correct!
      score += 1 //After Winning The Round 1 Point Is Awarded
      currentNumber = nextNumber //Grabs Next Number For Game
    } else {//Runs If Response Given Is Wrong
      print("You guessed Incorrectly") //Prints If Input = Wrong
      break //Closes The Game Out
    }
    
    }
  print("Your Total Score was \(score).") 
  }

//main
startGame() //Boots Game From 10th Func Line
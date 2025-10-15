import Foundation 

// list of words for the game

let words = ["swift", "replit", "challenge", "programming", "developer", "framework", "algorithm"]
// Function to pick a random word from the list
func pickRandomWord() -> String{
  return words.randomElement() ?? "swift"
}

// Function to display the current state of the guessed word

func displayWord(word: String, guessedLetters: Set<Character>) -> String {
  var display = ""
  for letter in word{
    if guessedLetters.contains(letter){
      display.append(letter)
    } else{
        display.append("_")
    }
    display.append(" ")
  }
  return display.trimmingCharacters(in: .whitespaces)
}

// function to play the hangman game!

func playHangman(){
  let word = pickRandomWord()
  var attemptsRemaining = 6
  var guessedLetters = Set<Character>()
  var wrongGuesses = Set<Character>()

  while attemptsRemaining > 0 {
    print("\nWord to guess: \(displayWord(word: word, guessedLetters: guessedLetters))")
    print("Wrong guesses: \(wrongGuesses.sorted())")
    print("Attempts remaining: \(attemptsRemaining)")

    print("Enter a letter: ", terminator: "")
    guard let input = readLine(), let guess = input.first, input.count == 1 else {
        print("Please enter a single letter.")
        continue
    }

    if guessedLetters.contains(guess) || wrongGuesses.contains(guess) {
        print("You've already guessed that letter. Try again.")
        continue
    }

    if word.contains(guess){
      guessedLetters.insert(guess)
      if displayWord(word: word, guessedLetters: guessedLetters).replacingOccurrences(of: " ", with: "") == word {
        print("\nCongratulations! You've guess the word: \(word)")
        return
      }

    }else {
      wrongGuesses.insert(guess)
      attemptsRemaining -= 1
      print("Wrong guess.")
    }
  }
  print("\nGame Over! The world was: \(word)")
}

// start the game

playHangman()

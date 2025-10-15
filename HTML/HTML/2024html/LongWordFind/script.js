// console.log("hello james")
let i = 0
i += 1
// console.log("test", i)
//const word = "computer"
// console.log(word.length)


function longWordFinder(arr) {
  let longestWord = ""
  for (let i = 0; i < arr.length; i++) {
    let word = arr[i]
    if (word.length > longestWord.length){
      longestWord = word
    }
  }
  return longestWord
}


const testCase = ["hi","hello","bye"]
console.log(longWordFinder(testCase))
const testCase2 = ["hello","bye","h","friday"]
console.log(longWordFinder(testCase2))
const testCase3 = ["hello"]
console.log(longWordFinder(testCase3))

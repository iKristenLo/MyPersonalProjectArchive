const ansEl = document.querySelector("#ans")
//console.log(ansEl)

// function removeEnds(str){
//   console.log(str.length)
//   output = ""
//   for (let i = 1; i < str.length - 1; i++) {
//     console.log(i,str[i])
//     //output = output + str[i]
//     output += str[i]
    
//   }
//   console.log(output)
//   return output

// }
// const x = removeEnds("hello")
// ansEl.innerText = x

function mostCLtr(str){

  let commonChar = ""
  let maxFreq = 0
  const obj = {}
  for (let i = 0; i <str.length; i++){
    const char = str[i].toLowerCase()
    if (char === " "){
      continue
    }
    //console.log(char)
    if (obj[char] === undefined){
      obj[char] = 1
    
    }
    else{
      obj[char] += 1
    }
  }
  console.log(obj)
  for (let key in obj){
    console.log(key, obj[key])
    if (obj[key] > maxFreq){
      console.log("NewMaxFreq")
      maxFreq = obj[key]
      commonChar = key
    }
  }
  console.log(commonChar)
  return commonChar
}
y = mostCLtr("hello From China My Name Is James")
ansEl.innerText = y
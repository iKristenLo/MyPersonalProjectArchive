function capsF(word){
  output = word[0].toUpperCase()
  for (let i = 1;i < word.length;i++){
    output += word[i].toLowerCase()
  }
  return output
}


console.log(capsF ("EEVEE"))
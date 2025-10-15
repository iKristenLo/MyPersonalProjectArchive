const url = "https://api.openweathermap.org/data/2.5/weather";
const apikey = "d806023fd14fadea31498ed9c5ca6fd7";

$(document).ready(function(){
  weatherFn("Pune");
});

async function weatherFn(Cname){
  const temp = '${url}?q=${cName}&appid=${apiKey}&units=metric';
  try{
    const res = await fetch(temp);
    const data = await res.json();
    if(res.ok){
      weatherShowFn(data);
    }else{
      alert("Data Not Found!")
    }
  }catch(error){
    console.error("An Error Has Occurred");
  }
}
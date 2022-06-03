const API_KEY = "9de30f9ab5c3ba7f28d339c3a3baeb04";


function onGeoOk(position){
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`;
    console.log("you live in", lat, lng);
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const weather = document.querySelector("#weather span:first-child");
            const city = document.querySelector("#weather span:last-child");
            city.innerText = data.name;
            weather.innerText = data.weather[0].main;
        });

}
function onGeoError(){
    alert("i cant find your location");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
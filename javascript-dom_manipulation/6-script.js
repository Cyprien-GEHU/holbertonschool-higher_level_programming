document.addEventListener("DOMContentLoaded", () => {
    fetch("https://swapi-api.hbtn.io/api/people/5/?format=json")
      .then(response => response.json())
      .then(newData => {
        document.getElementById("character").textContent = newData.name;
      })
      .catch(e => console.error("Error:", e));
})

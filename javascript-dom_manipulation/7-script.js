document.addEventListener("DOMContentLoaded", () => {
    fetch("https://swapi-api.hbtn.io/api/films/?format=json")
        .then(reponse => reponse.json())
        .then(newData => {
            const film = newData.results
            const list = document.getElementById("list_movies")
            film.forEach(movie => {
                const li = document.createElement('li');
                li.textContent = movie.title;
                list.appendChild(li);
            });
        })
        .catch(e => console.error("Error:", e));
})
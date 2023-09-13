async function fetcher() {
    const info_fetch = await (await fetch('https://swapi-api.hbtn.io/api/films/?format=json')).json()
    const ul = document.getElementById("list_movies")
    count = info_fetch["count"]
    the_movies = info_fetch["results"]
    for (let i = 0; i < count; i++) {
        the_title = the_movies[i]["title"]
        ul.innerHTML += "<li>" + the_title + "</li>"
    }
}

fetcher()
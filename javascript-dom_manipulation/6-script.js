async function fetcher() {
    const info_fetch = await (await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')).json()
    const div = document.querySelector("#character")
    div.innerHTML = info_fetch["name"]
}

fetcher()
async function fetcher() {
    const info_fetch = await (await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')).json()
    const div = document.getElementById("hello")
    div.innerHTML = info_fetch["hello"]
}

fetcher()
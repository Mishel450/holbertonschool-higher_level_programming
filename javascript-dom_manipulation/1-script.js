function change_on_click() {
    const click = document.getElementById("red_header")
    click.addEventListener("click", function() {
        const header_ = document.querySelector("header")
        header_.style.color = "#FF0000"
    })
}

change_on_click()

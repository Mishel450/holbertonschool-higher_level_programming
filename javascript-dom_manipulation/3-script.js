function ch_class_on_click() {
    const click = document.getElementById("toggle_header")
    click.addEventListener("click", function() { 
        const header = document.querySelector("header")
        header.classList.toggle("red")
        header.classList.toggle("green")
    })
}

ch_class_on_click()

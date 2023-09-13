function ch_class_on_click() {
    const click = document.getElementById("red_header")
    click.addEventListener("click", function() { 
        const header = document.querySelector("header")
        header.classList.add("red")
    })
}

ch_class_on_click()

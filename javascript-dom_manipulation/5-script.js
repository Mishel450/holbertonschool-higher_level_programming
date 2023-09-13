function ch_class_on_click1() {
    const click = document.getElementById("update_header")
    click.addEventListener("click", function() { 
        const header = document.querySelector("header")
        header.textContent = "New Header!!!"
    })
}

ch_class_on_click1()

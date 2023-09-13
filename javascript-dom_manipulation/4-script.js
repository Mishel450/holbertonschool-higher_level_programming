function ch_class_on_click1() {
    const click = document.getElementById("add_item")
    click.addEventListener("click", function() { 
        const lista = document.querySelector(".my_list")
        lista.innerHTML += "<li>Item</li>"
    })
}

ch_class_on_click1()

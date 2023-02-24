function myFunction(id) {
    let redes = document.getElementById(id);
    redes.style.display === "none" ? redes.style.display = "flex" : redes.style.display = "none";
}

function colapse(id){
    let elemento_pai = document.getElementById(id);
    let elementos_filhos = elemento_pai.getElementsByTagName('a');
    console.log(elementos_filhos);
    for (let item of elementos_filhos){
        item.classList.toggle('active');
    }
}

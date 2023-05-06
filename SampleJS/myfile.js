function foo(){
    let name = "Muthuselvan";
    let pTag = document.getElementById("text");
    console.log(pTag.innerHTML)
    pTag.innerHTML = name;

    // change CSS color
    pTag.style.color = "green"

}


function remove(){
    let pTag = document.getElementById("text");
    pTag.remove();
}



function addToList(){
    // creation of an element
    let pTag = document.createElement("p");
    pTag.innerHTML = "Muthu";
    document.getElementById("list").append(pTag)
}
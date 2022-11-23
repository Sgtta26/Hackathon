// const boxOne = document.getElementById("boxOne");
// const boxTwo = document.getElementById("boxTwo");
// const boxThree = document.getElementById("boxThree");
// const boxFour = document.getElementById("boxFour");
// const boxFive = document.getElementById("boxFive");
// const boxSix = document.getElementById("boxSix");
// const boxSeven = document.getElementById("boxSeven");
// const boxEight = document.getElementById("boxEight");
// const boxNine = document.getElementById("boxNine");


let color = ["pink", "orange", "green","yellow","red" ,"purple" ,"blue","black","grey"];
let color2 = ["yellow","blue" ,"grey", "black","pink" , "orange","green","red","purple"];

let counter = 0;
let counter2 = 0;

function addBox (event) {
    let section = document.getElementsByTagName("section")[0];
    for(let i = 0; i < 9; i++){
        let divElement = document.createElement("div"); //ajouter un element 1ere ligne
        divElement.classList.add("dropzone");
        divElement.style.backgroundColor = color[i]; // couleur 

        divElement.addEventListener("dragover", dragOverBox); //3 parties pour drag and drop

        divElement.addEventListener("drop", dropBox);

        section.appendChild(divElement);

    }
}
addBox()


function addBoxElement () {
    let section = document.getElementsByTagName("section")[1];
    for(let i = 0; i < 9; i++){
        let divElement = document.createElement("div"); //ajouter un element 2e ligne
        divElement.setAttribute("draggable","true");
        divElement.classList.add("draggedItem");
        divElement.style.backgroundColor = color2[i]; // couleur

        divElement.setAttribute("id", `box${i}`)

        divElement.addEventListener("dragstart", startDragging); //pour le drag

        section.appendChild(divElement);

    }
}

addBoxElement()


function startDragging(event){
        console.log(event);
        event.dataTransfer.setData("text/plain", event.target.id);
}


function dragOverBox (event){
    event.preventDefault(); //necessite pour que le drop fonctionne 
    console.log('dragOverBox',event.target);
    
}


function dropBox (event){
    
    event.preventDefault();
    console.log('dropBox',event.target);
    const droping = event.dataTransfer.getData("text/plain");
    const droped = document.getElementById(droping)


    if(event.target.style.backgroundColor == droped.style.backgroundColor){ 
        event.target.appendChild(droped);    //boucle pour savoir si ma ligne 1 et 2 corresponde
        counter2++
    }
    else{
        alert('not a match!') // si correspond pas alert 
        counter++
    }

    
    
    if (counter2 === 9 ){ // boucle pour 9 bien places alors gagnant 
        alert ("WINNER")
    }
    

    if (counter === 3 ){   // boucle 3 erreurs perdu
        alert("out of chances...")

    }

}   







// let color_box = 9;  -->comment faire pour que les 9 premieres boites ai les mm couleurs que les 9 autres en aleatoire

// for (let i=0; i < color_box; i++ ){
//     let div = document.createElement("div");
//     div.style.backgroundColor = randomColor();
//     div.addEventListener("click", function(event){
//         color = event.target.style.backgroundColor;
//     })
//     sidebar.appendChild(div)
// }


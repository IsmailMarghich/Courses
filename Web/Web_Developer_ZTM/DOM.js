/*The document object model is what allows javascript to interact with the HTML and CSS of a website
* in this file we will showcase DOM selectors and events*/

/*Selectors is how we can select things from our website*/
console.log(document.getElementsByTagName("h1")); /*we can select by tag name*/
console.log(document.getElementById("first")); /*we can select by ID*/
console.log(document.getElementsByClassName("second")); /*we can select by class*/
/*the tag and class functions dont return the actual element, but a html collection
* there are other functions however that can select the html elements directly*/

console.log(document.querySelector("h1")); /*selects first item with this tag*/
console.log(document.querySelectorAll("p")) /*selects all elements with tag p*/

let paragraph = document.querySelector("p"); /*we can apply methods to elements, but first lets store one*/
console.log(paragraph.getAttribute("id")); /*this will print the attribute 'id' from our p element*/
/*we can change these attributes too*/
paragraph.setAttribute("id", "zero"); /*id becomes zero*/
console.log(paragraph.getAttribute("id")); /*prints zero*/

/*we can also change the style (css) of an element*/
paragraph.style.color = "red"; /*with .style we can access all the css properties of this element, it now turns red*/
paragraph.style.background = "black";

/*the issue with the above code is that it inserts the css into the html, but we want to separate html & css*/
let header = document.querySelector("h1")
/*we can apply css from a css file to an element instead*/
header.className = "title" /*now the header gets css properties from the class title in dom.css*/
console.log(header.classList); /*returns the classes in an element*/
header.classList.remove("title"); /*removes a class*/
header.classList.add("title"); /*adds a class*/
header.classList.toggle("title"); /*we can also toggle the class off instead of removing it*/
header.classList.toggle("title"); /*toggles the class back on*/

/*Events are what allows us to make our website dynamic, javascript listens to events and reacts, for example a mouse click*/
button = document.querySelector("button"); /*select a button from html*/
/*we can now add an event listener to our button, which will wait for an event to happen, a hover in this case*/

button.addEventListener("mouseenter", function (){
    button.style.backgroundColor = "green"
})
button.addEventListener("mouseleave", function () {
    button.style.backgroundColor = "white"
})
/*lets make this button add to the prices list, taking input from a text field*/
let input = document.getElementById("userinput"); /*our input*/
let ul = document.querySelector("ul"); /*our unordered list*/


function createListElement(){ /*this function will create a list element and add it to our list*/
    let li = document.createElement("li") /*create a list entry element*/
    li.textContent += input.value; /*each element in html has a text node, which is empty at first, but we can add text from input to it*/
    ul.appendChild(li); /*append the list entry item in the unordered list*/
    input.value = ""; /*reset the field after user enters something*/
}
button.addEventListener("click", function (){
    if (input.value.length > 0){
        createListElement();
    }else{ /*if the user doesnt enter anything, we let him know by modifying the placeholder of the text field*/
        input.placeholder = "please enter something";
    }
})
input.addEventListener("keydown", function () { /*lets add the same thing but when u press enter in the text fie;d*/
    if (event.key === "Enter"){ /*we listen for a key being pressed, if its enter we add the text to the list*/
        if (input.value.length > 0){
            createListElement()
        }else{
            input.placeholder = "Please enter something";
        }
    }
})
let deletebutton = document.getElementById("delete_button") /*lets add a button that deletes the last entered item*/
deletebutton.addEventListener("mouseenter", function (){
    deletebutton.style.backgroundColor = "red"
})
deletebutton.addEventListener("mouseleave", function () {
    deletebutton.style.backgroundColor = "white"
})
deletebutton.addEventListener("click", function () {
    ul.removeChild(ul.lastChild); /*use removechild function on the last child of the list*/
})
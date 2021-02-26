var css = document.querySelector("h3"); /*the output text*/
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient"); /*the current gradient, body*/

function setGradient() {
	body.style.background = 
	"linear-gradient(to right, " 
	+ color1.value 
	+ ", " 
	+ color2.value 
	+ ")";/*this string will generate the css code required for the background*/
	css.textContent = body.style.background + ";"; /*we change the text content of <h3> with the background of the body*/
}

color1.addEventListener("input", setGradient); /*the event we listen to is called input, which is whenever the input changes of the color*/
/*we run the above function whenever we change the 2 colors, to update the background*/
color2.addEventListener("input", setGradient);
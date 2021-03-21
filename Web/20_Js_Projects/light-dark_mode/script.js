const toggleSwitch = document.querySelector('input[type="checkbox"]'); /*select button*/
const mode = document.getElementById('mode'); /*our text on website */
/*Elements that dont get changed by changing our theme*/
const nav = document.getElementById('nav');
const toggleIcon = document.getElementById('toggle-icon');
const image1 = document.getElementById('image1');
const image2 = document.getElementById('image2');
const image3 = document.getElementById('image3');
const textBox = document.getElementById('text-box');

// Dark or light images
const imageMode = (color) =>{ /*function to change image themes*/
    image1.src = `img/undraw_proud_coder_${color}.svg`
    image2.src = `img/undraw_feeling_proud_${color}.svg`
    image3.src = `img/undraw_conceptual_idea_${color}.svg`
}

// Dark mode styles
const darkMode = () =>{
    nav.style.backgroundColor = 'rgb(0,0,0, 0.5)';
    textBox.style.backgroundColor = 'rgb(255,255,255, 0.5)';
    toggleIcon.children[0].textContent = 'Dark Mode' /*change the text next to toggle switch*/
    toggleIcon.children[1].classList.replace('fa-sun','fa-moon'); /*replace sun with moon*/
    imageMode('dark') /*change images*/
}
// Light mode styles
const lightMode = () =>{
    nav.style.backgroundColor = 'rgb(255,255,255, 0.5)';
    textBox.style.backgroundColor = 'rgb(0,0,0, 0.5)';
    toggleIcon.children[0].textContent = 'Light Mode' /*change the text next to toggle switch*/
    toggleIcon.children[1].classList.replace('fa-moon','fa-sun'); /*replace moon with sun*/
    imageMode('light') /*change images*/
}

//Switch theme dynamically
const switchTheme = (event) => {
    if (event.target.checked){ /*if the button is checked*/
        document.documentElement.setAttribute('data-theme', 'dark'); /*change document to dark theme*/
        mode.textContent = "Dark Mode" /*change text on website*/
        localStorage.setItem('theme', 'dark')
        darkMode()
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        mode.textContent = "Light Mode"
        localStorage.setItem('theme', 'light')
        lightMode()
    }
}
/*Event listener*/
toggleSwitch.addEventListener("change", switchTheme)

// Check local storage, to load the previous selected theme
const currentTheme = localStorage.getItem('theme')
if (currentTheme){
    document.documentElement.setAttribute('data-theme', currentTheme); /*change document to saved theme*/
    if (currentTheme === 'dark'){ /*if saved theme is dark, make it dark*/
        toggleSwitch.checked = true;
        darkMode()
    } else {
        lightMode()
    }
}
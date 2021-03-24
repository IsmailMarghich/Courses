/*Importing all the elements we will change*/
const inputContainer = document.getElementById('input-container');
const countdownForm = document.getElementById('countdownForm');
const dateElement = document.getElementById('date-picker');
const titleElement = document.getElementById('title');

const countdownElement = document.getElementById('countdown');
const countdownElementTitle = document.getElementById('countdown-title');
const resetBtn = document.getElementById('countdown-button');
const timeElements = document.querySelectorAll('span');

const completeElement = document.getElementById('complete');
const completeElementInfo = document.getElementById('complete-info');
const completeBtn = document.getElementById('complete-button');

/*global variables we use and change through our program*/
let countdownTitle = '';
let countdownDate = '';
let countdownValue = Date;
let countdownActive;
let savedCountdown;

/*time constants in ms*/

const second = 1000;
const minute = second * 60;
const hour = minute * 60;
const day = hour * 24;

/* Set the minimum date input with the date of today*/
const today = new Date().toISOString().split('T')[0]; /*grab today's date only, no time*/
dateElement.setAttribute('min', today)

/*This is going to populate the countdown screen*/
const updateDOM = () => {
    countdownActive = setInterval(() =>{ /*this will run this block of code every second to update the count down*/
        const now = new Date().getTime(); /*current time in milliseconds since 1970*/
        const distance = countdownValue - now; /*get the amount of milliseconds in between the target date and now*/

        const days = Math.floor(distance / day) /*get the amount of full days using divide and flooring*/
        const hours = Math.floor((distance % day) / hour) /*get amount of full hours using remainder of days*/
        const minutes = Math.floor((distance % hour) / minute)
        const seconds = Math.floor((distance % minute) / second)

        /*Hide input*/
        inputContainer.hidden = true;

        /*if the countdown has ended, show complete*/
        if (distance < -0){
            countdownElement.hidden = true;
            clearInterval(countdownActive);
            completeElementInfo.textContent = `${countdownTitle} finished on ${countdownDate}`;
            completeElement.hidden = false;
        } else{
            /*else, show the countdown in progress*/
            /*populate countdown*/
            countdownElementTitle.textContent = `${countdownTitle}`; /* add the title that the user entered*/
            timeElements[0].textContent = `${days}`;
            timeElements[1].textContent = `${hours}`;
            timeElements[2].textContent = `${minutes}`;
            timeElements[3].textContent = `${seconds}`;
            completeElement.hidden = true;
            countdownElement.hidden = false;
        }
    }, second)
}
/*Take value from form input*/
const updateCountdown = (e) => {
    e.preventDefault(); /*prevent page from refreshing after sending form*/
    countdownTitle = e.target[0].value;
    countdownDate = e.target[1].value;
    savedCountdown = {
        title: countdownTitle,
        date: countdownDate,
    };
    localStorage.setItem('countdown', JSON.stringify(savedCountdown));
    /* Get number version of current Date, update DOM*/
    /*Check for valid date*/
    if (countdownDate === ''){
        alert('Please select a valid date')
    } else{
        countdownValue = new Date(countdownDate).getTime();
        updateDOM();
    }
}
/*Reset all values*/
const reset = () =>{
    /*hide countdowns, show input*/
    countdownElement.hidden = true;
    completeElement.hidden = true;
    inputContainer.hidden = false;
    /*stop the countdown*/
    clearInterval(countdownActive);
    /*reset values*/
    countdownTitle = '';
    countdownDate = '';
    localStorage.removeItem('countdown');
}

const restorePreviousCountdown = () => { /*if user returns we want to display the previous countdown*/
    /*get countdown from localstorage*/
    if(localStorage.getItem('countdown')){
        inputContainer.hidden;
        savedCountdown = JSON.parse(localStorage.getItem('countdown'));
        countdownTitle = savedCountdown.title;
        countdownDate = savedCountdown.date;
        completeElement.hidden = true;
        countdownValue = new Date(countdownDate).getTime();
        updateDOM();
    }
}

/*Event Listener*/
countdownForm.addEventListener('submit',updateCountdown)
resetBtn.addEventListener('click', reset);
completeBtn.addEventListener('click', reset);

/*on load check local storage for previous sessions*/
restorePreviousCountdown();
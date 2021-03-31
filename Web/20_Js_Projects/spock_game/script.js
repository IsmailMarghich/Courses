const playerScoreElement = document.getElementById('playerScore');
const playerChoiceElement = document.getElementById('playerChoice');
const computerScoreElement = document.getElementById('computerScore');
const computerChoiceElement = document.getElementById('computerChoice');
const resultText = document.getElementById('resultText');
/*player icons*/
const playerRock = document.getElementById('playerRock');
const playerScissors = document.getElementById('playerScissors');
const playerPaper = document.getElementById('playerPaper');
const playerLizard = document.getElementById('playerLizard');
const playerSpock = document.getElementById('playerSpock');
/*computer icons*/
const computerRock = document.getElementById('computerRock');
const computerScissors = document.getElementById('computerScissors');
const computerPaper = document.getElementById('computerPaper');
const computerLizard = document.getElementById('computerLizard');
const computerSpock = document.getElementById('computerSpock');

const allGameIcons = document.querySelectorAll('.far');

const choices = {
    rock: {name: 'Rock', defeats: ['scissors', 'lizard']},
    paper: {name: 'Paper', defeats: ['rock', 'spock']},
    scissors: {name: 'Scissors', defeats: ['paper', 'lizard']},
    lizard: {name: 'Lizard', defeats: ['paper', 'spock']},
    spock: {name: 'Spock', defeats: ['scissors', 'rock']},
};

let playerScoreNumber = 0;
let computerScoreNumber = 0;
let computerChoice = ''

/*Reset all 'selected icons'*/
const resetSelected = () => {
    allGameIcons.forEach((icon) => {
        icon.classList.remove('selected')
    })
}
/*Reset score and player/computer choice*/
const resetAll = () => {
    playerScoreNumber = 0;
    computerScoreNumber = 0;
    playerScoreElement.textContent = playerScoreNumber;
    computerScoreElement.textContent = computerScoreNumber;
    playerChoiceElement.textContent = '';
    computerChoiceElement.textContent = '';
    resultText.textContent = '';
    resetSelected();
}

const computerRandomChoice = () => {
    const computerChoiceNumber = Math.floor(Math.random() * 5); /*get a number between 0 and 4*/
    if (computerChoiceNumber === 0) {
        computerChoice = 'rock';
    } else if (computerChoiceNumber === 1) {
        computerChoice = 'paper';
    } else if (computerChoiceNumber === 2) {
        computerChoice = 'scissors';
    } else if (computerChoiceNumber === 3) {
        computerChoice = 'lizard';
    } else {
        computerChoice = 'spock';
    }
};

/*Add selected styling and computer choice*/
const displayComputerChoice = () => {
    /*Add selected styling and update playerChoice variable*/
    switch (computerChoice) {
        case 'rock':
            computerRock.classList.add('selected');
            computerChoiceElement.textContent = ' --- Rock';
            break;
        case 'paper':
            computerPaper.classList.add('selected');
            computerChoiceElement.textContent = ' --- Paper';
            break;
        case 'scissors':
            computerScissors.classList.add('selected');
            computerChoiceElement.textContent = ' --- Scissors';
            break;
        case 'lizard':
            computerLizard.classList.add('selected');
            computerChoiceElement.textContent = ' --- Lizard';
            break;
        case 'spock':
            computerSpock.classList.add('selected');
            computerChoiceElement.textContent = ' --- Spock';
            break;
        default:
            break;
    }
}

/*check result increase scores, update resultText*/
const updateScore = (playerChoice) => {
    if (playerChoice === computerChoice) { /*tie*/
        resultText.textContent = "It's a tie."
    } else {
        const choice = choices[playerChoice]; /*lookup the player choice in our array and see what that choice beats*/
        /*look up the index of computer choice, if its 1 or zero, it means win, -1 means defeat*/
        if (choice.defeats.indexOf(computerChoice) > -1) { /*win*/
            resultText.textContent = "You won!";
            playerScoreNumber++; /*increase score and display*/
            playerScoreElement.textContent = playerScoreNumber;
        } else { /*loss*/
            resultText.textContent = "You lost!";
            computerScoreNumber++; /*increase score and display*/
            computerScoreElement.textContent = computerScoreNumber;
        }
    }
}
/*Function to process turns*/
const checkResult = (playerChoice) => {
    resetSelected();
    computerRandomChoice();
    displayComputerChoice();
    updateScore(playerChoice)
}
/*Passing player selection value and then style icons*/
const select = (playerChoice) => {
    /*Add selected styling and update playerChoice variable*/
    resetSelected();
    checkResult(playerChoice);
    switch (playerChoice) {
        case 'rock':
            playerRock.classList.add('selected');
            playerChoiceElement.textContent = ' --- Rock';
            break;
        case 'paper':
            playerPaper.classList.add('selected');
            playerChoiceElement.textContent = ' --- Paper';
            break;
        case 'scissors':
            playerScissors.classList.add('selected');
            playerChoiceElement.textContent = ' --- Scissors';
            break;
        case 'lizard':
            playerLizard.classList.add('selected');
            playerChoiceElement.textContent = ' --- Lizard';
            break;
        case 'spock':
            playerSpock.classList.add('selected');
            playerChoiceElement.textContent = ' --- Spock';
            break;
        default:
            break;
    }
}
/*On load*/
resetAll(); /*set initial values*/

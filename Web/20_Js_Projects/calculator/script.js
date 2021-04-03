const calculatorDisplay = document.querySelector('h1');
const inputBtns = document.querySelectorAll('button');
const clearBtn = document.getElementById('clear-btn');

let firstValue = 0;
let operatorValue = '';
let awaitingNextValue = false; /*boolean to check whether were waiting for second number or not*/

const calculate = { /*Calculate the equation depending on operator*/
    '/': (firstNumber, secondNumber) => firstNumber / secondNumber,
    '*': (firstNumber, secondNumber) => firstNumber * secondNumber,
    '+': (firstNumber, secondNumber) => firstNumber + secondNumber,
    '-': (firstNumber, secondNumber) => firstNumber - secondNumber,
    '=': (firstNumber, secondNumber) => secondNumber,
}

const sendNumberValue = (number)=>{
    /*replace current display value if first value is entered*/
    if (awaitingNextValue){
        calculatorDisplay.textContent = number
        awaitingNextValue = false;
    }else {
        /*if current display is 0, replace, otherwise add to textContent*/
        const displayValue = calculatorDisplay.textContent;
        calculatorDisplay.textContent = displayValue === '0' ? number : displayValue + number;
    }
}
const addDecimal = () =>{
    /*if operator pressed, dont add decimal*/
    if (awaitingNextValue) return;
    /*if no decimal, add one*/
    if (!calculatorDisplay.textContent.includes('.')){
        calculatorDisplay.textContent = `${calculatorDisplay.textContent}.`
    }
}

/* operator function*/
const useOperator = (operator) => {

    /*prevent multiple operators*/
    if (operatorValue && awaitingNextValue) { /*if we have our operator value, and first number, dont add more operators*/
        operatorValue = operator; /*make sure we dont '=' as operator*/
        return
    }
    const currentValue = Number(calculatorDisplay.textContent);
    if (!(operator === '=')){ /*we want to visually show which operating we are using, after we grab our number*/
        calculatorDisplay.textContent += operator;
    }
    /*assign first value if it doesnt exist yet*/
    if (!firstValue) {
        firstValue = currentValue;
    }else {
        const calculation = calculate[operatorValue](firstValue, currentValue); /*grab the equation using our calculate object*/
        calculatorDisplay.textContent = calculation; /*change display to result*/
        firstValue = calculation; /*make the result the first value, so user can make second equation*/
    }
    awaitingNextValue = true; /*we are ready for next value*/
    operatorValue = operator;
}

/*Reset all values & display*/
const resetAll =()=> {
    calculatorDisplay.textContent = '0'
    firstValue = 0;
    operatorValue = '';
    awaitingNextValue = false;
}

/*Add event listeners for numbers, operators, decimal buttons*/
inputBtns.forEach((inputBtn)=> {
    if (inputBtn.classList.length === 0){ /*grab the number buttons, those dont have classes*/
        inputBtn.addEventListener('click', ()=> sendNumberValue(inputBtn.value))
    }
    else if (inputBtn.classList.contains('operator')){ /*grab the buttons with operators*/
        inputBtn.addEventListener('click', ()=> useOperator(inputBtn.value))
    }
    else if (inputBtn.classList.contains('decimal')){ /*grab the buttons with operators*/
        inputBtn.addEventListener('click', ()=> addDecimal())
    }
})
/*event listener for our reset button*/
clearBtn.addEventListener('click', resetAll);
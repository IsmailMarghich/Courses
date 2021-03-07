/*there is more ways to do control flow in javascript*/
let bool = true;
/*ternary operator, does first expression if condition is true, second if condition is false*/
bool ? console.log("true") : console.log("false");
/*^condition*/
let color = "red";
/*instead of using long chains of if and else if statements we can use switch statement
* which executes certain code if a case of the condition is met*/
switch (color) {
    case color = "red":
        console.log("Your color is red");
        break;
    case color = "blue":
        console.log("Your color is blue");
        break;
    case color = "green":
        console.log("Your color is green");
        break;
}
name = "bob";
age = 55;
job = "programming"
/*the old way of putting variables in strings is tedious*/
annoyingstring =  "I am" + name + "im" + age + "years old and my job is" + job;
/*we can use template strings instead where we enclose variables with {} and add $ before it*/
modernstring = `I am ${name} im ${age} years old and my job is "${job}"`;/*we can also freely use "" and ''*/
console.log(modernstring);
/*it can be pretty annoying to write tons of small functions, but arrow functions can help us*/
const add = (a,b) => a + b; /*function that takes 2 variables and returns the sum of them*/
console.log(add(5,7));

const subtract = (a) => (b) => a - b; /*currying a function means changing it to take multiple parameters seperately*/
console.log(subtract(6)(3));
const removeFrom5 = subtract(5) /*the benefit of currying is that it allows us to split up a function*/
console.log(removeFrom5(3));

const compose = (f, g) => (a) => f(g(a)); /*a compose function allows us to execute multiple functions in one*/
const sum = (num) => num + 1; /*a function that adds 1 to input*/
compose(sum, sum)(5); /*use 2 sums on 5*/

/*theres more ways of looping in Javascript*/
/*for of loop allows us to loop without making a variable, we are iterating over the array, rather than putting in indexes*/
let basket = ["apples", "bananas", "grapes"];
for (item of basket){
    console.log(item);
}
objectbasket = {
    apples: 5,
    bananas: 15,
    grapes: 1000
}
/*a for in loop makes use of enumeration, because we cannot iterate over an object*/
for (item in objectbasket){
    console.log(item);
}
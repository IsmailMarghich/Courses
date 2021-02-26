/*control flow allows us to change the flow of a javascript program*/
let name = "billy";
let age = 18;
if (name === "billy") { /*an if statement will run a block of code in brackets {} if it meets the condition*/
    console.log("Your name is billy!");
} else{ /*if the statement is not met, the block of code after an else statement is ran instead*/
    console.log("Your name is not billy")
}
if( age > 17){ /*we can add additional if statements */
    console.log("You are an adult!")
}
/*we can combine multiple ifs with logical operators*/
if (name === "billy" && age > 17){ /*&& is an AND operator, it returns true if both statements are true*/
    console.log("billy is an adult")
} /*there is also || which is the OR operator which returns true if either statements are true
and there is ! which is a NOT operator, which returns the opposite of something, true to false, false to true*/

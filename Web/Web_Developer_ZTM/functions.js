/*Functions are blocks of reusable code, they take data in the form of arguments as input and return data
*console.log is also a function, it takes a message as argument and sends it to the console*/
console.log("Im using a function");
/*we can make a function ourselves*/
function greeting(){ /*we start with function keyword, function name, and arguments in ()*/
    console.log("Hello") /*in the brackets is the code is that getting run when function is called*/
}
greeting(); /*we call the function by its name and passing arguments if necessary */

let bye = function (){ /*we can also set the function to a variable, this function is now anonymous
since we cannot access it directly, the function can only be called as a method when accessing this object*/
    console.log("Bye")
}
bye();
function double(number){ /*this function takes a variable as argument*/
    return 2 * number; /*it returns the value of argument multiplied by 2*/
}
double(10); /*this does not output anything, because it is returned, not logged*/
/*to use the returned value we have to use it in another express*/
let number = 10; /*variables and arguments within functions are local, they cannot be accessed from the outside*/
console.log(double(number));
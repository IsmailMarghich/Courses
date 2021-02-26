/*In javascript there is a few different types of data we can store in variables
* we can declare variables with let and const keyword*/
let number1 = 20; /*in javascript there is numbers*/
let number2 = 10;
let string = "Hello, world"; /*strings*/
let plus = true; /*boolean values, which are true or false*/
let nothing = null; /*and null values, meaning nothing*/
let number = 10;
let notype; /*when variables dont have a type, they are undefined*/
/*we can apply operators between these variables
* we can write to the console using console.log*/
console.log(number1 + number2); /*we can do all sorts of mathematical operations on numbers*/
console.log(number1 > number2); /*we can compare with greater or less than, this returns true or false*/
console.log(number1 < number2);
console.log(number1 === number2); /*we can see if variables are equal or not with === and !===, this returns true or false*/
console.log(number1 !== number2);

/*arrays are a series of data which we can access via an index*/
let list = [1,2,3,4,5];
console.log(list);
console.log(list[0]) /*we can access the values of the list via [] and entering the index of a value*/
list[1] = "letter"; /*we can have different data types in the same list but this is bad for performance*/
console.log(list[1]); /*we can change the values of items in a list*/
let twodarray = [list, [6,7,8,9]]; /*arrays can be items in arrays as well*/
console.log(twodarray);

/*we can also apply methods to arrays, which are functions specific for arrays*/
list.pop(); /*pop removes last element*/
console.log(list);
list.push(6); /*push adds a new element at the end*/
console.log(list);
list.shift(); /*shift removes an element from the start*/
console.log(list);
list.sort(); /*sorts the array. when there is strings, they are sorted on alphabet*/
console.log(list);
list = list.concat([7,8,9]) /*we can connect 2 arrays together with concat, but we have to re assign this new list into the original one*/
console.log(list);

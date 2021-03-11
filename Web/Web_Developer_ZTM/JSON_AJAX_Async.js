/*We can use JSON to send data over the internet, JSON has a similar syntax to javascript objects*/
const fetch = require("node-fetch");

let obj = ('{"name":"John", "age":30, "city":"New York"}'); /*json style syntax object*/
console.log(obj);

let parsed = JSON.parse(obj); /*parse converts json object to js object*/
console.log(parsed.name); /*we can print its values just like an object*/
console.log(parsed.age);
console.log(parsed.city);

console.log(JSON.stringify(parsed)); /*stringify turns js object to json*/
/*we can use the handy fetch function to get data from the internet, in this case a json document*/
fetch('https://jsonplaceholder.typicode.com/users')/*go to this website and grab the json file*/
    .then(response =>  response.json()) /*then convert the response to JSON*/
    .then(response => console.log(response)) /*then print the result*/
/*we can remake this function in an easier way, with async functions
* rather than chaining a bunch of .then methods, we can use await to wait for a response from API*/
const fetchUsers = async function () {
    const response = await fetch('https://jsonplaceholder.typicode.com/users') /*wait for API to load and then store result*/
    return await response.json(); /*wait for the response, then return the response converted to json*/
}

fetchUsers().then(r =>{ /*call the function, and then log our result*/
    console.log(r);
});
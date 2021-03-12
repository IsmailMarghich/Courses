const fetch = require("node-fetch");
/*we can request information from API's in a simple way, using json and fetch*/
fetch('https://api.github.com/users/apple')
    .then(response =>  response.json())
    .then(response => console.log(response))
/*returns data from apple's github account*/
    fetch('https://swapi.dev/api/people/1/')
        .then(response =>  response.json())
        .then(response => console.log(response))
/*returns data about luke skywalker from the star wars API*/
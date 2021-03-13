/*lets use express, a nodejs framework to help us build servers faster*/
const express = require('express');
const app = express();
const user = {
    name: 'Reiner',
    hobby: 'Games'
}
app.use(express.urlencoded({extended: false}))

app.use(((req, res, next) => { /*when our app is used*/
    console.log('A user is visiting our website')
    next(); /*after the above code block is gone, move onto next code*/
}))

app.get('/', (req, res) =>{ /*when we receive a get request to / or the homepage*/
    res.send(user) /*express automatically stringifies javascript objects to JSON*/
    /*REST APIs are a set of standards set for APIS, below are some common REST API methods*/
    console.log(req.query); /*prints what the users queries with the ? after the website URL, used in forms a lot*/
    console.log(req.body); /*returns body of request*/
    console.log(req.headers) /*returns headers*/
    console.log(req.params) /*returns parameters of request, which is the text after the /*/
})
/*we can do another get for other pages*/
app.get('/profile', (req, res)=>{
    res.send('<h1>Profile:</h1><br>')
})
app.post('/profile', ((req, res) => { /*if someone tries to post on profile with a POST request*/
    console.log(req.body) /*we log the contents of the request*/
}))

app.listen(3001)

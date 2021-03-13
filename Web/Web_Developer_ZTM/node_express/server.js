const http = require('http');
/*in this file we will create our own server using node and http module*/
const server = http.createServer((request, response) =>{
   response.setHeader('Content-Type', 'application/json'); /*make a header file*/
    const user = {
        name: 'John',
        hobby: 'Soccer'
    }
   response.end(JSON.stringify(user)) /*respond to the request with JSON, this is a very basic API*/
    console.log('request received');
    console.log('headers: ', request.headers); /*display information about the request*/
    console.log('method: ', request.method);
    console.log('url', request.url);
})

server.listen(3001); /*the port we listen to*/
#!/usr/bin/node

// import the 'request' module
const request = require('request');

// perform an HTTP GET request using the 'request' module
// to the URL
request.get(process.argv[2])
    // set up the event listener of the 'response' event
    // emitted by the HTTP request
    .on('response', function (response) {
        // log the HTTP status code of the response to the console
        console.log(`code: ${response.statusCode}`);
    });

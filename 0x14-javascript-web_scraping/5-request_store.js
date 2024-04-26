#!/usr/bin/node
// import the fs module
const fs = require('fs');

// import the request module
const request = require('request');

// use the request module to perform an HTTP GET
// request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));

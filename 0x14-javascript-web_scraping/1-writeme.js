#!/usr/bin/node

// import the builtin Node.js 'fs' module
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
    if (error) {
        console.error(error);
    }
});

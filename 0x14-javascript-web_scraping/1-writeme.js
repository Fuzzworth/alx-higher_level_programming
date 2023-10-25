#!/usr/bin/node
const fileName = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

fs.writeFile(fileName, str, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});

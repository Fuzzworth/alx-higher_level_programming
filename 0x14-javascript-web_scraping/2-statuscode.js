#!/usr/bin/node
const request = require('request');
let url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const resJ = JSON.parse(body);
    console.log(resJ.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});

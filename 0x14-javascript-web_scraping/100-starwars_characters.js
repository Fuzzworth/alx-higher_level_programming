#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  for (const character of JSON.parse(body).characters) {
    request.get(character, (errorInner, responseInner, bodyInner) => {
      if (errorInner) {
        console.log(errorInner);
      }
      console.log(JSON.parse(bodyInner).name);
    });
  }
});

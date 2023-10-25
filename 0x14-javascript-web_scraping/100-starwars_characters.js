#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  for (let i = 0; i < JSON.parse(body).characters.length; i++)  {
    request.get(JSON.parse(body).characters[i], (errorInner, responseInner, bodyInner) => {
      if (errorInner) {
        console.log(errorInner);
      }
      console.log(JSON.parse(bodyInner).name);
    });
  }
});

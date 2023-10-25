#!/usr/bin/node
const request = require('request');
const util = require('util');
const pr = util.promisify(request);
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  getCharacter(JSON.parse(body).characters);
});

async function getCharacter(characters, index) {
    await pr.get(characters[i], (errorInner, responseInner, bodyInner) => {
      if (errorInner) {
        console.log(errorInner);
      }
      console.log(JSON.parse(bodyInner).name);
      if (index + 1 < characters.length) getCharacter(characters, index++);
    });
}



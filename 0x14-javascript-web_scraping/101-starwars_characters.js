#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, { json: true }, (error, response, body) => {
if (!error) {
for (const charUrl of body.characters) {
request(charUrl, { json: true }, (errorInner, responseInner, bodyInner) => {
if (!errorInner) {
  console.log(bodyInner.name);
} else {
  console.log(errorInner);
}
});
}
} else {
console.log(error);
}
});

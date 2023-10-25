#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (error, response, body) => {
if (error) {
console.log(error);
}
for (const character of JSON.parse(body).characters) {
request.get(character, (error_inner, response_inner, body_inner) => {
if (error_inner) {
console.log(error_inner);
}
console.log(JSON.parse(body_inner).name);
});
}
});

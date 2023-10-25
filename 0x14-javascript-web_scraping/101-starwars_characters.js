#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, { json: true },(error, response, body) => {
if (!error) {
for (const char_url of body.characters) {
request(cahr_url, { json: true }, (error, response, body) => {
if (!error) {
console.log(body.name);
}
}
}i
});
});

#!/usr/bin/node
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(body.split('/people/18/').length - 1);
});

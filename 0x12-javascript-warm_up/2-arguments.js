#!/usr/bin/node
const process = require('node:process');
if (process.argv.length == 2) {
  console.log('No argument');
} else {
  console.log('Argument found');
}

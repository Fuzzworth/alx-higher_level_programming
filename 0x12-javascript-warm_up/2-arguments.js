#!/usr/bin/node
const process = require('node:process');
if (process.argv.length <= 1) {
  console.log('No argument');
} else if (process.argv.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

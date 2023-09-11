#!/usr/bin/node
const process = require('node:process');
if (process.argv.length === 1) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}

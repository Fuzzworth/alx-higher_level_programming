#!/home/fuzzworth/.nvm/versions/node/v14.21.3/bin/node
const process = require('node:process');
if (process.argv.length <= 1) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}

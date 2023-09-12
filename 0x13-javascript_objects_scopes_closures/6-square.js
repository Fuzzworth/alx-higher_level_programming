#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    let row = '';
    for (let x = 0; x < this.size; x++) {
      for (let y = 0; y < this.size; y++) {
        row = row + c;
      }
      console.log(row);
      row = '';
    }
  }
};

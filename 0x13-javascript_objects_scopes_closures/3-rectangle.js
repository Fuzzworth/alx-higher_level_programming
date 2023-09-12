#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let row = '';
    for (let x = 0; x < this.height; x++) {
      for (let y = 0; y < this.width; y++) {
        row = row + 'X';
      }
      console.log(row);
      row = '';
    }
  }
};

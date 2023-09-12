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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};

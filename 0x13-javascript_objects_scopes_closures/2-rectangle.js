#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }
};

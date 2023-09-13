#!/usr/bin/node
exports.logMe = function (item) {
  if (this.num === undefined) {
    this.num = 0;
  }
  console.log(`${this.num}: ${item}`);
  this.num++;
};

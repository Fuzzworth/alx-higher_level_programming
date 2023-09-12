#!/usr/bin/node
const Square = require('./5-square.js');
module.exports = class Square extends Square {
	constructor (size) {
		super(size);
	}

	charPrint(c = 'X') {
		let row = '';
		for (let x = 0; x < this.height; x++) {
			for (let y = 0; y < this.width; y++) {
				row = row + c;
			}
			console.log(row);
			row = '';
		}
	}
};

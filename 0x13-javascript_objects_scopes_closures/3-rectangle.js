#!/usr/bin/node

/* A class the defines a rectangle */
class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		const w = this.width * 'X';
		for (let i = 0; i < this.height; i++)
			console.log(w);
}

module.exports = Rectangle;

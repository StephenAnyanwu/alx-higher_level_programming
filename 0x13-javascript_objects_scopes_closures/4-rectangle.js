#!/usr/bin/node

/* A class the defines a rectangle */
class Rectangle {
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		let x = '';
		for (let i = 0; i < this.width; i++) {
			x += 'X';
		}
		for (let j = 0; j < this.height; j++) {
			console.log(x);
		}
	}

	rotate () {
		let tmp = this.width;

		this.width = this.height;
		this.height = tmp;
	}

	double () {
		this.width *= this.width;
		this.height *= this height;
	}
}

module.exports = Rectangle;

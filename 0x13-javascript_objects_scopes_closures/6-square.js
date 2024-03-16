#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x += c;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(x);
    }
  }
}

#!/usr/bin/node
const Squarei = require('./5-square');
class Square extends Squarei {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s = s + c;
      }
      console.log(s);
    }
  }
}
module.exports = Square;

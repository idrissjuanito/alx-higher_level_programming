#!/usr/bin/node
const Square = require('./5-square');

module.exports = class Square extends Square {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let k = 0; k < this.width; k++) {
        line += c;
      }
      console.log(line);
    }
  }
};

#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  printChar (c) {
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

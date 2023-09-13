#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
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

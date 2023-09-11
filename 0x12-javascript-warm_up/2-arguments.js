#!/usr/bin/node
const { argv } = require('node:process');
let output = 'No argument';
if (argv.length === 3) {
  output = 'Argument found';
}
if (argv.length > 3) {
  output = 'Arguments found';
}
console.log(output);

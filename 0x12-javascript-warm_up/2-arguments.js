#!/usr/bin/node

let output = 'No argument';
if (process.argv.length === 3) {
  output = 'Argument found';
}
if (process.argv.length > 3) {
  output = 'Arguments found';
}
console.log(output);

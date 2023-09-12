#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) return 'NaN';
  return parseInt(a) + parseInt(b);
}
const { argv } = process;
console.log(add(argv[2], argv[3]));

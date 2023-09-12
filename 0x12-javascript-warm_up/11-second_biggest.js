#!/usr/bin/node
const topTwo = [];
const { argv } = process;
if (argv.length < 3) console.log(0);
else {
  for (let i = 2; i < argv.length; i++) {
    const arg = parseInt(argv[i]);
    if (topTwo.length === 0) {
      topTwo.push(arg);
      continue;
    }
    if (topTwo.length === 1) {
      if (topTwo[0] > arg) topTwo.unshift(arg);
      else topTwo.push(arg);
      continue;
    }
    if (arg > topTwo[1]) {
      topTwo.shift();
      topTwo.push(arg);
      continue;
    }
    if (arg > topTwo[0]) {
      topTwo.shift();
      topTwo.unshift(arg);
    }
  }
}
console.log(topTwo[0]);

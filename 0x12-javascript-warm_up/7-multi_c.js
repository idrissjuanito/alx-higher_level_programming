#!/usr/bin/node
const occurs = parseInt(process.argv[2]);
if (isNaN(occurs)) console.log('Missing number of occurrences');
else {
  for (let i = 0; i < occurs; i++) {
    console.log('C is fun');
  }
}

#!/usr/bin/node
const occurs = parseInt(process.argv[2]);
if (isNaN(occurs)) console.log('Missing size');
else {
  for (let i = 0; i < occurs; i++) {
    let X = '';
    for (let j = 0; j < occurs; j++) {
      X += 'X';
    }
    console.log(X);
  }
}

#!/usr/bin/node
const { argv } = require('node:process');
let output = 'No argument';
if (argv.length === 3) output = 'Argument found';
if (argv.length > 3) output = 'Arrguments found';
console.log(output);

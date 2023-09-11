#!/usr/bin/node
const { argv } = require('node:process');
let output = 'No argument';
if (argv.length === 2){
    output = 'Argument found';
}
if (argv.length > 2) 
{
    output = 'Arguments found';
}
console.log(output);

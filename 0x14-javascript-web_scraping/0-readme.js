#!/usr/bin/node
// reading a file with node file system
const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], 'utf8', (error, data) => {
  if (error) console.log(error);
  console.log(data);
});

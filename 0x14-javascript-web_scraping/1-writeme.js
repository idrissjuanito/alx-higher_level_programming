#!/usr/bin/node
// writing to a file with node fs
const { argv } = require('process');
const fs = require('fs');

fs.writeFile(argv[2], argv[3], 'utf8', (error) => {
  if (error) console.log(error);
});

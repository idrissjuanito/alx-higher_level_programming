#!/usr/bin/node
const fs = require('fs');

const { argv } = process;
fs.readFile(argv[2], (data) => {
  fs.writeFile(argv[4], data, () => {
    fs.readFile(argv[3], (data2) => {
      fs.appendFile(argv[4], data2);
    });
  });
});

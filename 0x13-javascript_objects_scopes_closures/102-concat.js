#!/usr/bin/node
const fs = require('fs');

const { argv } = process;
fs.readFile(argv[2], (err, data) => {
  if (err) throw err;
  fs.writeFile(argv[4], data, () => {
    fs.readFile(argv[3], (err, data2) => {
      if (err) throw err;
      fs.appendFile(argv[4], data2, () => {});
    });
  });
});

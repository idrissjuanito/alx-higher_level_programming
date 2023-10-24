#!/usr/bin/node
// Lorem ipsum api request and file write
const { argv } = require('process');
const fs = require('fs');
const request = require('request');

request(argv[2], (error, res, body) => {
  if (error) console.log(error);
  fs.writeFile(argv[3], body, 'utf8', (err) => {
    err && console.log(err);
  });
});

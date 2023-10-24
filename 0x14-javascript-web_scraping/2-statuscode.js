#!/usr/bin/node
// http request with the request library
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, res, body) => {
  if (error) console.log(error);
  console.log('code:', res.statusCode);
});

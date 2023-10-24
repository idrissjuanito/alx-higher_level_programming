#!/usr/bin/node
// Api query with request library
const request = require('request');
const { argv } = require('process');
const requestUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(requestUrl + argv[2], (error, res, body) => {
  if (error) console.log(error);
  body = JSON.parse(body);
  console.log(body.title);
});

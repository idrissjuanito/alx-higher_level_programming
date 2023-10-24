#!/usr/bin/node
// Api query with request library
const request = require('request');
const { argv } = require('process');

request(argv[2], (error, res, body) => {
  if (error) console.log(error);
  body = JSON.parse(body);
  const films = body.results;
  const num = films.reduce((prev, next) => {
    const characters = next.characters;
    for (let i = 0; i < characters.length; i++) {
      if (characters[i].slice(-3, -1) === '13') prev++;
    }
    return prev;
  }, 0);
  console.log(num);
});

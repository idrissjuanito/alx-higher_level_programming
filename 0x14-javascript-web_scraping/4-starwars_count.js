#!/usr/bin/node
// Api query with request library
const request = require('request');
const { argv } = require('process');
const characterLink = 'https://swapi-api.alx-tools.com/api/people/18/';

request(argv[2], (error, res, body) => {
  if (error) console.log(error);
  body = JSON.parse(body);
  let films = body.results;
  films = films.filter(film => film.characters.includes(characterLink));
  console.log(films.length);
});

#!/usr/bin/node
// Starwars api filter data
const request = require('request');
const { argv } = require('process');
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(reqUrl + argv[2], (error, res, body) => {
  if (error) console.log(error);
  const films = JSON.parse(body);
  films.characters.forEach(character => {
    request(character, (error, res, body) => {
      if (error) console.log(error);
      const ch = JSON.parse(body);
      console.log(ch.name);
    });
  });
});

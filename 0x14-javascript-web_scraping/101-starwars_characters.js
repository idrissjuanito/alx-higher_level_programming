#!/usr/bin/node
// Starwars api filter data
const request = require('request');
const { argv } = require('process');
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(reqUrl + argv[2], async (error, res, body) => {
  if (error) console.log(error);
  const films = JSON.parse(body);

  const arr = films.characters.map(async (ch, index) => {
    const name = await new Promise((resolve, reject) => {
      request(ch, (error, res, body) => {
        if (error) return reject(error);
        return resolve(JSON.parse(body).name);
      });
    });
    return name;
  });
  const values = await Promise.all(arr);
  values.forEach(name => console.log(name));
});

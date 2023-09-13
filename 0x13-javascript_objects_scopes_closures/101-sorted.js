#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = Object.values(dict).reduce((prev, current) => {
  prev[current] = [];
  return prev;
}, {});
Object.keys(dict).forEach((key) => newDict[dict[key]].push(key));
console.log(newDict);

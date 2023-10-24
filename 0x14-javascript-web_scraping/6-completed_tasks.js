#!/usr/bin/node
// Lorem ipsum api request and file write
const { argv } = require('process');
const request = require('request');

request(argv[2], (error, res, body) => {
  if (error) console.log(error);
  const obj = {};
  const todos = JSON.parse(body);
  todos.forEach(todo => {
    if (todo.completed) {
      if (Object.hasOwn(obj, todo.userId)) obj[todo.userId]++;
      else obj[todo.userId] = 1;
    }
  });
  console.log(obj);
});

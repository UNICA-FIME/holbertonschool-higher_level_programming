#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 18;
let count = 0;
let dicFilms = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  dicFilms = JSON.parse(body);
  for (let i = 0; i < dicFilms.results.length; i++) {
    for (let j = 0; j < dicFilms.results[i].characters.length; j++) {
      if (dicFilms.results[i].characters[j].includes(id)) {
        count++;
      }
    }
  }
  console.log(count);
});

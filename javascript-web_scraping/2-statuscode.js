#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request((url), function (response) {
  console.log('code: ', response && response.statusCode);
});

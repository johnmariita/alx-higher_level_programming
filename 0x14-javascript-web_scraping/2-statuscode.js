#!/usr/bin/node

const request = require('request');
const { argv } = require('node:process');

request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code:', response.statusCode);
});

#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

request(argv[2], function (err, response, body) {
  if (err) console.log(err);
  else {
    console.log('Code:', response.statusCode);
  }
});

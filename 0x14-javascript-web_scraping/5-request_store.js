#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');
const request = require('request');

request(argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    fs.writeFile(argv[3], body, function (error) {
      if (error) console.log(error);
    });
  }
});

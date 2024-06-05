#!/usr/bin/node

const fs = require('fs');
const { argv } = require('node:process');

fs.writeFile(argv[2], argv[3], 'utf8', function (err) {
  if (err) {
    console.error(err);
  }
});

#!/usr/bin/node

const { argv } = require('node:process');

const MyNum = parseInt(argv[2]);
if (!isNaN(MyNum)) {
  console.log('My number: ' + argv[2]);
} else {
  console.log('Not a number');
}

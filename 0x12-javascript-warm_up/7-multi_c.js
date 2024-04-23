#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length !== 3) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(argv[2]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

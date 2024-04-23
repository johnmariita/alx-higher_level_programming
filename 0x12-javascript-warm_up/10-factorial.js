#!/usr/bin/node

const { argv } = require('node:process');

function factorial (n) {
  if (isNaN(n)) { return 1; }
  return (n * (n < 2 ? 1 : factorial(n - 1)));
}
console.log(factorial(parseInt(argv[2])));

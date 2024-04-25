#!/usr/bin/node
const dict = require('./101-data.js').dict;

const sorted = {};

Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (sorted[dict[occurences]] === undefined) {
    sorted[dict[occurences]] = [occurences];
  } else {
    sorted[dict[occurences]].push(occurences);
  }
});
console.log(sorted);

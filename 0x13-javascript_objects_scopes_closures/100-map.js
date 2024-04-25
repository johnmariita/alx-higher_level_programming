#!/usr/bin/node

const { list } = require('./100-data');

console.log(list);
const newList = list.map((a, b) => a * b);
console.log(newList);

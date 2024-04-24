#!/usr/bin/node

const { list } = require('./100-data');

console.log(list);
const newList = list.map(a => a * list.indexOf(a));
console.log(newList);

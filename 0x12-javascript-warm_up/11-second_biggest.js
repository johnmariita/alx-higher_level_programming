#!/usr/bin/node

const { argv } = require('node:process');

const MyArr = [];
if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    MyArr.push(parseInt(argv[i]));
  }
  MyArr.sort();
  MyArr.reverse();
  console.log(MyArr[1]);
}

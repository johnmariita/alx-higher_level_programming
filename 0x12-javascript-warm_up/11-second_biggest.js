#!/usr/bin/node

const { argv } = require('node:process');

const MyArr = [];
if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    MyArr.push(Number(argv[i]));
  }
  MyArr.sort((a, b) => a - b);
  MyArr.reverse();
  console.log(MyArr[1]);
}

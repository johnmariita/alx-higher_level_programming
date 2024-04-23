#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length !== 3) {
  console.log('Missing Size');
} else {
  const size = parseInt(argv[2]);
  if (isNaN(size)) {
    console.log('Missing size');
  } else {
    for (let height = 0; height < size; height++) {
      for (let width = 0; width < size; width++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}

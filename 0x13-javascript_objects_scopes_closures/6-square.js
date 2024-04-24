#!/usr/bin/node

const Square = require('./5-square');
class Square2 extends Square {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      super.print();
    } else {
      for (let hc = 0; hc < this.size; hc++) {
        for (let wc = 0; wc < this.size; wc++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
}
module.exports = Square2;

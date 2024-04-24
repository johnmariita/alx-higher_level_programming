#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
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
module.exports = Square;

#!/usr/bin/node
const file = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

if (
  file.existsSync(fileA) &&
file.statSync(fileA).isFile &&
file.existsSync(fileB) &&
file.statSync(fileB).isFile &&
fileC !== undefined
) {
  const fileAContent = file.readFileSync(fileA);
  const fileBContent = file.readFileSync(fileB);
  const stream = file.createWriteStream(fileC);

  stream.write(fileAContent);
  stream.write(fileBContent);
  stream.end();
}

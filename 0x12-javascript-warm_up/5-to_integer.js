#!/usr/bin/node
const res = Math.floor(Number(process.argv[2]));
if (isNaN(res)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${res}`);
}

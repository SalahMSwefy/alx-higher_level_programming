#!/usr/bin/node
const times = Number(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing size');
}

for (let i = 0; i < times; i++) {
  let x = '';
  for (let j = 0; j < times; j++) {
    x += 'X';
  }
  console.log(x);
}

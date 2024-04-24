#!/usr/bin/node
const path = process.argv[2];
const fs = require('fs');

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(data);
});

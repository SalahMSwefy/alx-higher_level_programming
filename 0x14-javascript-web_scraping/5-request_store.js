#!/usr/bin/node
const url = process.argv[2];
const path = process.argv[3];
const request = require('request');
const fs = require('fs');

request({ url, method: 'GET' }, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    fs.writeFile(path, body, 'utf8', err => {
      if (err) {
        console.error(err);
        process.exit(1);
      }
    });
  }
});

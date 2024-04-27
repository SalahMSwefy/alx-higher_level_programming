#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const count = {};

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.lenght; i++) {
      if (tasks[i].completed === true) {
        if (count[tasks[i].userId] === undefined) {
          count[tasks[i].userId] = 1;
        } else {
          count[tasks[i].userId] += 1;
        }
      }
    }
  }
  console.log(count);
});

#!/usr/bin/node
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request({ url, method: 'GET' }, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request({ url: character, method: 'GET' }, (err, response, body) => {
        if (err) {
          console.error(err);
          process.exit(1);
        } else { console.log(JSON.parse(body).name); }
      });
    });
  }
});

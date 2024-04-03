#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const res = JSON.parse(body);
  const cast = res.characters;
  for (let i = 0; i < cast.length; i++) {
    request.get(cast[i], (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const res = JSON.parse(body);
      console.log(res.name);
    });
  }
});

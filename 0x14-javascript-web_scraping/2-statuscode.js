#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
// function handling response output
function handleResponse (response) {
  console.log(`code: ${response.statusCode}`);
}
request.get(url).on('response', handleResponse);

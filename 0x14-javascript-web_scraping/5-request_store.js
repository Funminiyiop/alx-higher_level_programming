#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[3];
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(filePath));

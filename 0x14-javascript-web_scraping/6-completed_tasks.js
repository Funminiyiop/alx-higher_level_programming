#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const completedTasks = {};
request(url, (error, response, body) => {
  if (!error) {
    const res = JSON.parse(body);
    for (let i = 0; i < res.length; i++) {
      if (res[i].completed === true) {
        if (completedTasks[res[i].userId] === undefined) {
          completedTasks[res[i].userId] = 1;
        } else {
          completedTasks[res[i].userId]++;
        }
      }
    }
    console.log(completedTasks);
  } else {
    console.log(error);
  }
});

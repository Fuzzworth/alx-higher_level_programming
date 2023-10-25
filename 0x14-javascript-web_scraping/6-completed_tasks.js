#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    }
    console.log(completed);
  }
});

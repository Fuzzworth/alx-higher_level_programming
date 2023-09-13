#!/usr/bin/node
const list = require('./100-data.js').list;
const index = (value, idx) => value * idx;
const NuList = list.map(index);
console.log(list);
console.log(NuList);

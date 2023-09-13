#!/usr/bin/node
exports.esrever = function (list) {
  const nl = [];
  for (let x = list.length - 1; x >= 0; x--) {
    nl.push(list[x]);
  }
  return nl;
};

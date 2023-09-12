#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const reducer = function (count, value) {
    if (value === searchElement) {
      count = count + 1;
    }
    return count;
  };
  return list.reduce(reducer, 0);
};

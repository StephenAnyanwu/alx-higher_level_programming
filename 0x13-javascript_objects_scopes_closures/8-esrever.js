#!/usr/bin/node

/* A function that returns the reversed version of a list */
exports.esrever = function (list) {
  let lastIdx = list.length - 1;
  let currIdx = lastIdx;
  for (let i = 0; i <= Math.floor(lastIdx / 2); i++) {
    const tmp = list[currIdx];
    list[currIdx] = list[i];
    list[i] = tmp;
    currIdx--;
  }
  return list;
};

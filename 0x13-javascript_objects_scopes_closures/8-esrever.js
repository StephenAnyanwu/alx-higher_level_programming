#!/usr/bin/node

/* A function that returns the reversed version of a list */
exports.esrever = function (list) {
  let lastIdx = list.length - 1;
  for (let i = 0; i <= floor(lastIdx / 2); i++) {
    const tmp = list[lastIdx];  
    list[lastIdx] = list[i];
    list[i] = tmp;
    lastIdx--;
  }
};

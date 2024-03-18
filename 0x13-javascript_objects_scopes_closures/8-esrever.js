#!/usr/bin/node

/* A function that returns the reversed version of a list */
exports.esrever = function (list) {
  let lastIdx = list.length - 1;
  const midIdx = floor(lastIdx / 2);
  for (let i = 0; i <= midIdx; i++) {
    const tmp = list[lastIdx];  
    list[lastIdx] = list[i];
    list[i] = tmp;
    lastIdx--;
  }
};

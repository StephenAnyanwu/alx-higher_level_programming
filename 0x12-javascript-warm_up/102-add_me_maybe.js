#!/usr/bin/node
/* A function that increments and calls a function. */
/* The function is visible from outside */
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};

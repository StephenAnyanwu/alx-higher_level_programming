#!/usr/bin/node

const list = require('./100-data.js').list;
console.log(list);
/* A new list is created with each value equal to the value */
/* of the initial list, multipled by the index in the list */
console.log(list.map((item, idx) => item * idx));

#!/usr/bin/node

const dict = require('./101-data').dict;
// List of keys and values
const totaList = Object.entries(dict);
// List of values in dict
const vals = Object.values(dict);
// List of unique values in vals
const uniqVals = [...new Set(vals)];
const newDict = {};
for (const i in uniqVals) {
  const list = [];
  for (const j in totaList) {
    if (totaList[j][1] === uniqVals[j]) {
      list.unshift(totaList[j][0]);
    }
  }
  newDict[uniqVals[i]] = list;
}
console.log(newDict);

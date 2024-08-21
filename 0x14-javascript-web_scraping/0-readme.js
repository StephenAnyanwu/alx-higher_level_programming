#!/usr/bin/node
// A script that reads and prints the content of a file.

const fileSys = require('fs');
fileSys.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });

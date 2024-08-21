#!/usr/bin/node
// A script that reads and prints the content of a file.

const file_sys = require('fs');
file_sys.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });

#!/usr/bin/node

/* A script that prints "My number: <arg1>" if the first argument */
/* can be converted to an integer print "Not a number" */
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}

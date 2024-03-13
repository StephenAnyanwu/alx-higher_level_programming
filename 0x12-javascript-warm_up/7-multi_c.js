#!/usr/bin/node

/* A script that prints x times “C is fun” x is the first argument of the script */
/* If the first argument can’t be converted to an integer, print “Missing number of occurrences” */
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}

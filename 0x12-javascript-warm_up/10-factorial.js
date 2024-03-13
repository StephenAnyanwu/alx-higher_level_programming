#!/usr/bin/node

/* A script that recursively computes and prints a factorial of a  number. */
/* Where the number is the first argument typecasted to integer */
function factorial (n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));

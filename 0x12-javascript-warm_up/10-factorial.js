#!/usr/bin/node
function factorial (n) {
  const m = parseInt(n);
  if (isNaN(m) || m === 1) return 1;
  return m * factorial(m - 1);
}
console.log(factorial(process.argv[2]));

#!/usr/bin/node
function logger () {
  let count = 0;
  return (str) => {
    console.log(count + ':', str);
    count++;
  };
}
exports.logMe = logger();

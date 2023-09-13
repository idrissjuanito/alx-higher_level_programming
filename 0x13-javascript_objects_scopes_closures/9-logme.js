#!/usr/bin/node
function logger () {
  let count = 0;
  return (str) => {
    count++;
    console.log(count + ':', str);
  };
}
exports.logMe = logger();

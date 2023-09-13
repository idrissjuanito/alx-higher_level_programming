#!/usr/bin/node
exports.converter = function (base) {
  return (base10) => {
    return base10.toString(base);
  };
};

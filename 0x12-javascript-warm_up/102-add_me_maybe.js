#!/usr/bin/node
exports.addMeMaybe = function (nb, callback) {
  nb++;
  callback(nb);
};

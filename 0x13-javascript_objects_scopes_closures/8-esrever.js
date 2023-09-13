#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  const ln = list.length;
  if (ln < 2) return list;
  for (let i = 0; i < ln; i++) {
    reverseList.push(list.pop());
  }
  return reverseList;
};

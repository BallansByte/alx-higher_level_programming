#!/usr/bin/node
/**
 * Executes a given function a specified number of times.
 * @param {number} x The number of times to execute the function.
 * @param {Function} theFunction The function to execute.
 */
const callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};

module.exports.callMeMoby = callMeMoby;

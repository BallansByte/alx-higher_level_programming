#!/usr/bin/node

/**
 * Increments a number and calls a callback function with the incremented value.
 * @param {number} number The number to increment.
 * @param {Function} theFunction The callback function to call with the incremented number.
 */
const addMeMaybe = (number, theFunction) => {
  theFunction(number + 1);
};

module.exports.addMeMaybe = addMeMaybe;

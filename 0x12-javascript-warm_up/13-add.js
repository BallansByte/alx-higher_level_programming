#!/usr/bin/node

/**
 * This function adds two integers.
 * @param {number} a The first integer.
 * @param {number} b The second integer.
 * @returns {number} The sum of the two integers.
 */
const add = (a, b) => {
    if (Number.isInteger(a) && Number.isInteger(b)) {
        return a + b;
    } else {
        throw new Error('Both arguments must be integers');
    }
};

module.exports = add;

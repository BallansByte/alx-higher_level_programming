#!/usr/bin/node

const { dict } = require('./101-data');

function transformDict (originalDict) {
  const newDict = {};
  for (const [key, value] of Object.entries(originalDict)) {
    if (!newDict[value]) {
      newDict[value] = [];
    }
    newDict[value].push(parseInt(key));
  }
  return newDict;
}

const transformedDict = transformDict(dict);

console.log(transformedDict);

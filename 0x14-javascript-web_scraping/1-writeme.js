#!/usr/bin/node

const fs = require('fs');
const [,, filePath, content] = process.argv;

/*This module checks if the file path is there or the content to be copied is available. 
If its not it brings ans error*/
if (!filePath || !content) {
  console.error('Usage: ./writeToFile.js <file path> <string to write>');
  process.exit(1);
}
/*Code to write ther file and return any error if any */
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log('File has been written');
});

#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Error: File path or content not provided.');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});

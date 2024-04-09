#!/usr/bin/node
const fs = require('fs');

const readFile = (filePath) => fs.readFileSync(filePath, 'utf8');
const writeFile = (filePath, data) => fs.writeFileSync(filePath, data);

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const content1 = readFile(sourceFilePath1);
const content2 = readFile(sourceFilePath2);

writeFile(destinationFilePath, content1 + content2);

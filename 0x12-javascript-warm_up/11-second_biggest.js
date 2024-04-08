#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const numberArgs = process.argv.slice(2).map(Number).sort((x, y) => x - y);
  console.log(numberArgs[numberArgs.length - 2]);
}

#!/usr/bin/node
const args = process.argv[2];
const toPrint = 'C is fun';

if (args !== undefined) {
  const argValue = parseInt(args, 10);
  if (!isNaN(argValue)) {
    for (let i = 0; i < argValue; i++) {
      console.log(toPrint);
    }
  }
} else {
  console.log('Missing number of occurrences');
}

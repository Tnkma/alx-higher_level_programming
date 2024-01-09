#!/usr/bin/node
const args = process.argv[2];

if (args !== undefined) {
  const argsValue = parseInt(args, 10);
  if (!isNaN(argsValue)) {
    console.log('My number: ' + argsValue);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}

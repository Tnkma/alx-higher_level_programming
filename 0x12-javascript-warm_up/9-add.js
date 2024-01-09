#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length !== 2) {
  console.log('NaN');
}

const firstArg = parseInt(args[0], 10);
const secArg = parseInt(args[1], 10);

if (isNaN(firstArg) || isNaN(secArg)) {
  console.log('NaN');
} else {
  const result = firstArg + secArg;
  console.log(result);
}

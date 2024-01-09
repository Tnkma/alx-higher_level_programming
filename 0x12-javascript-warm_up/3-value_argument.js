#!/usr/bin/node
const args = process.argv.slice(2);
const cmdargs = args[0];
if (args < 2) {
  console.log('No argument');
} else {
  console.log(cmdargs);
}

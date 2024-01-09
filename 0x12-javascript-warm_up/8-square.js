#!/usr/bin/node

const args = process.argv[2];
if (args !== undefined) {
  const argValue = parseInt(args, 10);
  if (!isNaN(argValue)) {
    for (let i = 0; i < argValue; i++) {
      let row = '';
      for (let j = 0; j < argValue; j++) {
        row += 'X';
      }
      console.log(row);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}

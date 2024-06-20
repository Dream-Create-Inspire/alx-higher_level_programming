#!/usr/bin/node
const args = process.argv.slice(2);

// Get the first argument and convert it to an integer
const x = Number.parseInt(args[0], 10);

// Check if the conversion is successful
if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

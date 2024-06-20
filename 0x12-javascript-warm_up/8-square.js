#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Get the first argument and convert it to an integer
const size = Number.parseInt(args[0], 10);

// Check if the conversion is successful
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  // Print the square
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}

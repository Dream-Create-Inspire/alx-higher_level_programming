#!/usr/bin/node
// Get the arguments passed to the script
const args = process.argv.slice(2);

// Get the first argument
const firstArg = args[0];

// Convert the first argument to an integer
const number = Number.parseInt(firstArg, 10);

// Check if the conversion is successful
const output = !Number.isNaN(number) ? `My number: ${number}` : 'Not a number';

// Print the output
console.log(output);

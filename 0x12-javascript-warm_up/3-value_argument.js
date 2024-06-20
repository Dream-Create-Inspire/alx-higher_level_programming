#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Check if there are any arguments
const firstArg = args[0];

// Print the first argument or "No argument" if none are passed
const output = firstArg !== undefined ? firstArg : 'No argument';
console.log(output);

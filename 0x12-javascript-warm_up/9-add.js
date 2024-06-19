#!/usr/bin/node
const args = process.argv.slice(2);

// Get the first and second arguments and convert them to integers
const a = Number(args[0]);
const b = Number(args[1]);

// Function to add two numbers
const add = (a, b) => a + b;

// Print the result of the addition, which will be NaN if either argument is not a number
console.log(add(a, b));

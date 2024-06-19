#!/usr/bin/node
// Get the arguments passed to the script
const args = process.argv.slice(2);

// Get the first and second arguments
const firstArg = args[0] ? args[0] : "undefined";
const secondArg = args[1] ? args[1] : "undefined";

// Print the output in the format " is "
console.log(`${firstArg} is ${secondArg}`);

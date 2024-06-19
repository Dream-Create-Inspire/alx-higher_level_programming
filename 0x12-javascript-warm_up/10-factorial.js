#!/usr/bin/node
// Get the arguments passed to the script
const args = process.argv.slice(2);

// Get the first argument and convert it to an integer
const num = Number.parseInt(args[0], 10);

// Function to compute the factorial recursively
const factorial = n => {
    if (isNaN(n) || n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
};

// Compute the factorial and print the result
console.log(factorial(num));

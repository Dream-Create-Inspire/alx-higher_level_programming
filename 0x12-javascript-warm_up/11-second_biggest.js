#!/usr/bin/node

// Get the arguments passed to the script
const args = process.argv.slice(2);

// Convert arguments to integers and sort them in descending order
const numbers = args.map(Number).sort((a, b) => b - a);

// Determine the second biggest integer
let secondBiggest = Number.MIN_SAFE_INTEGER;
if (numbers.length > 1) {
    for (let i = 1; i < numbers.length; i++) {
        if (numbers[i] < numbers[i - 1]) {
            secondBiggest = numbers[i];
            break;
        }
    }
}

// Print the second biggest integer
console.log(secondBiggest);

#!/usr/bin/node

const factorial = (num) => {
  // Base case: Factorial of 0 and NaN is 1
  if (isNaN(num) || num === 0) {
    return 1;
  }

  // Recursive case: num * factorial(num - 1)
  return num * factorial(num - 1);
};

// Get the first argument (cast to a number)
const number = Number(process.argv[2]);

// Calculate the factorial
const result = factorial(number);

// Print the factorial result, handling Infinity if the result is too large
console.log(Number.isFinite(result) ? result : "Infinity");

 #!/usr/bin/python3
def uppercase(s):
    lines = s.split('\n')  # Split the input into lines
    for line in lines:
        words = line.split(' ')  # Split each line into words
        for i, word in enumerate(words):
            for char in word:
                ascii_value = ord(char)
                if 97 <= ascii_value <= 122:  # Check if lowercase
                    ascii_value -= 32  # Convert to uppercase ASCII value
                print(chr(ascii_value), end='')
            if i < len(words) - 1:  # Check if it's not the last word
                print(' ', end='')  # Print space between words
        print()  # Print newline between lines

# Test cases
test_cases = [
    "holberton",
    "Holberton School",
    "Holberton School, 98 battery street",
    "",
    "98",
    "z"
]

# Run the test cases
for case in test_cases:
    uppercase(case)

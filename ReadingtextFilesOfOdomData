import re
import time

# Open the text file for reading
file_path = 'path/to/text/file.txt'
file = open(file_path, 'r')

# Define the letter and associated number pattern to extract from the text
letter_pattern = """)
pose: 
  position: 
    x: (r'[-+]?(\d*\.\d+|d+(\.d*)?)([eE][-+]d+)?')
    y: (r'[-+]?(\d*\.\d+|d+(\.d*)?)([eE][-+]d+)?')
    z: (r'[-+]?(\d*\.\d+|d+(\.d*)?)([eE][-+]d+)?')

"""

# Create a dictionary to store the current value of each letter
letter_values = {}

# Monitor the file for changes and update the letter values
while True:
    # Read the new content of the file
    new_content = file.read()

    # Find all matches of the letter pattern in the new content
    matches = re.findall(letter_pattern, new_content)

    # Extract the letter and associated number from each match
    for letter, number in matches:
        # Convert the number to an integer
        number = int(number)

        # Update the value of the letter in the dictionary
        if letter in letter_values:
            letter_values[letter] += number
        else:
            letter_values[letter] = number

    # Print the current letter values
    print(letter_values)

    # Wait for a short period of time before checking for changes again
    time.sleep(0.001)




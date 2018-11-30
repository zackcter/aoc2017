# Take input in the form of a sequence of digits

# Return the sum of each consecutive digit: 1111 -> 4, 1122 -> 3.
# The list is circular, so the last digit is compared to the first.

import argparse

# Check if the next entry equals the current one. Add to summation if so.
def parse_list(sequence_list):
    summation = 0

    for idx, entry in enumerate(sequence_list):
        if idx < len(sequence_list) - 1:
            if entry == sequence_list[idx+1]:
                summation += entry
        
        # Wrap around if at the end.
        elif (entry == sequence_list[0]):
            summation += entry
    
    return summation

# Initialize Arguments    
parser = argparse.ArgumentParser("day1")
parser.add_argument("sequence", help="A sequence of digits that will be parsed. The sum of all consecutive numbers will be returned.")
args = parser.parse_args()
sequence = str(args.sequence) # Not going to get overly defensive. Assume integer input. 
digit_list = []

# Convert integer to list of ints
for digit in sequence:
    digit_list.append(int(digit))

# Call func, return output
print(parse_list(digit_list))
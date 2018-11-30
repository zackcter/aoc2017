# Take input in the form of a sequence of digits

# Return the sum of each digit that matches the digit len()/2 spots ahead.
# 1212 -> 6
# The list is circular.

import argparse

# Check if the next entry len/2 ahead is equal to the current one. Add to summation if so.
def parse_list(sequence_list):
    summation = 0
    check_interval = int(len(sequence_list)/2)

    for idx, entry in enumerate(sequence_list):
        if idx < len(sequence_list)/2 - 1:
            if entry == sequence_list[idx+check_interval]:
                summation += entry
        
        # Wrap around if at the end.
        elif (entry == sequence_list[idx-check_interval]):
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
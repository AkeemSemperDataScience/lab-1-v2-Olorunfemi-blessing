def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = None
    # Do the work here
    # The solution to this goes here (and in all of them below...)
    # Set the variable num_bytes to the answer and return it
    num_bytes = input_gb * 1024* 1024* 1024
    return num_bytes

def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    if not isinstance(name, str):
        return None
    length = len(name)
    if length % 2 == 0:
        is_odd = False
    else:
        is_odd = True
    
    return is_odd

def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.

    
    character_at =-1
    
    if 0 <= input_number < len(input_string):
        return input_string[input_number]
    
    return character_at 

def lab1Question4(file_name):
    # Read the file and return a list of all numbers in it
    list_of_nums = []
    try:
        with open(file_name, 'r') as file:
            return [int(word) for line in file for word in line.split() if word.isdigit()]
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    return list_of_nums

def lab1Question5(list_numbers):
    # Take a list of numbers
    # Return the mode from that list
    mode_of_list = None
    from collections import Counter
    
    # Find the mode using Counter
    mode_of_list = Counter(list_numbers).most_common(1)[0][0]
    
    return mode_of_list

def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = None
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

## Example of calling a function to test these... 
# Question 1 Check:
in_gb = 10
expected_bytes = 10*1024*1024*1024
calculated_bytes = lab1Question1(in_gb)

print("Input gigabytes: ", in_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
    print("Test passed")
else:
    print("Test failed")

# You can make similar tests to check if things work for you. 
# This is kind of annoying, I am aware, but it is a really important skill in programming. 
# Determining how to check if your code works, and define specific tests for what "working" means is 
# something that allows you to tackele any larger problem - you can break it into smaller bits, attack one bit at a time,
# check to ensure you've done it correctly, and then move on to the next bit.
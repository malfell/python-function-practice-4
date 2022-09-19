# 4
# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, 
# num_within(10,2,5) returns False.

# use begin and end numbers to list the range?
# list(range(begin, end + 1))
# add a plus 1 to end to make sure it's inclusive?

# then check the initial number to see if it's in the list?

def num_within(num, begin, end):
    # first get the range
    range_list = list(range(begin, end + 1))

    # check if number is in the range_list
    # if so, return true
    if(num in range_list):
        return True
    # if number doesn't exist in there, return false
    else:
        return False

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))
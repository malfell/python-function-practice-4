# 3
# Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    # -1 starts at end of the string and moves backward until it reaches the 0 index
    # revealing the initial string too
    return f'{string}: {string[::-1]}'

print(rev_string('hello'))
print(rev_string('this sentence is backwards now, wow'))
# 2
# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    # initializer must be 1! Because starting off at 0 will make the result stay 0. :(
    total = 1
    for num in list:
        # goes through the list multiplying each number by the total
        # then that number becomes new total and process repeats
        total = num * total
    # when function goes through all the list, it returns the new total
    return total

list1 = [2, 2, 2, 2]   
list2 = [1, 500]
list3 = [500, 200, 4, 4, 8, 9]
list4 = [0]
print(f"{list1} multipled together is {mult_list(list1)}")
print(f"{list2} multipled together is {mult_list(list2)}")
print(f"{list3} multipled together is {mult_list(list3)}")
print(f"{list4} multipled together is {mult_list(list4)}")
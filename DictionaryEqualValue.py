# Python3 code to demonstrate working of
# Test if all Values are Same in Dictionary
# Using loop

# initializing dictionary
test_dict = {"Gfg": 5, "is": 5, "Best": 5}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Flag to check if all elements are same
res = True

# extracting value to compare
test_val = set(list(test_dict.values()))
print(test_val)

# for ele in test_dict:
#     if test_dict[ele] != test_val:
#         res = False
#         break
#
# # printing result
# print("Are all values similar in dictionary? : " + str(res))
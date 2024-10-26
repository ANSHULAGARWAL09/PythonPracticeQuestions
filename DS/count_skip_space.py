test_str = 'geeksforgeeks 33 is   best'
print("Original Length is : ", len(test_str))

res = sum(not chr.isspace() for chr in test_str)
print("Length after skipping space",res)
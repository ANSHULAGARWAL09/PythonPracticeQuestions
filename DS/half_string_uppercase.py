test_str = 'geeksforgeek'

def uppercase_halfstr(tes_str):
    length = len(test_str)
    mid = length // 2
    add = tes_str[:mid] + tes_str[mid:].upper()
    return  add

print(uppercase_halfstr(test_str))
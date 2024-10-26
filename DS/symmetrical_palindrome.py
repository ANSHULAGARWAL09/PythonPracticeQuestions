def palin(s):
    return s == s[::-1]

def symm(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]


string = "amaamao"
if palin(string):
     print("The Enter String is palindrome")
else:
    print("The Entered String is Not Palindrome")

if symm(string):
    print("The Entered String is Symmetrical")
else:
    print("The Enter String is NOT Symmetrical")

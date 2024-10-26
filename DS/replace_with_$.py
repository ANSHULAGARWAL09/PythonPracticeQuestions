str = "Ali has all aces"

modified = ""

for i in range(0,len(str)):
    if(str[i] == 'a' or str[i] == 'A'):
        modified += '$'
    else:
        modified += str[i]
print(modified)


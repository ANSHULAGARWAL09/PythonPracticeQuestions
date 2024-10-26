Input = "geeksforgeeks"
Input1 = "ABeeIghiObhkUul"
vowels = "aeiou"

Check = False

def vowel_Accepted(In):
    for i in In:
        if i.lower() in vowels:
            Check = True

        else:
            Check = False
    return Check

print(vowel_Accepted(Input))
print(vowel_Accepted(Input1))

t = (1,2,3,4,1,1)
print(t.count(1))

s = {1,1,1,1,2,3,7}
print(s.add(10))
print(s)
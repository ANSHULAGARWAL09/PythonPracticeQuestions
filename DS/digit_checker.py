Input = "welcom2eou3rcountry1"
Input1 = "assscccaasas"

flag = False

def digitchk(I):
    for i in I:
        if i.isdigit() :
            flag = True
        else:
            flag = False
    return flag

print(digitchk(Input))
print(digitchk(Input1))


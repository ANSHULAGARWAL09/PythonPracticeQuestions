num = 19
# print(int(num / 10))

def happy_num(num):
    while(num == 1):
        n = num % 10
        square = n*n
        sum = n + square
        num = num / 10
        if(sum == 1):
            print("Happy num")
        else:
            print("Not hapyy")

print(happy_num(num))


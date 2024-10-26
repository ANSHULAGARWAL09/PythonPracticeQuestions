str="This is a python language new word"
splito = str.split()
new_str = []

for i in splito:
    if(len(i) % 2 == 0 ):
        add = new_str.append(i)

print(" ".join(new_str))

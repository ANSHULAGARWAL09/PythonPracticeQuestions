String_word = "mai pagal hu"
list1 = []

split_words = String_word.split()[::-1]
for i in split_words:
    add = list1.append(i)

print(" ".join(list1))




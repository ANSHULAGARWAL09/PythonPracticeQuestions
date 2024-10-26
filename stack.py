import array
import numpy as np

a=[1,2,3,4,5,6,7,8,9]
print(a[::3])

my_aray = array.array('i', [1, 2, 3, 9, 100, 9, 9, 9])
print("count 2",my_aray.count(2))
print("count 9", my_aray.count(9))

for i in my_aray:
    print(i)

my_ar = np.array([1,2], dtype=int)
print(my_ar)



#1
import numpy as np

#2
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]]
np_arr = np.array(a)
print()

#3
print(np_arr.shape)
print()

#4
np_02 = np_arr.reshape(3,4)
print(np_02)
print()

#5
print(np_arr[2])
print()

#6
print(np_arr * 10)
print()

#7
print(np_arr[np_arr > 7])
print()

#8
np_arr[np_arr > 7] *= 2
print(np_arr[np_arr > 7])
print()

#9
print(np_arr)
print()

#10
print(np.where(np_arr % 3 == 0, 1, 0))
print()

#11
print(np.mean(np_arr))
print(np.mean(np_arr, axis = 0))
print(np.mean(np_arr, axis = 1))
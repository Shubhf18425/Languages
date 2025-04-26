def add(x):
    return x+2
# print(add(3))

# print((lambda x: x + 2)(3))

f= lambda x: x + 2
# print(f(2))

# print((lambda x, y: x * y * y)(2, 3))

f = (lambda x : len(x))([1 ,2 ,3 , 4])

# print(f)


x=  3
f = 2 if x<3 else 4
# print(f)

f =(lambda x,y : y if x<y else x)(10,9)

# print(f)

array = [1,2,3,4,5,6,7,8,9]

f = [x*x for x in array]
# print(f)

f = list(map(lambda x:x*x, array))

# print(f


f = list(map(lambda x, y , z : x+y-z ,[1,2,3],[4,5,6],[7,8,9]))

# print(f)

f= (lambda x:x>20)(12)
# print(f)
# -----------------------------------filter
f = list(filter(lambda x:x < 10 , [1 ,2, 3, 5 , 6, 7 , 10 , 5 , 19]))

# print(f) 

f = list(filter(lambda x:x<100 , map(lambda x:x*x , [1, 2 ,3 , 4 ,5, 10 , 10 ,11 ,20])))
f = list(map(lambda x:x*x , filter(lambda x:x < 9 , [1, 2 ,3 , 4 ,5, 810 , 10 ,11 ,20])))

# print(f)
#  ------------------------------------------------ functools
n = [1 , 2 , 4 , 5 , 6 , 20 , 30]
import functools
f = functools.reduce(lambda x,y : x+y , n)
f = functools.reduce(lambda x,y : x*y , n)
f= functools.reduce(lambda x,y:x**2+y**2,[1,2,3])

f = functools.reduce(lambda x, y : x if x>y else y , [1 ,4 , 4.6 , 8.2 , 9 , 10.4 , 1, 4])

f = functools.reduce(lambda x , y : x**2 + y**2 , list(map(lambda x : x-5 , [1 ,2 ,3 ,8, 9 ,10])))
# print(f)

import numpy as np
arr = np.array([[-1 , 2, 3,4] , [3 , 4 , 5 , 8 ] , [5 , 7 , 6 , 8] , [8 , 9 ,1 ,0]])
arr = np.array([[-1 , 2] , [3 , 8 ] , [ 6 , 8] , [ 1 ,0]])
arr = np.array([[-1 , 2 , 3] , [3 , 8 , 9 ] , [ 6 , 8 , 5] , [ 1 ,0 ,9]])

temp = arr[:2 , ::2]
print(temp)
# arr[start_row:end_row, start_column:end_column:step]

# Row Slicing (:2): Selects the first two rows.
# Column Slicing (::1): Selects all columns without skipping.
# NumPy Slicing: Efficiently extracts subarrays from larger arrays.
"""messing around with numpy for the first time properly"""

import numpy as np 
# print(np.__version__)

#array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])

#array[start:end:step]

# print(array[1:4]) #prints from index 1 to index 3 (4 is exclusive)
# print(array[1:]) #prints from index 1 to the end
# print(array[:3]) #prints from the start to index 2 (3 is exclusive)
# print(array[::2]) #prints every 2nd row starting from the first row
# print(array[1::2]) #prints every 2nd row starting from the second row
# print(array[:, 1]) #prints the second column of the array
# print(array[:, 1:3]) #prints the second and third columns of the array
# print(array[0:2, 0:2]) #prints the top-left 2x2 subarray
# print(array[1:3, 1:3]) #prints the middle 2x2 subarray
# print(array[::2, ::2]) #prints every 2nd row and every 2nd column, resulting in a 2x2 subarray of the original array


#scalar arithmetic 

radii= np.array([1,2,3, 4])
print(np.pi * (radii)**2) #calculates the area of circles with the given radii using numpy's pi constant and array operations

array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])

print(array1 + array2) #element-wise addition of two arrays
print(array1 * array2) #element-wise multiplication of two arrays
print(array1 / array2) #element-wise division of two arrays
print(array1 ** array2) #element-wise exponentiation of two arrays

scores= np.array([90, 82, 70, 67])
print(scores > 75) #returns a boolean array indicating which scores are greater than 75
print(scores[scores > 75]) #returns the scores that are greater than 75

scores[scores > 75] = 100 #sets all scores greater than 75 to 100
scores[scores <= 75] = 0 #sets all scores less than or equal to 75 to 0
print(scores)



import numpy as np

arr = np.array([45, 12, 78, 23, 9, 56, 34])

print("Original:", arr)
print("Ascending:", np.sort(arr))
print("Descending:", np.sort(arr)[::-1])

arr.sort()
print("Sorted array:", arr)
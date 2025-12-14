import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Array:\n", arr)

print("Sum axis=0:", np.sum(arr, axis=0))   # column-wise sum
print("Sum axis=1:", np.sum(arr, axis=1))   # row-wise sum

print("Cumulative sum axis=0:\n", np.cumsum(arr, axis=0))
print("Cumulative sum axis=1:\n", np.cumsum(arr, axis=1))

print("Max axis=0:", np.max(arr, axis=0))
print("Max axis=1:", np.max(arr, axis=1))

print("Min axis=0:", np.min(arr, axis=0))
print("Min axis=1:", np.min(arr, axis=1))

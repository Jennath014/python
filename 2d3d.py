import numpy as np

a = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

print("Original 2D array:\n", a)
print("First row:", a[0])
print("First column:", a[:, 0])
print("Sub-array (first 2 rows & cols):\n", a[:2, :2])


b = np.array([
                [[1,2,3],
                 [4,5,6]],

                [[7,8,9],
                 [10,11,12]]
             ])

print("\nOriginal 3D array:\n", b)
print("Slice layer 0:\n", b[0])
print("Elements from all layers, row 1:\n", b[:, 1])
print("Specific slice:", b[:, :, 1])  # all layers, middle column

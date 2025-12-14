import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

odd_numbers = arr[arr % 2 != 0]

print("Odd numbers:", odd_numbers)

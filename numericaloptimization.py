import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Function to minimize
def f(x):
    return x**2 + 4*np.sin(x)

# Store optimization path
path = []
def callback(x):
    path.append(x)

# Perform optimization
result = minimize(f, x0=2, callback=callback)

# Convert path list to array
path = np.array(path)

print("Minimum found at:", result.x)
print("Minimum value:", f(result.x))

# Plot function and optimization path
x = np.linspace(-10, 10, 400)
y = f(x)

plt.plot(x, y, label='Function')
plt.scatter(path, f(path), color='red', label='Optimization Path')
plt.legend()
plt.title("Optimization Path Visualization")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

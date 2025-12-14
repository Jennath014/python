import numpy as np
import matplotlib.pyplot as plt

# Generate data
data = np.random.normal(loc=10, scale=3, size=1000)

# Plot histogram
plt.hist(data, bins=30)
plt.title("Histogram of Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

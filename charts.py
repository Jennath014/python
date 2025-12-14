import numpy as np
import matplotlib.pyplot as plt

# Sample ndarray
data = np.array([10, 20, 30, 40])

labels = ['A', 'B', 'C', 'D']

# Bar Chart
plt.bar(labels, data)
plt.title("Bar Chart")
plt.show()

# Horizontal Bar Chart
plt.barh(labels, data)
plt.title("Horizontal Bar Chart")
plt.show()

# Pie Chart
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

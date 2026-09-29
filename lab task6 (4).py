import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.scatter(x, y)
plt.title("Point Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

data = [10, 12, 15, 15, 18, 20, 22, 25, 25, 30]
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

plt.boxplot(data)
plt.title("Boxplot")
plt.show()

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
z = np.array([5, 10, 15, 20, 25])

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(x, y, z)
ax.set_title("3D Plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
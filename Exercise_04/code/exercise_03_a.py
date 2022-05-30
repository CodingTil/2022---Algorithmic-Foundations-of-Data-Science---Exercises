import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math
import numpy as np

plt.figure(figsize=(5, 5))

X_points = np.array([-2, -2, -1, 1, 2, 2])
Y_points = np.array([-5, -3, 1, -1, 3, 5])

plt.scatter(X_points, Y_points)

plt.plot([-5, 5], [-10, 10], label='1. Principal Component')

plt.gca().set_xlim(-5.5, 5.5)
plt.gca().set_ylim(-5.5, 5.5)

plt.legend(loc='lower right')

plt.savefig('exercise_03_a.png')

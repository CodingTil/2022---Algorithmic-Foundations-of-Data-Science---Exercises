import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math
import numpy as np

plt.figure(figsize=(5, 5))

u_1 = np.array([-0.354,  0.169, -0.408,  0.408,  0.548, -0.214,  0.408, -0.002])
u_2 = np.array([-0.354,  0.493, -0.149, -0.558, -0.358,  0.056,  0.408, -0.002])

plt.scatter(u_1, u_2)

plt.gca().set_xlim(-1, 1)
plt.gca().set_ylim(-1, 1)

plt.savefig('exercise_04_d.png')

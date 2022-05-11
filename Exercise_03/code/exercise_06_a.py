import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

plt.figure(figsize=(5,5))

# unit circle
polygon = Polygon([[1,0], [0,1], [-1,0], [0,-1]], closed=False)
ax = plt.gca()
ax.add_patch(polygon)
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)

plt.savefig('exercise_06_a.png')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math

plt.figure(figsize=(5,5))

plt.gca().add_patch(plt.Rectangle((-1,-1), 2, 2))

plt.gca().add_patch(plt.Circle(( -0.5 , -0.5 ), 0.5 , fc='red',ec="black"))
plt.gca().add_patch(plt.Circle(( -0.5 ,  0.5 ), 0.5 , fc='red',ec="black"))
plt.gca().add_patch(plt.Circle((  0.5 , -0.5 ), 0.5 , fc='red',ec="black"))
plt.gca().add_patch(plt.Circle((  0.5 ,  0.5 ), 0.5 , fc='red',ec="black"))
plt.gca().add_patch(plt.Circle((0 , 0), (math.sqrt(2)-1)/2 , fc='purple',ec="black"))

plt.gca().set_xlim(-1.5,1.5)
plt.gca().set_ylim(-1.5,1.5)

plt.savefig('exercise_01_a.png')

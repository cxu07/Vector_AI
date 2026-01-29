# for three
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D vectors
v1 = np.array([2, 1, 3])
v2 = np.array([1, 2, 3])
v3 = np.array([-1, -2, 1])

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

# Draw vectors
ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='v1')
ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='v2')
ax.quiver(0, 0, 0, v3[0], v3[1], v3[2], color='g', label='v3')

ax.set_xlim([-4,4])
ax.set_ylim([-4,4])
ax.set_zlim([-4,4])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("3D Vectors")
plt.show()

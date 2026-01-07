import matplotlib.pyplot as plt
import numpy as np

# 2D vectors
v1 = np.array([3, 1])
v2 = np.array([1, 3])
v3 = np.array([-2, -1])

plt.figure(figsize=(6,6))

# Draw vectors
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
plt.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='g', label='v3')

plt.xlim(-4,4)
plt.ylim(-4,4)
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.legend()
plt.title("2D Vectors")
plt.show()

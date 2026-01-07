import matplotlib.pyplot as plt

# 1D vectors
v1 = 3
v2 = -2

plt.figure(figsize=(6,1))
plt.scatter([v1, v2], [0, 0], s=100)

plt.text(v1, 0.02, "v1 = 3", ha='center')
plt.text(v2, 0.02, "v2 = -2", ha='center')

plt.axhline(0)
plt.title("1D Vectors (Number Line)")
plt.yticks([])
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns

# Example 10D vectors
X = np.array([
    [0.9,0.1,0.3,0.8,0.2,0.4,0.6,0.7,0.5,0.1],
    [0.85,0.12,0.28,0.82,0.22,0.38,0.58,0.72,0.48,0.12],
    [0.1,0.8,0.9,0.2,0.7,0.6,0.3,0.2,0.4,0.9]
])

pca = PCA(n_components=2)
X_2d = pca.fit_transform(X)


sns.heatmap(X, annot=True, cmap="viridis")
plt.title("10D vectors heatmap")
plt.xlabel("Dimension")
plt.ylabel("Vector")
plt.show()
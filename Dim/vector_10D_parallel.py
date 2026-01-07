import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
X = np.array([
    [0.9,0.1,0.3,0.8,0.2,0.4,0.6,0.7,0.5,0.1],
    [0.85,0.12,0.28,0.82,0.22,0.38,0.58,0.72,0.48,0.12],
    [0.1,0.8,0.9,0.2,0.7,0.6,0.3,0.2,0.4,0.9]
])
df = pd.DataFrame(X, columns=[f"d{i+1}" for i in range(10)])
df.plot(figsize=(10,4))
plt.title("10D vectors (Parallel Coordinates)")
plt.xlabel("Dimension")
plt.ylabel("Value")
plt.grid()
plt.show()

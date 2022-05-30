import numpy as np
from numpy import linalg as LA

L = np.array([
    [3, 0, -1, -1, -1, 0, 0, 0],
    [0, 2, -1, -1, 0, 0, 0, 0],
    [-1, -1, 3, -1, 0, 0, 0, 0],
    [-1, -1, -1, 4, 0, 0, 0, -1],
    [-1, 0, 0, 0, 4, -1, -1, -1],
    [0, 0, 0, 0, -1, 3, -1, -1],
    [0, 0, 0, 0, -1, -1, 2, 0],
    [0, 0, 0, -1, -1, -1, 0, 3]
])

eigenvalues, eigenvectors = LA.eig(L)

eigen_pairs = [(eigenvalues[i], eigenvectors[i]) for i in range(len(eigenvalues))]
eigen_pairs.sort(key=lambda tuple: tuple[0])

eigen_pairs = list(map(lambda tuple: (round(tuple[0], 3), np.round(tuple[1], 3)), eigen_pairs))

print(eigen_pairs[0])
print(eigen_pairs[1])
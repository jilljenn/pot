import numpy as np
import matplotlib.pyplot as plt

pos = np.load('points-pos.npy')
neg = np.load('points-neg.npy')

with open('matching.txt') as f:
	for line in f:
		a, b = map(int, line.split())
		print(a, b)
		plt.plot([pos[a, 0], neg[b, 0]], [pos[a, 1], neg[b, 1]], c='r')

plt.scatter(pos[:, 0], pos[:, 1], marker='.')
plt.scatter(neg[:, 0], neg[:, 1], marker='x', c='r')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
#from math import abs

N = 20
M = 30
pos = np.random.random((N, 2))
pos[:, 1] = np.abs(pos[:, 1])
neg = np.random.random((M, 2))
neg[:, 1] = -np.abs(neg[:, 1])

np.save('points-pos.npy', pos)
np.save('points-neg.npy', neg)

cost = {}
for i in range(N):
	for j in range(M):
		cost[i, j] = (pos[i][1] - neg[j][1]) ** 2 / (np.abs(pos[i][0]) + np.abs(neg[j][0]))
		print(i, j, round(10000 * cost[i, j]))

plt.scatter(pos[:, 0], pos[:, 1], marker='.')
plt.scatter(neg[:, 0], neg[:, 1], marker='x', c='r')
plt.show()

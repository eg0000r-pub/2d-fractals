import numpy as np
import matplotlib.pyplot as plt

start = np.array([
    [-0.5, 0],
    [0, 0.5*np.tan(np.pi/3)],
    [0.5, 0],
    [-0.5, 0]
])

rot = np.array([
    [np.cos(np.pi/2), -np.sin(np.pi/2)],
    [np.sin(np.pi/2), np.cos(np.pi/2)]
])

def koch(arr):
    # The new number of sides is old number of sides times four
    new_arr = []
    # Number of sides is 1 less than points in the array
    for i in range(len(arr)-1):
        side = arr[i+1, :] - arr[i, :]
        new_arr.append(arr[i, :])
        new_arr.append(arr[i, :]+side/3)
        new_arr.append(arr[i, :]+side/2+np.matmul(rot, side)/6*np.tan(np.pi/3))
        new_arr.append(arr[i, :]+2*side/3)
    new_arr.append(arr[-1, :])
    return np.array(new_arr)

n_iter = 8

for i in range(n_iter):
    start = koch(start)

plt.plot(start[:, 0], start[:, 1])
plt.gca().set_aspect('equal')
plt.show()
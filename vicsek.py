import matplotlib.pyplot as plt
import numpy as np

levels = 5

size_old = 1
data_old = np.array([1.0])

for i in range(1, levels+1):
    size = 3*size_old
    data = np.zeros([size, size])

    # Top left
    data[0:size_old, 0:size_old] = data_old
    # Bottom left
    data[0:size_old, 2*size_old:3*size_old] = data_old
    # Center
    data[size_old:2*size_old, size_old:2*size_old] = data_old
    # Top right
    data[2*size_old:3*size_old, 0:size_old] = data_old
    # Bottom right
    data[2*size_old:3*size_old, 2*size_old:3*size_old] = data_old

    size_old = size
    data_old = data

plt.imshow(data, interpolation='none')
plt.show()

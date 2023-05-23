import matplotlib.pyplot as plt
import numpy as np


num_iter = 10

colors = {
    -0.5+0.8660254j: np.array([0xff, 0, 0]),
    -0.5-0.8660254j: np.array([0, 0xff, 0]),
    0+0j: np.array([0, 0, 0xff])
}


def newton(f, df, x0):
    for i in range(num_iter):
        x0 -= f(x0)/df(x0)
    return x0


def f(x):
    return x**3+x**2+x


def df(x):
    return 3*x**2+2*x+1


r_0 = -0.5-0.5
r_f = -0.5+0.5
i_0 = -0.5
i_f = 0.5

delta = 0.0025

Rs, Is = np.meshgrid(np.arange(r_0, r_f, delta), np.arange(i_0, i_f, delta))
ans = np.zeros([np.shape(Rs)[0], np.shape(Rs)[1], 3])

for x in range(np.shape(Rs)[0]):
    for y in range(np.shape(Rs)[1]):
        sol = newton(f, df, complex(Rs[x, y], Is[x, y]))
        dist = np.inf
        for key in colors.keys():
            if abs(sol-key) < dist:
                dist = abs(sol-key)
                ans[x, y, :] = colors[key]

plt.imshow(ans, interpolation='none', extent=[r_0, r_f, i_0, i_f])
#plt.plot([0, -0.5, -0.5], [0, 0.8660254, -0.8660254], 'ok')
plt.xlabel('$Re$')
plt.ylabel('$Im$')
plt.show()
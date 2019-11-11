import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)


n = 256
x = np.linspace(-4, 4, n)
y = np.linspace(-4, 4, n)
X, Y = np.meshgrid(x, y)

plt.axes([0.05, 0.05, 0.9, 0.9])

plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
plt.clabel(C, inline=2, fontsize=5)

plt.xticks([]), plt.yticks([])
plt.show()

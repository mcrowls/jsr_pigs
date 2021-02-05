import numpy as np
import matplotlib.pyplot as plt
from sympy import *

t = Symbol('t')
growth_rate = 0.035
y = 135 / (1 + 30 * exp(-growth_rate * t))
f = lambdify(t, y, 'numpy')
t_diff = 1
y_diff = y.diff(t)
f_prime = lambdify(t, y_diff, 'numpy')
ts = np.linspace(0, 320, 30)
derivatives = f_prime(ts)
for i in range(np.size(derivatives)):
    lim = 2
    x_diff = (ts[i]+lim) - ts[i]
    y_diff = f(ts[i]+lim) - f(ts[i])
    plt.arrow(ts[i], f(ts[i]), x_diff, y_diff)

plt.show()

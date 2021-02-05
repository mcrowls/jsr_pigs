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
ts = np.linspace(0, 320, 20)
derivatives = f_prime(ts)
for i in range(np.size(derivatives)):
	lim = 5
	x_diff = (ts[i]+lim) - ts[i]
	y_diff = f(ts[i]+lim) - f(ts[i])
	plt.arrow(ts[i], f(ts[i]), x_diff, y_diff, length_includes_head=True, head_width=1, head_length=2)

plt.xlim(-20, 320)
plt.ylim(0, 150)   
plt.xlabel('Days Since Weaning')
plt.ylabel('Weights (kg)')
plt.show()

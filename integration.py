import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20)
y = 1.24 ** x

plt.plot(x, y)
plt.show()

import sympy as sym

x = sym.Symbol('x')
a = sym.integrate(1.24 **x,(x,0,20))

print("적분 값:" , round(a, 2))